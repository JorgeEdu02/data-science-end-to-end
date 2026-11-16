"""Configuracion compartida del registro y el servicio."""
import os

NOMBRE_MODELO = "tarifa-taxis-proyecto"
ALIAS = "produccion"
TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:5050")
