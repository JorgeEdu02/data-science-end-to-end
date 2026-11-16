"""Registra una version nueva: python -m servicio.registrar_modelo 64."""
import argparse
from pathlib import Path

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from modelado.pipeline_proyecto import FEATURES, crear_modelo
from servicio.config import NOMBRE_MODELO, TRACKING_URI

# Fuente demostrativa disponible en el propio repositorio.
DATOS = Path(__file__).resolve().parents[3] / "laboratorios/semana-13-sesion-01/starter/ejercicio1/viajes_features.csv"


def registrar(neuronas):
    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment("tarifa-taxis-proyecto")
    viajes = pd.read_csv(DATOS)
    X_train, X_test, y_train, y_test = train_test_split(
        viajes[FEATURES], viajes["tarifa"], test_size=0.2, random_state=42
    )
    modelo = crear_modelo(neuronas)
    modelo.fit(X_train, y_train)
    mae = float(mean_absolute_error(y_test, modelo.predict(X_test)))
    with mlflow.start_run(run_name=f"red-{neuronas}"):
        mlflow.log_param("neuronas", neuronas)
        mlflow.log_metric("mae", mae)
        info = mlflow.sklearn.log_model(
            sk_model=modelo,
            artifact_path="modelo",
            registered_model_name=NOMBRE_MODELO,
        )
    version = str(info.registered_model_version)
    print(f"Registrada version {version}; neuronas={neuronas}; MAE={mae:.4f}")
    return version, mae


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("neuronas", type=int)
    args = parser.parse_args()
    registrar(args.neuronas)
