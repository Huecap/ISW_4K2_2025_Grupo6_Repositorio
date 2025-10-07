

def insribir_visitante(actividad, visitante, horario):
    if len(actividad.visitantes) < actividad.cupo_total:
        actividad.visitantes.append(visitante)
        return True
    else:
        return False

