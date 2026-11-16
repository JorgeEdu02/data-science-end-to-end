# Despliegue: versionado y registro

Proyecto demostrativo: estimacion de tarifa de taxi. La carpeta del proyecto personal estaba vacia; se usa el conjunto del laboratorio para ofrecer una implementacion funcional y reproducible.

El modelo registrado se llama **tarifa-taxis-proyecto** en MLflow, experimento tarifa-taxis-proyecto. La metrica de seleccion es el **MAE en USD**, calculado en el mismo test split (20%, semilla 42) para los candidatos de 64 y 8 neuronas. No se inventa un valor de MAE ni una version de produccion: deben consultarse tras ejecutar los scripts.

## Registrar dos versiones

Desde psets/proyecto/, con MLflow en el puerto 5050:

~~~~bash
python -m servicio.registrar_modelo 64
python -m servicio.registrar_modelo 8
~~~~

Las versiones nunca se sobrescriben. Anota los numeros producidos; pueden no ser 1 y 2 si ya existe ese modelo en el registro.

## Promover

~~~~bash
python -m servicio.promover N
~~~~

Sustituye N por el numero de version con menor MAE. Se acepta una promocion si no hay una version previa o si el MAE del candidato es **estrictamente menor** que el de la actual. La persona responsable decide iniciar la promocion. MLflow deja etiquetas de auditoria: validacion, comparada_con y motivo. El alias produccion apunta a la version seleccionada.

## Exportar e iniciar servicio

~~~~bash
python -m servicio.exportar_modelo
uvicorn servicio.api:app --port 8000
pytest servicio/test_api.py monitoreo/test_desempeno.py -v
~~~~

La exportacion produce servicio/modelo.joblib y servicio/modelo_version.txt. La API responde version_modelo en /salud y en cada prediccion. La imagen incluye esos archivos y no necesita conectarse a MLflow durante inferencia. Cambiar el alias por si solo no actualiza un servicio que ya arranco.

Construccion desde la raiz del repositorio (despues de exportar):

~~~~bash
docker build -f psets/proyecto/servicio/Dockerfile -t tarifa-proyecto .
docker run --rm -p 8000:8000 -v "$(pwd)/psets/proyecto/monitoreo:/app/monitoreo" tarifa-proyecto
~~~~

## Volver a una version anterior

Desde psets/proyecto/:

~~~~bash
python -m servicio.promover 1 --rollback
python -m servicio.exportar_modelo
~~~~

Usa la version real que quieras recuperar; vuelve a construir la imagen y desplegarla. El rollback es intencional, se etiqueta como rollback_manual y debe contar con aprobacion humana. En un entorno real tambien se documenta quien autorizo el cambio y la revision desplegada.
