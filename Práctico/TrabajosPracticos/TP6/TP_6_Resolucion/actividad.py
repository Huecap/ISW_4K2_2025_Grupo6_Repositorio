from abc import ABC, abstractmethod

class Actividad(ABC):
    def __init__(self, cupo_total, visitantes, horario, tyc):
        self.cupo_total = cupo_total
        self.visitantes = visitantes
        self.horario = horario
        self.tyc = tyc

class Tirolesa(Actividad):
    def __init__(self, cupo, visitantes, horarios, tyc):
        super().__init__(cupo, visitantes, horarios, tyc)
        self.nombre = "Tirolesa"
    
class Safari(Actividad):
    def __init__(self, cupo_total, visitantes, horario, tyc):
        super().__init__(cupo_total, visitantes, horario, tyc)
        self.nombre = "Safari"

class Palestra(Actividad):
    def __init__(self, cupo_total, visitantes, horario, tyc):
        super().__init__(cupo_total, visitantes, horario, tyc)
        self.nombre = "Palestra"

class Jardineria(Actividad):
    def __init__(self, cupo_total, visitantes, horario, tyc):
        super().__init__(cupo_total, visitantes, horario, tyc)
        self.nombre = "Jardineria"
