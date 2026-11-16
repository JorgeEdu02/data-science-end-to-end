"""Promocion por MAE o rollback explicito.

python -m servicio.promover 2
python -m servicio.promover 1 --rollback
"""
import argparse

from mlflow import MlflowClient
from mlflow.exceptions import MlflowException

from servicio.config import ALIAS, NOMBRE_MODELO, TRACKING_URI


def mae_de(cliente, version):
    run_id = cliente.get_model_version(NOMBRE_MODELO, str(version)).run_id
    return float(cliente.get_run(run_id).data.metrics["mae"])


def promover(version, rollback=False):
    cliente = MlflowClient(tracking_uri=TRACKING_URI)
    try:
        actual = cliente.get_model_version_by_alias(NOMBRE_MODELO, ALIAS).version
    except MlflowException:
        actual = None

    candidato = mae_de(cliente, version)
    referencia = mae_de(cliente, actual) if actual is not None else None
    aprobado = rollback or referencia is None or candidato < referencia
    cliente.set_model_version_tag(NOMBRE_MODELO, str(version), "comparada_con", str(actual) if actual else "ninguna")
    cliente.set_model_version_tag(NOMBRE_MODELO, str(version), "validacion", "aprobada" if aprobado else "rechazada")
    cliente.set_model_version_tag(NOMBRE_MODELO, str(version), "motivo", "rollback_manual" if rollback else "mae_menor")
    if aprobado:
        cliente.set_registered_model_alias(NOMBRE_MODELO, ALIAS, str(version))
    print(f"Version {version}: MAE={candidato:.4f}; actual={actual}; promovida={aprobado}")
    return aprobado


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    parser.add_argument("--rollback", action="store_true")
    args = parser.parse_args()
    promover(args.version, args.rollback)
