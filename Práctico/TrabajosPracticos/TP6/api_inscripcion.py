from flask import Flask, request, jsonify
from flask_cors import CORS

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from db_config import db_uri, DB_PATH

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


def get_or_create_visitante(v_data: dict) -> Visitante:
    dni = str(v_data.get("dni", "")).strip()
    if not dni:
        raise ValueError("Falta DNI del visitante")

    existente = db.session.scalar(select(Visitante).where(Visitante.dni == dni))
    if existente:
        return existente

    nuevo = Visitante(
        nombre=v_data.get("nombre"),
        dni=dni,
        edad=int(v_data.get("edad", 0)),
        talla_vestimenta=v_data.get("talla_vestimenta"),
        acepta_tyc=bool(v_data.get("acepta_tyc", False)),
    )
    db.session.add(nuevo)
    # ❌ antes hacías commit aquí, lo quitamos
    db.session.flush()  # asigna ID sin cerrar transacción
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