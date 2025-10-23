
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError
from Models.models import db, Visitante, Actividad, Turno, Inscripcion

class CupoAgotado(Exception): ...
class RequisitosNoCumplidos(Exception): ...
class TurnoNoExiste(Exception): ...
class DobleHorario(Exception): ...
class VisitanteNoExiste(Exception): ...

def normalizar_hora(h: str) -> str:
    h = (h or "").strip()
    if ":" not in h and h != "":
        h = f"{int(h):02d}:00"
    if not h:
        return h
    hh, mm = h.split(":")
    return f"{int(hh):02d}:{int(mm or 0):02d}"

def inscribir(visitante_id: int, actividad_nombre: str, horario: str) -> int:
    horario = normalizar_hora(horario)
    with db.session.begin_nested():
        turno = db.session.scalar(
            select(Turno).join(Actividad).where(Actividad.nombre==actividad_nombre, Turno.hora==horario)
        )
        if not turno:
            raise TurnoNoExiste()

        v = db.session.get(Visitante, visitante_id)
        if not v:
            raise VisitanteNoExiste()

        # Requisitos
        if not v.acepta_tyc:
            raise RequisitosNoCumplidos()
        act = turno.actividad
        if v.edad < act.edad_minima:
            raise RequisitosNoCumplidos()
        if act.requiere_vestimenta and not v.talla_vestimenta:
            raise RequisitosNoCumplidos()

        # Mismo horario en otra actividad
        ya_mismo_horario = db.session.scalar(
            select(func.count(Inscripcion.id)).join(Turno).where(
                Inscripcion.visitante_id==visitante_id,
                Turno.hora==horario
            )
        )
        if ya_mismo_horario:
            raise DobleHorario()

        # Cupo
        inscriptos = db.session.scalar(
            select(func.count(Inscripcion.id)).where(Inscripcion.turno_id==turno.id)
        )
        if inscriptos >= turno.cupo:
            raise CupoAgotado()

        insc = Inscripcion(turno_id=turno.id, visitante_id=visitante_id)
        db.session.add(insc)
        db.session.flush()
        return insc.id

def cancelar_inscripcion(inscripcion_id: int) -> None:
    with db.session.begin():
        insc = db.session.get(Inscripcion, inscripcion_id)
        if insc:
            db.session.delete(insc)

def cupo_disponible(actividad_nombre: str, horario: str) -> int:
    horario = normalizar_hora(horario)
    turno = db.session.scalar(
        select(Turno).join(Actividad).where(Actividad.nombre==actividad_nombre, Turno.hora==horario)
    )
    if not turno:
        return 0
    usados = db.session.scalar(select(func.count(Inscripcion.id)).where(Inscripcion.turno_id==turno.id))
    return max(0, turno.cupo - (usados or 0))
