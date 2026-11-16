"""Verifica el MAE por periodo y version con datos controlados."""
import pandas as pd

from monitoreo.desempeno import resumen


def test_union_y_mae_por_version():
    pred = pd.DataFrame({
        "id_prediccion": ["a", "b", "c"],
        "fecha_hora_inicio": ["2026-11-02 10:00", "2026-11-03 10:00", "2026-11-09 10:00"],
        "version_modelo": ["1", "1", "2"],
        "tarifa_estimada": [10.0, 20.0, 30.0],
    })
    verdad = pd.DataFrame({
        "id_prediccion": ["a", "b", "c"],
        "tarifa_cobrada": [12.0, 18.0, 36.0],
    })
    tabla = resumen(pred, verdad).reset_index()
    assert tabla["mae"].tolist() == [2.0, 6.0]
    assert tabla["casos_con_verdad"].tolist() == [2, 1]


def test_sin_verdad_no_finge_mae():
    pred = pd.DataFrame({
        "id_prediccion": ["a"],
        "fecha_hora_inicio": ["2026-11-02 10:00"],
        "version_modelo": ["1"],
        "tarifa_estimada": [15.0],
    })
    assert "mae" not in resumen(pred).columns
