
def inscribir_visitante(actividad, nuevos_visitantes, horario):
  
    cupo_disponible = actividad.cupo_total - len(actividad.visitantes)
    if actividad.horario != horario or len(nuevos_visitantes) > cupo_disponible:
        print(" cupo disponible menor al de la inscripcion")
        print(f"cupo { cupo_disponible}")
        return False  # Falla si el horario no coincide o si el grupo no cabe.

    for visitante in nuevos_visitantes:
        if not visitante.acepta_tyc:
            print("no acepto los terminos")
            return False 

    actividad.visitantes.extend(nuevos_visitantes)
    return True