"""Simula noviembre y escribe cobros asociados a cada prediccion.

Desde psets/proyecto/: python -m monitoreo.simular_noviembre
"""
import csv
from pathlib import Path

import pandas as pd
from fastapi.testclient import TestClient
from servicio import api

DATOS = Path(__file__).resolve().parents[3] / "laboratorios/semana-13-sesion-02/starter/ejercicio1/viajes_noviembre.csv"
SALIDA = Path(__file__).resolve().parent / "cobros.csv"


def simular():
    if api.modelo is None:
        raise RuntimeError("No hay modelo: primero exportalo desde MLflow")
    ruta = Path(api.RUTA_REGISTRO)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.unlink(missing_ok=True)
    viajes = pd.read_csv(DATOS)
    cobros = []
    with TestClient(api.app) as cliente:
        for viaje in viajes.to_dict("records"):
            real = viaje.pop("tarifa_real")
            entrada = {clave: valor for clave, valor in viaje.items() if not pd.isna(valor)}
            respuesta = cliente.post("/predecir", json=entrada)
            respuesta.raise_for_status()
            cobros.append({
                "id_prediccion": respuesta.json()["id_prediccion"],
                "tarifa_cobrada": real,
            })
        for _ in range(3):
            cliente.post("/predecir", json={"zona_origen": "Midtown"})
        print("Metricas:", cliente.get("/metricas").json())
    with SALIDA.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["id_prediccion", "tarifa_cobrada"])
        escritor.writeheader()
        escritor.writerows(cobros)
    print(f"Viajes: {len(cobros)}. Cobros: {SALIDA}")


if __name__ == "__main__":
    simular()
