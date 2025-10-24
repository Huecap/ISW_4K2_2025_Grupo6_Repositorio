from Models.actividad import Safari, Tirolesa, Palestra, Jardineria
from Models.visitante import Visitante

def test_incripcion_exitosa():
    """Probar inscribirse a una actividad con cupos disponibles, seleccionando un horario, 
    ingresando los datos del visitante (nombre, DNI, edad, talla de la vestimenta si la actividad lo requiere) 
    y aceptando los términos y condiciones"""

    tirolesa = Tirolesa()  
    visitante = Visitante(
        nombre="Carlos", 
        dni="87654321", 
        edad=15, 
        talla_vestimenta="M",  
        acepta_tyc=True
    )
    
    resultado = tirolesa.inscribir_visitante(visitante, "11:00")
    assert resultado == True  # PASA
    
def test_inscripcion_sin_cupo():
    """Probar inscribirse a una actividad que no tiene cupo para el horario seleccionado"""

    tirolesa = Tirolesa()  # Cupo máximo: 10
    
    # Llenar todos los cupos del horario 11:00
    for i in range(10): 
        visitante = Visitante(
            nombre=f"Persona{i}", 
            dni=f"1111111{i}", 
            edad=15, 
            talla_vestimenta="M",  
            acepta_tyc=True
        )
        tirolesa.inscribir_visitante(visitante, "11:00")
    
    # Intentar inscribir uno más
    visitante_extra = Visitante(
        nombre="Extra", 
        dni="99999999", 
        edad=16, 
        talla_vestimenta="L",  # CON vestimenta
        acepta_tyc=True
    )
    resultado = tirolesa.inscribir_visitante(visitante_extra, "11:00")
    assert resultado == False # FALLA
    
def test_incripcion_sin_vestimenta_no_requerida():
    """Probar inscribirse a una actividad sin ingresar talle de vestimenta 
    cuando la actividad no lo requiere"""
    
    safari = Safari()  # Safari no requiere vestimenta
    visitante = Visitante(
        nombre="Maria", 
        dni="44444444", 
        edad=30, 
        talla_vestimenta=None,  
        acepta_tyc=True
    )
    
    resultado = safari.inscribir_visitante(visitante, "10:00")
    assert resultado == True # PASA
    
def test_inscripcion_fuera_horario():
    """Probar inscribirse a una actividad seleccionando un horario en el cual 
    el parque está cerrado o la actividad no esta disponible"""
    
    jardineria = Jardineria()  # Horarios: 09:00 a 17:00
    
    visitante = Visitante(
        nombre="Marta", 
        dni="77777777", 
        edad=40, 
        talla_vestimenta=None,
        acepta_tyc=True
    )
    
    # Intentar inscribir en horario fuera del rango de horarios disponibles
    resultado = jardineria.inscribir_visitante(visitante, "07:00")  # Actividad no disponible
    assert resultado == False # FALLA

def test_incripcion_sin_vestimenta_requerido():
    "Probar inscribirse a una actividad sin ingresar el talle de la vestimenta "
    "requerido por la actividad"

    tirolesa = Tirolesa() # Tirolesa si requiere vestimenta
    visitante = Visitante(
        nombre="Juan", 
        dni="42653547", 
        edad=35, 
        talla_vestimenta=None,  
        acepta_tyc=True
    ) 

    
    # Crear actividad Safari 
    safari = Safari()
    resultado_1 = safari.inscribir_visitante(visitante, "11:00")
    assert resultado_1 == True
        
    resultado_2 = tirolesa.inscribir_visitante(visitante, "09:00")
    assert resultado_2 == False #FALLA
     
def test_inscripcion_sin_aceptar_tyc():
    """
    Probar Inscribir un visitante a una actividad sin aceptar los terminos y condiciones
    
    """
    safari = Safari()
    visitante = Visitante(
        nombre='Juancho', 
        dni='123123123', 
        edad=23, 
        talla_vestimenta=None, 
        acepta_tyc=False
        )
    resultado = safari.inscribir_visitante(visitante=visitante, horario="08:00")
    assert resultado == False # FALLA

def test_inscripcion_multiples_actividades_mismo_horario_con_cupo():
    from Models.actividad import Safari
    from Models.actividad import Tirolesa
    from Models.visitante import Visitante
    visitante_nuevo = Visitante(
    nombre="Charlie", 
    dni="12345678", 
    edad=35, 
    talla_vestimenta="m",
    acepta_tyc=True
    )
    # Crear actividad Safari con 2 cupo, e inscribimos a un visitante
    safari = Safari()
    tirolesa = Tirolesa()
    inscripcion_1 = safari.inscribir_visitante(visitante_nuevo, "11:00")
    inscripcion_2 = tirolesa.inscribir_visitante(visitante_nuevo, "11:00")
    assert inscripcion_1 == True and inscripcion_2 == False

def test_inscripcion_multiples_actividades_distinto_horario_con_cupo():
    from Models.actividad import Safari
    from Models.actividad import Tirolesa
    from Models.visitante import Visitante
    visitante_nuevo = Visitante(
    nombre="Charlie", 
    dni="12345678", 
    edad=35, 
    talla_vestimenta="m",
    acepta_tyc=True
    )
    # Crear actividad Safari con 2 cupo, e inscribimos a un visitante
    safari = Safari()
    tirolesa = Tirolesa()
    inscripcion_1 = safari.inscribir_visitante(visitante_nuevo, "11:00")
    inscripcion_2 = tirolesa.inscribir_visitante(visitante_nuevo, "12:00")
    assert inscripcion_1 == True and inscripcion_2 == True
    
if __name__ == "__main__":
    test_incripcion_exitosa()
    test_inscripcion_sin_cupo()
    test_incripcion_sin_vestimenta_no_requerida()
    test_inscripcion_fuera_horario()
    test_incripcion_sin_vestimenta_requerido()
    test_inscripcion_sin_aceptar_tyc()
    test_inscripcion_multiples_actividades_mismo_horario_con_cupo()
    test_inscripcion_multiples_actividades_distinto_horario_con_cupo()
