
def inscribir_visitante(actividad, visitante, horario):
    if actividad.horario == horario and len(actividad.visitantes) < actividad.cupo_total and visitante.acepta_tyc == True:
        actividad.visitantes.append(visitante)
        return True
    else:
        return False
