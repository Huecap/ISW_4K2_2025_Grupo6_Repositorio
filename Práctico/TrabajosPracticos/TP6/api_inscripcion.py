from flask import Flask, request, jsonify
from flask_cors import CORS

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from db_config import db_uri, DB_PATH
from actividad import Safari, Tirolesa, Palestra, Jardineria
from visitante import Visitante as VisitanteDominio

# Modelos y ORM
from models import db, Visitante, Actividad, Turno, Inscripcion # (Actividad, Turno, Inscripcion) no los usamos directo aquí
# Servicios de dominio (validaciones y persistencia de la inscripción)
from services import (
    inscribir, cancelar_inscripcion, cupo_disponible,
    CupoAgotado, RequisitosNoCumplidos, TurnoNoExiste, DobleHorario, VisitanteNoExiste
)

print("DB absoluta usada por API:", DB_PATH)   # <- para verificar en consola

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = db_uri()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def validar_en_dominio(actividad_nombre: str, visitante_array: [dict], horario: str):
    """
    Usa las clases del dominio (actividad.py y visitante.py)
    para validar que el visitante pueda inscribirse.
    Si pasa, devuelve la instancia de VisitanteDominio validada.
    Si falla, lanza una excepción descriptiva.
    """
    # Crear visitante del dominio (no persistente)
    for visitante_data in visitante_array:
        visitante_dom = VisitanteDominio(
            nombre=visitante_data.get("nombre"),
            dni=visitante_data.get("dni"),
            edad=int(visitante_data.get("edad", 0)),
            talla_vestimenta=visitante_data.get("talla_vestimenta"),
            acepta_tyc=bool(visitante_data.get("acepta_tyc")),
        )

        # Crear actividad según nombre
        actividad_nombre = actividad_nombre.lower()
        if actividad_nombre == "safari":
            actividad_dom = Safari()
        elif actividad_nombre == "tirolesa":
            actividad_dom = Tirolesa()
        elif actividad_nombre == "palestra":
            actividad_dom = Palestra()
        elif actividad_nombre == "jardineria":
            actividad_dom = Jardineria()
        else:
            raise ValueError(f"Actividad desconocida: {actividad_nombre}")

        # Ejecutar la lógica de los tests (dominio puro)
        # Si el método inscribir_visitante lanza alguna excepción, se intercepta arriba
        resultado = actividad_dom.inscribir_visitante(visitante_dom, horario)

        if not resultado:
            raise ValueError(f"Validación fallida en dominio")

def get_or_create_visitante(v_data: dict) -> Visitante:
    dni = str(v_data.get("dni", "")).strip()
    if not dni:
        raise ValueError("Falta DNI del visitante")

    existente = db.session.scalar(select(Visitante).where(Visitante.dni == dni))
    if existente:
        # 🔁 Actualizar con los datos más recientes del formulario
        # Tomamos el valor del payload si viene; si no, dejamos el actual.
        if v_data.get("nombre"):
            existente.nombre = v_data["nombre"]
        if v_data.get("edad") is not None:
            existente.edad = int(v_data["edad"])
        # Para actividades que requieren vestimenta, permitimos actualizar el talle
        if "talla_vestimenta" in v_data:
            existente.talla_vestimenta = v_data["talla_vestimenta"]
        # Si el usuario aceptó TyC ahora, reflejarlo
        if "acepta_tyc" in v_data:
            existente.acepta_tyc = bool(v_data["acepta_tyc"])

        db.session.flush()  # aplica cambios sin cerrar la transacción
        return existente

    # 🆕 Crear si no existe
    nuevo = Visitante(
        nombre=v_data.get("nombre"),
        dni=dni,
        edad=int(v_data.get("edad", 0)),
        talla_vestimenta=v_data.get("talla_vestimenta"),
        acepta_tyc=bool(v_data.get("acepta_tyc", False)),
    )
    db.session.add(nuevo)
    db.session.flush()
    return nuevo


@app.route('/inscribir', methods=['POST'])
def inscribir_visitante_api():
    """
    Recibe JSON:
    {
      "actividad": "Safari",
      "horario": "11:00",
      "visitantes": [
        {"nombre":"Ana","dni":"123","edad":22,"talla_vestimenta":"M","acepta_tyc":true},
        {"nombre":"Luis","dni":"124","edad":19,"acepta_tyc":true}
      ]
    }
    Para cada visitante: crea si no existe (por DNI) y llama services.inscribir(visitante_id, actividad, horario).
    Responde con detalle de éxitos/errores.
    """
    

    datos = request.get_json(silent=True) or {}
    actividad = datos.get('actividad')
    horario = datos.get('horario')
    visitantes_data = datos.get('visitantes', [])

    if not actividad or not horario:
        return jsonify({"success": False, "mensaje": "Faltan 'actividad' u 'horario'."}), 400
    if not isinstance(visitantes_data, list) or not visitantes_data:
        return jsonify({"success": False, "mensaje": "Debe incluirse una lista 'visitantes' con al menos un elemento."}), 400

    resultados = []
    hubo_error = False

    # Validación lógica del dominio (igual que los tests)
    try:
        validar_en_dominio(actividad, visitantes_data, horario)
    except (ValueError) as e:
        resultados.append(str(e))

    if len(resultados) > 0:
        status=400
        return jsonify({
        "success": hubo_error,
        "actividad": actividad,
        "horario": horario,
        "resultados": resultados
    }),status

    for v_data in visitantes_data:
        try:

            
            v = get_or_create_visitante(v_data)

            # Llama a la lógica de negocio ya existente (valida TyC, edad, vestimenta, doble horario y cupo)
            insc_id = inscribir(visitante_id=v.id, actividad_nombre=actividad, horario=horario)

            resultados.append({
                "dni": v.dni,
                "visitante_id": v.id,
                "inscripcion_id": insc_id,
                "ok": True,
                "mensaje": "Inscripción exitosa"
            })
        except (ValueError,) as e:
            hubo_error = True
            resultados.append({
                "dni": v_data.get("dni"),
                "ok": False,
                "error": "DatosInvalidos",
                "mensaje": str(e)
            })
        except TurnoNoExiste:
            hubo_error = True
            resultados.append({
                "dni": v_data.get("dni"),
                "ok": False,
                "error": "TurnoNoExiste",
                "mensaje": "La actividad/horario no existe"
            })
        except RequisitosNoCumplidos:
            hubo_error = True
            resultados.append({
                "dni": v_data.get("dni"),
                "ok": False,
                "error": "RequisitosNoCumplidos",
                "mensaje": "No cumple TyC, edad mínima o vestimenta requerida"
            })
        except DobleHorario:
            hubo_error = True
            resultados.append({
                "dni": v_data.get("dni"),
                "ok": False,
                "error": "DobleHorario",
                "mensaje": "Ya tiene una inscripción en ese mismo horario"
            })
        except CupoAgotado:
            hubo_error = True
            resultados.append({
                "dni": v_data.get("dni"),
                "ok": False,
                "error": "CupoAgotado",
                "mensaje": "No hay cupo disponible para ese turno"
            })
        except Exception as e:
            hubo_error = True
            resultados.append({
                "dni": v_data.get("dni"),
                "ok": False,
                "error": "ErrorDesconocido",
                "mensaje": str(e)
            })
    db.session.commit()

    # Convención de status:
    # - 201 si todos OK
    # - 207 Multi-Status si hubo mezcla de éxitos/errores
    # - 400 si todos fallaron
    if all(r.get("ok") for r in resultados):
        status = 201
    elif any(r.get("ok") for r in resultados):
        status = 207  # mixto
    else:
        status = 400  # todo falló

    return jsonify({
        "success": not hubo_error,
        "actividad": actividad,
        "horario": horario,
        "resultados": resultados
    }), status

    #aqui usamos las pruebas despues de haber mapeado los datos del json
       

@app.get("/disponibilidad")
def disponibilidad():
    """
    Devuelve actividades con sus turnos y cupos:
    {
      "items": [
        {
          "actividad": "Safari",
          "requiere_vestimenta": false,
          "edad_minima": 0,
          "turnos": [
            {"turno_id": 1, "hora": "11:00", "cupo_max": 10, "cupo_disponible": 6}
          ]
        },
        ...
      ]
    }
    """
    actividades = db.session.execute(
        select(Actividad).order_by(Actividad.nombre)
    ).scalars().all()

    items = []
    for act in actividades:
        turnos_json = []
        for t in act.turnos:  # relación Actividad -> Turno
            disponible = cupo_disponible(act.nombre, t.hora)  # calcula en base a Inscripcion
            turnos_json.append({
                "turno_id": t.id,
                "hora": t.hora,
                "cupo_max": t.cupo,
                "cupo_disponible": disponible
            })
        items.append({
            "actividad": act.nombre,
            "requiere_vestimenta": act.requiere_vestimenta,
            "edad_minima": act.edad_minima,
            "turnos": turnos_json
        })

    return {"items": items}


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()  # descomentar solo si necesitás crear el schema
        pass
    app.run(debug=True)