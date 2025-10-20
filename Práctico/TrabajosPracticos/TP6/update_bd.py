# reset_db_with_cupos.py
from flask import Flask
from sqlalchemy import select
import os

from models import db, Actividad, Turno

# Ruta absoluta al app_v3.db en esta misma carpeta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "app_v3.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Configuración de cupos por actividad y horarios a crear
CUPOS = {
    "Safari": 8,
    "Tirolesa": 10,
    "Palestra": 12,
    "Jardineria": 12,
}
HORARIOS = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]  # cambiá/extendé si querés

# Atributos extra (podés ajustarlos si tu negocio lo requiere)
ATRIBUTOS_ACTIVIDAD = {
    "Safari":      dict(requiere_vestimenta=False, edad_minima=0),
    "Tirolesa":    dict(requiere_vestimenta=True,  edad_minima=8),
    "Palestra":    dict(requiere_vestimenta=True,  edad_minima=12),
    "Jardineria":  dict(requiere_vestimenta=False, edad_minima=0),
}

with app.app_context():
    print("DB absoluta:", DB_PATH)

    # ⚠️ Destructivo: borra y crea todo
    db.drop_all()
    db.create_all()

    # Crear actividades
    actividades = {}
    for nombre, extras in ATRIBUTOS_ACTIVIDAD.items():
        act = Actividad(
            nombre=nombre,
            requiere_vestimenta=extras.get("requiere_vestimenta", False),
            edad_minima=extras.get("edad_minima", 0),
        )
        db.session.add(act)
        actividades[nombre] = act

    db.session.flush()  # asigna IDs a actividades

    # Crear turnos con cupo por actividad
    for nombre, act in actividades.items():
        cupo_max = CUPOS[nombre]
        for h in HORARIOS:
            db.session.add(Turno(actividad_id=act.id, hora=h, cupo=cupo_max))

    db.session.commit()
    print("Listo ✅  Actividades y turnos recreados con cupos solicitados.")

    # Mostrar un pequeño resumen en consola
    for act in db.session.execute(select(Actividad)).scalars():
        turnos = [f"{t.hora} (cupo {t.cupo})" for t in act.turnos]
        print(f"- {act.nombre}: {', '.join(turnos)}")
