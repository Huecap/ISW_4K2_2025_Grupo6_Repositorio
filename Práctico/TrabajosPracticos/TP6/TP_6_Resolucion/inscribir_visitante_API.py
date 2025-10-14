from flask import Flask, request, jsonify
from flask_cors import CORS
from inscripcion_actividad import inscribir_visitante
from actividad import Safari, Tirolesa
from visitante import Visitante

app = Flask(__name__)
CORS(app)

# Simulación del estado global: un "parque" con actividades pre-cargadas. esto deberiamos hacerlo por bd
# o poner las actividades con los cupos una por hora con la cantidad de cupos real
ACTIVIDADES = {
    "Safari-11:00": Safari(cupo_total=2, visitantes=[], horario="11:00", tyc="Seguir al guia"),
    "Safari-9:00": Safari(cupo_total=4, visitantes=[], horario="9:00", tyc="Seguir al guia"),
    "Tirolesa-14:00": Tirolesa(8, [], "14:00", "Usar arnés"),
}

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
    clave_actividad = f"{nombre_actividad}-{horario_solicitado}"
    actividad_seleccionada = ACTIVIDADES.get(clave_actividad)

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
    resultado_inscripcion = inscribir_visitante(
        actividad_seleccionada,
        nuevos_visitantes,
        horario_solicitado
    )

    # aqui deberiamos ver que si se cumplen todas las pruebas devuelva la respuesta a React
    if resultado_inscripcion:
        return jsonify({
            "success": True,
            "mensaje": f"Inscripción exitosa a {nombre_actividad} a las {horario_solicitado}. cantidad de inscriptos: {len(nuevos_visitantes)}"
        })
    else:
        # El error puede ser por falta de cupo, horario incorrecto, o que el visitante no cumple los requisitos.
        return jsonify({"success": False, "mensaje": "No hay cupo disponible o el visitante no cumple los requisitos."}), 400

if __name__ == '__main__':
    # Usar 'debug=True' solo para desarrollo, permite recargar automáticamente los cambios
    app.run(debug=True)