from inscripcion_actividad import inscribir_visitante

def test_sin_aceptar_tyc():
    from actividad import Safari
    from visitante import Visitante
    visitante_nuevo = Visitante(
    nombre="David", 
    dni="87654321", 
    edad=28, 
    talla_vestimenta="m",
    acepta_tyc=False

    )
    # Crear actividad Safari con 2 cupo, e inscribimos a un visitante
    safari = Safari(2, [], "11:00", "Seguir al guia")
    resultado = inscribir_visitante(safari, visitante_nuevo, "11:00")
    assert resultado == False

def test_aceptar_tyc():
    from actividad import Safari
    from visitante import Visitante
    visitante_nuevo = Visitante(
    nombre="David", 
    dni="87654321", 
    edad=28, 
    talla_vestimenta="m",
    acepta_tyc=True

    )
    # Crear actividad Safari con 2 cupo, e inscribimos a un visitante
    safari = Safari(2, [], "11:00", "Seguir al guia")
    resultado = inscribir_visitante(safari, visitante_nuevo, "11:00")
    assert resultado == True


if __name__ == "__main__":
    test_sin_aceptar_tyc()
    test_aceptar_tyc()