from inscripcion_actividad import insribir_visitante

def test_sin_cupo():
    from actividad import Safari
    # Crear actividad Safari con 1 cupo, e inscribimos a un visitante
    safari = Safari(1, ["Charlie"], "11:00", "Seguir al guia")
    
    # Probamos inscribir a otro visitante cuando no hay cupo
    resultado = insribir_visitante(safari, "David", "11:00")
    assert resultado == False

def test_con_cupo():
    from actividad import Safari
    # Crear actividad Safari con 2 cupo, e inscribimos a un visitante
    safari = Safari(2, ["Charlie"], "11:00", "Seguir al guia")
    # Probamos inscribir a otro visitante cuando no hay cupo
    resultado = insribir_visitante(safari, "David", "11:00")
    assert resultado == True
    
if __name__ == "__main__":
    
    test_con_cupo()
    test_sin_cupo()