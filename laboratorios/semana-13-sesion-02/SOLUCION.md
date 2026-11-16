# Semana 13, sesion 2: respuestas del laboratorio

## Antes de empezar

Un servicio HTTP sano no implica un modelo preciso. Ademas de disponibilidad y latencia hay que vigilar MAE/recall/precision y los indicadores de cambio de distribucion. Si la verdad llega tarde, se pueden seguir data drift, prediction drift y tasa de alertas; son indicadores indirectos, no prueba de calidad.

Fuente: https://www.datadoghq.com/blog/ml-model-monitoring-in-production-best-practices/

## Apertura

Hay que cruzar la estimacion con el resultado real mediante id_prediccion, calcular la metrica de modelo por semana y version y vigilar indicadores indirectos en el intermedio.

## Ejercicio 1

1. Antes de los TODO, 1156 viajes obtienen tarifa, /metricas responde un diccionario vacio y desempeno.py se detiene por falta del registro. No se puede concluir que las tarifas fueron buenas.
2. Se esperan **3 respuestas 422** de solicitudes invalidas y cero errores de servidor. La latencia p95 se mide en la maquina, no puede adivinarse; no deberia crecer sistematicamente entre semanas por un cambio en el MAE.
3. id_prediccion es la clave para unir cobro y prediccion. Fecha y tarifa no son identificadores unicos: pueden existir viajes repetidos.
4. El MAE de prueba v1 fue **1.17 USD**. Las primeras semanas deberian acercarse a la referencia y a partir del 16-11-2026 se espera aumento. Los valores exactos deben obtenerse al entrenar y simular.
5. Para anotar p95, errores y MAEs exactos, ejecutar entrenar.py, simular_noviembre.py y desempeno.py en el entorno del curso.

## ConcepTest

El README no incluye opciones A-D. Idea: la salud del sistema no demuestra la calidad del modelo; una variacion indirecta tampoco demuestra por si misma una caida de recall.

## Ejercicio 2: datos calculados desde el CSV de 5874 pagos

La fecha HOY del script es **2026-12-14** (fecha de corte simulada).

| Semana | Pagos | Tasa de revision | Recall maduro |
| --- | ---: | ---: | ---: |
| 2026-11-02 | 1487 | 0.0706 | 0.767 |
| 2026-11-09 | 1490 | 0.0685 | 0.736 |
| 2026-11-16 | 1471 | 0.0503 | 0.276 |
| 2026-11-23 | 1426 | 0.0456 | No disponible |

Latencia p95 maxima: **78.2 ms**, el **2026-11-10**.

1. Alertas: **sistema** por latencia del 10-11; **modelo indirecta** por bajas tasas de revision de las semanas 16 y 23; **modelo** por recall bajo de la semana 16. La latencia alta no coincide con la semana de recall bajo.
2. Primera senal en la semana del **16-11** (tasa de revision 0.0503). El recall se conoce de modo completo para esa semana desde el **13-12**. Una tasa menor no prueba menor recall: puede variar la prevalencia de fraude.
3. La semana del **23-11** termina el 29-11; con demora maxima de 21 dias madura el **20-12**. Confirmar algunos fraudes antes no da un denominador completo.
4. Si HOY es **2026-11-30**, solo tiene recall maduro la semana del 02-11. La semana 09 madura el 06-12, la del 16 el 13-12.

## Ejercicio 3

Se implemento un ejemplo completo en psets/proyecto/: middleware p50/p95 y codigos, JSONL con ID y version, union con verdad y MAE semanal por version, pruebas con tmp_path y documentacion. Ver docs/monitoreo.md.

La verdad llega al terminar el viaje y registrar el cobro. Mientras tanto se pueden observar cambios en tarifas medias y entradas, sin afirmar que equivalen a MAE. Una API con latencia baja puede equivocarse sistematicamente si cambia la relacion entre entrada y tarifa real.

## Proxima sesion

Cuando la distribucion de las entradas se mantiene pero el MAE empeora, se sospecha **concept drift**, no necesariamente data drift. Sin verdad no se detectaria mirando solo los viajes.
