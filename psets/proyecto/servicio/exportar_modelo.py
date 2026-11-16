"""Congela el modelo y su version, sin depender de MLflow durante inferencia.

python -m servicio.exportar_modelo
"""
from pathlib import Path

import joblib
import mlflow.sklearn
from mlflow import MlflowClient

from servicio.config import ALIAS, NOMBRE_MODELO, TRACKING_URI


def exportar():
    mlflow.set_tracking_uri(TRACKING_URI)
    version = str(MlflowClient(tracking_uri=TRACKING_URI).get_model_version_by_alias(NOMBRE_MODELO, ALIAS).version)
    modelo = mlflow.sklearn.load_model(f"models:/{NOMBRE_MODELO}/{version}")
    directorio = Path(__file__).resolve().parent
    joblib.dump(modelo, directorio / "modelo.joblib")
    (directorio / "modelo_version.txt").write_text(version, encoding="utf-8")
    print(f"Modelo exportado: {NOMBRE_MODELO}, version {version}")
    return version


if __name__ == "__main__":
    exportar()
