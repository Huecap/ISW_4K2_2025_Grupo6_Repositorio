from actividad import Safari, Tirolesa, Palestra, Jardineria
from visitante import Visitante

def test_incripcion_exitosa():
    """Probar inscribirse a una actividad con cupos disponibles, seleccionando un horario, 
    ingresando los datos del visitante (nombre, DNI, edad, talla de la vestimenta si la actividad lo requiere) 
    y aceptando los términos y condiciones"""

    safari = Safari()
    visitante_safari = Visitante(
        nombre="Ana", 
        dni="12345678", 
        edad=25, 
        talla_vestimenta=None,  # No requiere vestimenta
        acepta_tyc=True
    )
    
    resultado_safari = safari.inscribir_visitante(visitante_safari, "10:00")
    assert resultado_safari == True  # PASA
    
    
def test_inscripcion_sin_cupo():
    """Probar inscribirse a una actividad que no tiene cupo para el horario seleccionado"""
    safari = Safari()
    
    # Llenar todos los cupos del horario 10:00
    for i in range(8):  # Safari tiene cupo máximo 8
        visitante = Visitante(
            nombre=f"Persona{i}", 
            dni=f"1111111{i}", 
            edad=20, 
            talla_vestimenta=None,
            acepta_tyc=True
        )
        safari.inscribir_visitante(visitante, "10:00")
    
    # Intentar inscribir uno más
    visitante_extra = Visitante(
        nombre="Extra", 
        dni="99999999", 
        edad=30, 
        talla_vestimenta=None,
        acepta_tyc=True
    )
    resultado = safari.inscribir_visitante(visitante_extra, "10:00")
    assert resultado == False  # Debe fallar por falta de cupo
    
    
if __name__ == "__main__":
    
    test_incripcion_exitosa()
    test_inscripcion_sin_cupo()