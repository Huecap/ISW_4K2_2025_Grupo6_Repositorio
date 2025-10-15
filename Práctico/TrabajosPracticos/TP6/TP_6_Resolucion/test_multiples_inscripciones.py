from inscripcion_actividad import inscribir_visitante

def test_inscripcion_multiples_actividades_mismo_horario_con_cupo():
    from actividad import Safari
    from actividad import Tirolesa
    from visitante import Visitante
    visitante_nuevo = Visitante(
    nombre="Charlie", 
    dni="12345678", 
    edad=35, 
    talla_vestimenta="m",
    acepta_tyc=True
    )
    # Crear actividad Safari con 2 cupo, e inscribimos a un visitante
    safari = Safari(2, [], "11:00", "Seguir al guia")
    tirolesa = Tirolesa(2, [], "11:00", "Seguir al guia")
    inscripcion_1 = inscribir_visitante(safari, visitante_nuevo, "11:00")
    inscripcion_2 = inscribir_visitante(tirolesa, visitante_nuevo, "11:00")
    assert inscripcion_1 == True & inscripcion_2 == False

def test_inscripcion_multiples_actividades_distinto_horario_con_cupo():
    from actividad import Safari
    from actividad import Tirolesa
    from visitante import Visitante
    visitante_nuevo = Visitante(
    nombre="Charlie", 
    dni="12345678", 
    edad=35, 
    talla_vestimenta="m",
    acepta_tyc=True
    )
    # Crear actividad Safari con 2 cupo, e inscribimos a un visitante
    safari = Safari(2, [], "11:00", "Seguir al guia")
    tirolesa = Tirolesa(2, [], "12:00", "Seguir al guia")
    inscripcion_1 = inscribir_visitante(safari, visitante_nuevo, "11:00")
    inscripcion_2 = inscribir_visitante(tirolesa, visitante_nuevo, "12:00")
    assert inscripcion_1 == True & inscripcion_2 == False

if __name__ == "__main__":
    test_inscripcion_multiples_actividades_mismo_horario_con_cupo()
    test_inscripcion_multiples_actividades_distinto_horario_con_cupo()