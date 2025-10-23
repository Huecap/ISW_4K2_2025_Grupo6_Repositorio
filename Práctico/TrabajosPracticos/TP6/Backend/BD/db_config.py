# db_config.py
import os

# Siempre usar el .db que está en ESTA carpeta (la del código)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "app_v3.db")

def db_uri():
    return f"sqlite:///{DB_PATH}"