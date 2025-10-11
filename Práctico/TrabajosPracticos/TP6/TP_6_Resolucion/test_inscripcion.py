from inscripcion_actividad import inscribir_visitante

def test_sin_cupo():
    from actividad import Safari
    from visitante import Visitante
    visitante_existente = Visitante(
    nombre="Charlie", 
    dni="12345678", 
    edad=35, 
    talla_vestimenta="m",
    acepta_tyc=True

    )
    visitante_nuevo = Visitante(
    nombre="David", 
    dni="87654321", 
    edad=28, 
    talla_vestimenta="m",
    acepta_tyc=True

    )

    # Crear actividad Safari con 1 cupo, e inscribimos a un visitante
    safari = Safari(1, [visitante_existente], "11:00", "Seguir al guia")
    
    # Probamos inscribir a otro visitante cuando no hay cupo
    resultado = inscribir_visitante(safari, visitante_nuevo, "11:00")
    assert resultado == False


def test_con_cupo():
    from actividad import Safari
    from visitante import Visitante
    visitante_existente = Visitante(
    nombre="Charlie", 
    dni="12345678", 
    edad=35, 
    talla_vestimenta="m",
    acepta_tyc=True
    )
    visitante_nuevo = Visitante(
    nombre="David", 
    dni="87654321", 
    edad=28, 
    talla_vestimenta="m",
    acepta_tyc=True

    )
    # Crear actividad Safari con 2 cupo, e inscribimos a un visitante
    safari = Safari(2, [visitante_existente], "11:00", "Seguir al guia")
    # Probamos inscribir a otro visitante cuando no hay cupo
    resultado = inscribir_visitante(safari, visitante_nuevo, "11:00")
    assert resultado == True
    
if __name__ == "__main__":
    
    test_con_cupo()
    test_sin_cupo()