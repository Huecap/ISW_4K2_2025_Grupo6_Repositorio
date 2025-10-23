
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint, CheckConstraint, func

db = SQLAlchemy()

class Visitante(db.Model):
    __tablename__ = "visitante"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    dni = db.Column(db.String(32), nullable=False, unique=True)
    edad = db.Column(db.Integer, nullable=False)
    talla_vestimenta = db.Column(db.String(8))
    acepta_tyc = db.Column(db.Boolean, nullable=False, default=False)

    inscripciones = db.relationship("Inscripcion", back_populates="visitante", cascade="all, delete-orphan")

class Actividad(db.Model):
    __tablename__ = "actividad"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False, unique=True)
    requiere_vestimenta = db.Column(db.Boolean, nullable=False, default=False)
    edad_minima = db.Column(db.Integer, nullable=False, default=0)

    turnos = db.relationship("Turno", back_populates="actividad", cascade="all, delete-orphan")

class Turno(db.Model):
    __tablename__ = "turno"
    id = db.Column(db.Integer, primary_key=True)
    actividad_id = db.Column(db.Integer, db.ForeignKey("actividad.id"), nullable=False, index=True)
    hora = db.Column(db.String(5), nullable=False)  # 'HH:MM'
    cupo = db.Column(db.Integer, nullable=False)

    actividad = db.relationship("Actividad", back_populates="turnos")
    inscripciones = db.relationship("Inscripcion", back_populates="turno", cascade="all, delete-orphan")

    __table_args__ = (
        UniqueConstraint("actividad_id", "hora", name="uq_actividad_hora"),
        CheckConstraint("cupo >= 0", name="ck_cupo_nonneg"),
    )

class Inscripcion(db.Model):
    __tablename__ = "inscripcion"
    id = db.Column(db.Integer, primary_key=True)
    turno_id = db.Column(db.Integer, db.ForeignKey("turno.id"), nullable=False, index=True)
    visitante_id = db.Column(db.Integer, db.ForeignKey("visitante.id"), nullable=False, index=True)
    ts = db.Column(db.DateTime, server_default=func.current_timestamp(), nullable=False)

    turno = db.relationship("Turno", back_populates="inscripciones")
    visitante = db.relationship("Visitante", back_populates="inscripciones")

    __table_args__ = (
        UniqueConstraint("turno_id", "visitante_id", name="uq_turno_visitante"),
    )
