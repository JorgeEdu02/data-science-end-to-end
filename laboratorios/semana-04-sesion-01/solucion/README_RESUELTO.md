# Semana 4, sesión 1 — Orquestación

## Preguntas iniciales
**Cron vs. Kestra:** cron lanza comandos a una hora; un orquestador registra ejecuciones y estados, permite dependencias, reintentos y backfill. Errores posibles: API caída, cortes de red, datos incompletos, permisos, credenciales vencidas o fallo parcial.

## Ejercicio 1 — Flow diario
`solucion/ejercicio1/flow_ingesta.yml` incluye hasta 3 intentos con espera de 10 s, imprime `trigger.date ?? execution.startDate` y define `0 6 * * *` para las 06:00 cada día. Se trata de un flow con múltiples ejecuciones separadas; si cada intento falla con probabilidad 0,5 independientemente, tres fallos consecutivos tienen probabilidad aproximada de 0,125. Una ejecución fallida no deshabilita automáticamente el trigger del día siguiente.

## Ejercicio 2 — Flow de clima
`solucion/ejercicio2/flow_clima.yml` incluye 4 intentos a intervalos de 5 s, recibe fecha del trigger y se ejecuta lunes 07:00 (`0 7 * * 1`). El backfill debe configurarse manualmente desde Kestra sobre los tres lunes anteriores; cada ejecución histórica debe recibir **su propia fecha**, no la fecha de hoy, o escribiría registros incorrectos. Reintentos resuelven fallas transitorias, mientras que backfill reejecuta periodos históricos.

Los resultados de `comprobar.py`, logs, backfill y número observado de intentos requieren desplegar Kestra. **No se ha simulado ni confirmado un backfill real**.

## Ejercicio 3
`solucion/flow_proyecto.yml` propone actualización semanal para un pipeline de datos de futbol y ejecuta una imagen local `futbol-ingesta:latest` con `pullPolicy: NEVER`. Es un ejemplo que requiere que la imagen, el script y las rutas existan realmente.

## Siguiente sesión
Un proceso puede ejecutarse sin error y aun así guardar duplicados, nulos o formatos inconsistentes; por eso la calidad necesita tests independientes del estado de ejecución.

## Ejecución
Copia los YAML solucionados sobre sus versiones `starter/ejercicio1` y `starter/ejercicio2`; desde esas carpetas ejecuta `bash ../subir_a_kestra.sh flow_ingesta.yml ingesta_inestable.py` o `bash ../subir_a_kestra.sh flow_clima.yml ingesta_clima.py`. Verifica la interfaz, dispara ejecuciones y crea el backfill de los lunes.
