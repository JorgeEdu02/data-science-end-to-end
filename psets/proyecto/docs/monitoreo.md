# Monitoreo de tarifas

La salud HTTP no revela si un modelo estima mal. Las alertas de esta tabla son **umbrales iniciales propuestos**, no umbrales validados en produccion.

| Metrica | Clase | Fuente | Cuando disponible | Alerta |
| --- | --- | --- | --- | --- |
| Peticiones | Sistema | Middleware | Inmediato | Caida abrupta respecto a referencia |
| Errores 422 | Sistema / entrada | Middleware | Inmediato | > 2% de solicitudes |
| Errores 5xx | Sistema | Middleware | Inmediato | Al menos uno |
| Latencia p50 | Sistema | Middleware | Inmediato | Tendencia anomala |
| Latencia p95 | Sistema | Middleware | Inmediato | > 100 ms |
| MAE semanal por version | Modelo | Predicciones unidas a cobros | Al terminar/conciliar el viaje | > 2x MAE de validacion |
| Tarifa media estimada | Modelo indirecta | JSONL | Inmediato | Cambio > 25%, investigar |

## Ejecucion

Desde psets/proyecto/, tras exportar un modelo:

~~~~bash
python -m monitoreo.simular_noviembre
python -m monitoreo.desempeno --verdad monitoreo/cobros.csv
~~~~

La simulacion crea predicciones.jsonl (id_prediccion, momento, version, entrada y tarifa_estimada) y cobros.csv (id_prediccion, tarifa_cobrada). El MAE compara registros unidos por ese identificador, agrupados por semana y version.

Si aun no hay verdad:

~~~~bash
python -m monitoreo.desempeno
~~~~

Solo reporta cantidad de predicciones y tarifa media estimada: indicadores indirectos que **no prueban** la exactitud. En el caso simulado, la verdad llega al terminar el viaje y registrar el cobro. Un error en la relacion distancia/zona/tarifa puede aumentar MAE sin aumentar latencia ni errores 500.

## Limitaciones

Las metricas en memoria desaparecen al reiniciar el proceso. JSONL y su candado son adecuados para la demostracion de un solo proceso; con multiples instancias se debe usar una base de datos o cola persistente. Proteger los registros y definir retencion porque contienen los campos de la solicitud.
