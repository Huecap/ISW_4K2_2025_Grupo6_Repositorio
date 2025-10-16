from actividad import Actividad

class Visitante:
    def __init__(self, nombre: str, dni: int, edad: int, talla_vestimenta: str|None, acepta_tyc: bool):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.talla_vestimenta = talla_vestimenta
        self.acepta_tyc = acepta_tyc
        self.inscripciones = [] # [(actividad.nombre, "hh:mm"), (), ...]

    def agregar_inscripcion(self, actividad: Actividad, horario: str):
        self.inscripciones.append((actividad.nombre, horario))

    def esta_inscrito_en_horario(self, horario):
        for inscripcion in self.inscripciones:
            if inscripcion['horario'] == horario:
                return True
        return False