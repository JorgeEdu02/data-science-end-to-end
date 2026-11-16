"""Monitoreo semanal por version. Cruza predicciones con cobros reales.

python -m monitoreo.desempeno --verdad monitoreo/cobros.csv
python -m monitoreo.desempeno  # indicadores indirectos sin verdad
"""
import argparse
from pathlib import Path

import pandas as pd

CARPETA = Path(__file__).resolve().parent


def resumen(predicciones, verdad=None):
    datos = predicciones.copy()
    datos["semana"] = pd.to_datetime(datos["fecha_hora_inicio"]).dt.to_period("W").dt.start_time.dt.date
    grupos = ["semana", "version_modelo"]
    indirectas = datos.groupby(grupos, dropna=False).agg(
        peticiones=("id_prediccion", "size"),
        tarifa_media_predicha=("tarifa_estimada", "mean"),
    )
    if verdad is None:
        return indirectas.round(3)
    if verdad["id_prediccion"].duplicated().any():
        raise ValueError("La verdad contiene id_prediccion duplicados")
    unidos = datos.merge(verdad, on="id_prediccion", how="inner", validate="one_to_one")
    unidos["error_absoluto"] = (unidos["tarifa_estimada"] - unidos["tarifa_cobrada"]).abs()
    resultados = unidos.groupby(grupos, dropna=False).agg(
        casos_con_verdad=("id_prediccion", "size"),
        mae=("error_absoluto", "mean"),
    )
    return indirectas.join(resultados, how="left").round(3)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--registro", type=Path, default=CARPETA / "predicciones.jsonl")
    parser.add_argument("--verdad", type=Path, default=None)
    args = parser.parse_args()
    if not args.registro.exists():
        raise SystemExit(f"No existe el registro: {args.registro}")
    pred = pd.read_json(args.registro, lines=True)
    verdad = pd.read_csv(args.verdad) if args.verdad else None
    print(resumen(pred, verdad).to_string())


if __name__ == "__main__":
    main()
