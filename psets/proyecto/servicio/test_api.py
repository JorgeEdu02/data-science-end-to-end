"""Pruebas sin modelo real ni servidor MLflow."""
import json

import pytest
from fastapi.testclient import TestClient

from servicio import api


VIAJE = {
    "fecha_hora_inicio": "2026-11-05T08:30:00",
    "zona_origen": "Midtown",
    "zona_destino": "JFK Airport",
    "distancia_km": 26.4,
    "pasajeros": 2,
    "metodo_pago": "tarjeta",
}


class ModeloFalso:
    def predict(self, datos):
        return [20.0]


class ModeloConError:
    def predict(self, datos):
        raise RuntimeError("Falla simulada")


@pytest.fixture
def cliente(tmp_path, monkeypatch):
    monkeypatch.setattr(api, "modelo", ModeloFalso())
    monkeypatch.setattr(api, "version_modelo", "7")
    monkeypatch.setattr(api, "RUTA_REGISTRO", tmp_path / "predicciones.jsonl")
    monkeypatch.setattr(api, "metricas", api.Metricas())
    with TestClient(api.app, raise_server_exceptions=False) as cliente:
        yield cliente


def test_version_y_registro(cliente):
    respuesta = cliente.post("/predecir", json=VIAJE)
    assert respuesta.status_code == 200
    cuerpo = respuesta.json()
    assert cuerpo["version_modelo"] == "7"
    assert cuerpo["tarifa_estimada"] == 20.0
    with open(api.RUTA_REGISTRO, encoding="utf-8") as archivo:
        fila = json.loads(archivo.readline())
    assert fila["id_prediccion"] == cuerpo["id_prediccion"]
    assert fila["version_modelo"] == "7"
    assert fila["zona_destino"] == "JFK Airport"
    assert fila["momento"]


def test_metricas_validacion_y_servidor(cliente, monkeypatch):
    assert cliente.post("/predecir", json=VIAJE).status_code == 200
    assert cliente.post("/predecir", json={"zona_origen": "Midtown"}).status_code == 422
    monkeypatch.setattr(api, "modelo", ModeloConError())
    assert cliente.post("/predecir", json=VIAJE).status_code == 500
    met = cliente.get("/metricas").json()
    assert met["peticiones"] == 3
    assert met["errores_validacion"] == 1
    assert met["errores_servidor"] == 1
    assert met["latencia_p50_ms"] > 0
    assert met["latencia_p95_ms"] >= met["latencia_p50_ms"]
