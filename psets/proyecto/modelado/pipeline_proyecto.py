"""Preparacion reproducible de las tarifas de taxi (proyecto demostrativo)."""

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

NUMERICAS = ["distancia_km", "pasajeros"]
CALCULADAS = ["hora_sin", "hora_cos", "es_fin_de_semana", "es_hora_pico", "es_tarifa_fija"]
CATEGORICAS = ["zona_origen", "zona_destino", "metodo_pago"]
FEATURES = NUMERICAS + CALCULADAS + CATEGORICAS
ZONAS_MANHATTAN = ["Midtown", "Upper East Side", "Upper West Side", "Lower Manhattan", "Harlem"]


def agregar_features(viajes):
    viajes = viajes.copy()
    inicio = pd.to_datetime(viajes["fecha_hora_inicio"])
    hora = inicio.dt.hour
    viajes["hora_sin"] = np.sin(2 * np.pi * hora / 24).round(4)
    viajes["hora_cos"] = np.cos(2 * np.pi * hora / 24).round(4)
    viajes["es_fin_de_semana"] = (inicio.dt.dayofweek >= 5).astype(int)
    viajes["es_hora_pico"] = (
        hora.isin([7, 8, 9, 16, 17, 18, 19]) & (viajes["es_fin_de_semana"] == 0)
    ).astype(int)
    a_jfk = viajes["zona_origen"].isin(ZONAS_MANHATTAN) & (viajes["zona_destino"] == "JFK Airport")
    desde_jfk = (viajes["zona_origen"] == "JFK Airport") & viajes["zona_destino"].isin(ZONAS_MANHATTAN)
    viajes["es_tarifa_fija"] = (a_jfk | desde_jfk).astype(int)
    return viajes


def preparar():
    return ColumnTransformer([
        ("numericas", Pipeline([
            ("imputar", SimpleImputer(strategy="median")),
            ("escalar", StandardScaler()),
        ]), NUMERICAS),
        ("calculadas", "passthrough", CALCULADAS),
        ("categoricas", Pipeline([
            ("imputar", SimpleImputer(strategy="most_frequent")),
            ("codificar", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
        ]), CATEGORICAS),
    ])


def crear_modelo(neuronas=64):
    return Pipeline([
        ("preparar", preparar()),
        ("modelo", MLPRegressor(hidden_layer_sizes=(neuronas,), max_iter=1000, random_state=42)),
    ])
