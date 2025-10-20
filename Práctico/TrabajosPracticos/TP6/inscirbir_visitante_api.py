from flask import Flask, request, jsonify
from flask_cors import CORS
from actividad import Safari, Tirolesa
from visitante import Visitante

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

# Importá los modelos y servicios de persistencia
from models import db, Visitante, Actividad, Turno
from services import (
    inscribir, cancelar_inscripcion, cupo_disponible,
    CupoAgotado, RequisitosNoCumplidos, TurnoNoExiste, DobleHorario, VisitanteNoExiste
)

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app_v3.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route('/inscribir', methods=['POST'])
def inscribir_visitante_api():
    """
    Endpoint para recibir una solicitud de inscripción y procesarla.
    """
    # 1. Recibir los datos del formulario (en formato JSON)
    datos = request.get_json()

    #  Extraer los datos necesarios (deben coincidir con lo que envía React)
    nombre_actividad = datos.get('actividad')
    horario_solicitado = datos.get('horario')
    visitantes_data = datos.get('visitantes', [])  # Lista de objetos visitante

    # 3. Buscar la actividad en el estado global
    # clave_actividad = f"{nombre_actividad}-{horario_solicitado}"
    # actividad_seleccionada = ACTIVIDADES.get(clave_actividad)

    if not actividad_seleccionada:
        return jsonify({"success": False, "mensaje": "Actividad o horario no encontrado"}), 404

    # 4. Crear los objetos Visitante a partir de los datos JSON
    nuevos_visitantes = []
    for v_data in visitantes_data:
        visitante = Visitante(
            nombre=v_data['nombre'],
            dni=v_data['dni'],
            edad=v_data['edad'],
            # La talla es opcional en la clase, por eso usamos .get
            talla_vestimenta=v_data.get('talla_vestimenta'),
            acepta_tyc=v_data["acepta_tyc"]
        )
        nuevos_visitantes.append(visitante)

    # Nota: La función original 'inscribir_visitante' solo inscribe 1 a la vez.
    # En un escenario real, se debería reescribir para manejar la lista
    # o hacer un bucle para inscribir a todos los visitantes.

    if not nuevos_visitantes:
        return jsonify({"success": False, "mensaje": "No se incluyeron visitantes"}), 400
    
    
    cupo_disponible = actividad_seleccionada.cupo_total - len(actividad_seleccionada.visitantes)
    print(cupo_disponible)

    #aqui usamos las pruebas despues de haber mapeado los datos del json
    resultados = []
    for visitante in nuevos_visitantes:
        actividad_seleccionada.inscribir_visitante(visitante, horario_solicitado)
        resultados.append(ok)

    if all(resultados):
        return jsonify({
            "success": True,
            "mensaje": f"Inscripción exitosa a {nombre_actividad} a las {horario_solicitado}. "
                    f"Cantidad de inscriptos: {len(resultados)}"
        }), 201
    else:
        return jsonify({
            "success": False,
            "mensaje": "Alguna inscripción falló (sin cupo, edad o TyC no cumplidos)."
        }), 400
       


if __name__ == '__main__':

    with app.app_context():
        # Si alguna vez querés crear tablas desde el ORM (no necesario si ya existe app_v3.db):
        # db.create_all()
        pass

    # Usar 'debug=True' solo para desarrollo, permite recargar automáticamente los cambios
    app.run(debug=True)