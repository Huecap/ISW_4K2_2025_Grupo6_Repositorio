from abc import ABC

class Actividad(ABC):
    def __init__(self, nombre, cupo_total, edad_minima, requiere_vestimenta, tyc, horarios_disponibles):
        self.nombre = nombre
        self.cupo_total = cupo_total
        self.edad_minima = edad_minima
        self.requiere_vestimenta = requiere_vestimenta
        self.tyc = tyc
        self.horarios_disponibles = horarios_disponibles
        self.visitantes_por_horario = {} # {horario: [visitantes]}

    def validar_inscripcion(self, visitante, horario):
        if not self.es_horario_valido(horario):
            return False  # Horario no disponible
        if not self.tiene_cupo_disponible(horario):
            return False  # No hay cupos
        if not self.edad_es_valida(visitante.edad):
            return False  # Edad insuficiente
        if self.requiere_vestimenta and not visitante.talla_vestimenta:
            return False  # Falta talla de vestimenta
        return True

    def inscribir_visitante(self, visitante, horario):
        if not self.validar_inscripcion(visitante, horario):
            return False # No cumple alugna validacion
        if not visitante.acepta_tyc:
            return False  # No aceptó términos
        if visitante.esta_inscrito_en_horario(horario):
            return False  # Ya inscrito en otro actividad mismo horario
        
        if horario not in self.visitantes_por_horario:
            self.visitantes_por_horario[horario] = []
        
        self.visitantes_por_horario[horario].append(visitante)
        visitante.agregar_inscripcion(self, horario)
        return True

    def es_horario_valido(self, horario):
        return horario in self.horarios_disponibles

    def tiene_cupo_disponible(self, horario):
        if horario not in self.visitantes_por_horario:
            return True
        return len(self.visitantes_por_horario[horario]) < self.cupo_total

    def edad_es_valida(self, edad):
        return edad >= self.edad_minima

    def obtener_cupos_disponibles(self, horario):
        if horario not in self.visitantes_por_horario:
            return self.cupo_total
        return self.cupo_total - len(self.visitantes_por_horario[horario])

class Tirolesa(Actividad):
    def __init__(self):
        tyc = "Uso obligatorio de arnés y casco, edad mínima 8 años"
        horarios = ["09:00", "11:00", "13:00", "15:00", "17:00"]
        super().__init__(
            nombre="Tirolesa",
            cupo_total=10,
            edad_minima=8,
            requiere_vestimenta=True,
            tyc=tyc,
            horarios_disponibles=horarios
        )

class Safari(Actividad):
    def __init__(self):
        tyc = "Seguir instrucciones del guía, no alimentar animales"
        horarios = ["10:00", "12:00", "14:00", "16:00"]
        super().__init__(
            nombre="Safari",
            cupo_total=8,
            edad_minima=0,
            requiere_vestimenta=False,
            tyc=tyc,
            horarios_disponibles=horarios
        )

class Palestra(Actividad):
    def __init__(self):
        tyc = "Equipo de seguridad obligatorio, edad mínima 12 años"
        horarios = ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00"]
        super().__init__(
            nombre="Palestra",
            cupo_total=12,
            edad_minima=12,
            requiere_vestimenta=True,
            tyc=tyc,
            horarios_disponibles=horarios
        )

class Jardineria(Actividad):
    def __init__(self):
        tyc = " Uso de guantes de protección, todas las edades"
        horarios = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
        super().__init__(
            nombre="Jardineria",
            cupo_total=12,
            edad_minima=0,
            requiere_vestimenta=False,
            tyc=tyc,
            horarios_disponibles=horarios
        )    