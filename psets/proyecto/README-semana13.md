# Demostracion de Semana 13

La carpeta psets/proyecto/ no tenia un proyecto personal implementado. Para completar los ejercicios 3 de ambas sesiones sin inventar datos personales, aqui hay una implementacion **demostrativa** de tarifas de taxis con los CSV incluidos en los laboratorios. Debe adaptarse si tu proyecto elegido es diferente.

## Requisitos

Python 3.11 y dependencias del requirements.txt de la raiz. MLflow en 127.0.0.1:5050; en Codespaces se puede arrancar con bash .devcontainer/mlflow-server.sh desde la raiz.

## Pasos

Desde psets/proyecto/:

~~~~bash
pytest servicio/test_api.py monitoreo/test_desempeno.py -v
python -m servicio.registrar_modelo 64
python -m servicio.registrar_modelo 8
python -m servicio.promover N
python -m servicio.exportar_modelo
uvicorn servicio.api:app --port 8000
~~~~

Sustituir N por el numero de version con menor MAE que imprimen los scripts. Para el monitoreo (en otra terminal):

~~~~bash
python -m monitoreo.simular_noviembre
python -m monitoreo.desempeno --verdad monitoreo/cobros.csv
~~~~

## Archivos

- modelado/pipeline_proyecto.py: mismas features para entrenamiento e inferencia
- servicio/registrar_modelo.py, promover.py, exportar_modelo.py: ciclo de vida de MLflow
- servicio/api.py, test_api.py, Dockerfile: API, metricas, pruebas y despliegue
- monitoreo/simular_noviembre.py, desempeno.py, test_desempeno.py: simulacion, verdad y MAE
- docs/despliegue.md y docs/monitoreo.md: criterio de versionado y plan de monitoreo

Los scripts y las pruebas se han preparado, pero el servidor MLflow y las metricas reales no se consideran ejecutados hasta probarlos en un ambiente con las dependencias del curso.
