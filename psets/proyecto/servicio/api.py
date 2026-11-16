"""Servicio de tarifas con trazabilidad y metricas HTTP."""
import json
import os
import threading
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from modelado.pipeline_proyecto import FEATURES, agregar_features

DIRECTORIO = Path(__file__).resolve().parent
RUTA_MODELO = DIRECTORIO / "modelo.joblib"
RUTA_VERSION = DIRECTORIO / "modelo_version.txt"
RUTA_REGISTRO = Path(os.getenv("RUTA_REGISTRO", str(DIRECTORIO.parent / "monitoreo/predicciones.jsonl")))

modelo = joblib.load(RUTA_MODELO) if RUTA_MODELO.exists() else None
version_modelo = RUTA_VERSION.read_text(encoding="utf-8").strip() if RUTA_VERSION.exists() else None
candado_registro = threading.Lock()


class Metricas:
    def __init__(self):
        self.latencias_ms = []
        self.codigos = []
        self.candado = threading.Lock()

    def registrar(self, ms, codigo):
        with self.candado:
            self.latencias_ms.append(ms)
            self.codigos.append(codigo)

    def resumen(self):
        with self.candado:
            tiempos = list(self.latencias_ms)
            codigos = list(self.codigos)
        return {
            "peticiones": len(codigos),
            "errores_validacion": sum(x == 422 for x in codigos),
            "errores_servidor": sum(x >= 500 for x in codigos),
            "latencia_p50_ms": round(float(np.percentile(tiempos, 50)), 2) if tiempos else None,
            "latencia_p95_ms": round(float(np.percentile(tiempos, 95)), 2) if tiempos else None,
        }


metricas = Metricas()
app = FastAPI(title="Tarifa taxis: proyecto demostrativo")


class Viaje(BaseModel):
    fecha_hora_inicio: datetime
    zona_origen: str
    zona_destino: str
    distancia_km: float | None = Field(default=None, ge=0)
    pasajeros: float | None = Field(default=None, ge=1)
    metodo_pago: str | None = None


@app.middleware("http")
async def medir(request: Request, call_next):
    if request.url.path != "/predecir":
        return await call_next(request)
    inicio = time.perf_counter()
    try:
        respuesta = await call_next(request)
    except Exception:
        metricas.registrar((time.perf_counter() - inicio) * 1000, 500)
        raise
    metricas.registrar((time.perf_counter() - inicio) * 1000, respuesta.status_code)
    return respuesta


@app.get("/salud")
def salud():
    return {
        "estado": "ok" if modelo is not None else "sin_modelo",
        "modelo_cargado": modelo is not None,
        "version_modelo": version_modelo,
    }


@app.get("/metricas")
def ver_metricas():
    return metricas.resumen()


@app.post("/predecir")
def predecir(viaje: Viaje):
    if modelo is None:
        raise HTTPException(status_code=503, detail="Primero exporta un modelo de produccion")
    datos = agregar_features(pd.DataFrame([viaje.model_dump()]))
    tarifa = round(float(modelo.predict(datos[FEATURES])[0]), 2)
    identificador = uuid.uuid4().hex
    registro = {
        "id_prediccion": identificador,
        "momento": datetime.now(timezone.utc).isoformat(),
        "version_modelo": version_modelo,
        **viaje.model_dump(mode="json"),
        "tarifa_estimada": tarifa,
    }
    with candado_registro:
        ruta = Path(RUTA_REGISTRO)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with ruta.open("a", encoding="utf-8") as archivo:
            archivo.write(json.dumps(registro) + "\n")
    return {"id_prediccion": identificador, "tarifa_estimada": tarifa, "version_modelo": version_modelo}
