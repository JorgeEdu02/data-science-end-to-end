# Semana 6, sesión 1 — Batch con Spark

## Teoría
Batch procesa conjuntos acumulados en corridas discretas; streaming procesa eventos cercanos a su llegada. Spark particiona y distribuye trabajo, superando un único proceso pandas cuando los datos crecen (aunque algunas operaciones siguen requiriendo memoria y coordinación). Transformaciones como `filter` y `groupBy` son *lazy*; acciones como `count`, `show` o `write` ejecutan el plan.

## Ejercicio 1
En `solucion/ejercicio1_spark.py`, la primera acción que materializa el filtro es `electronica.count()`. `groupBy("categoria").agg(...)` equivale a un `GROUP BY` SQL. Spark escribe una carpeta con archivos `part-*.csv` y `_SUCCESS`, no un solo archivo como pandas. El resultado de hogar `215.23000000000002` es la aproximación de números flotantes binarios, también posible en pandas; redondear para reportar, o usar Decimal para cálculos financieros.

## Ejercicio 2
Se filtra `estado=="entregado"` antes de calcular `peso_kg * tarifa_por_kg`; después se agrupa por ciudad. Datos del CSV: 14 envíos, 10 entregados y 4 excluidos. Costos de entregados por ciudad: **Quito 22,75**, **Guayaquil 49**, **Cuenca 26**, total **97,75** en las unidades del dataset. Por lo tanto, Guayaquil tiene el mayor total. Compara con pandas para verificar una muestra pequeña, pero no recopiles a pandas el histórico enorme que no cabe en RAM.

**Nota:** los totales se calcularon a partir de las filas del CSV del profesor, no de una ejecución Spark verificada en este entorno.

## Ejercicio 3
Se necesita el dataset procesado de futbol para implementar una misma transformación (por ejemplo, suma o media de valoración por temporada/posición) en pandas y Spark y contrastar resultados. Para grandes datos, usar almacenamiento distribuido y evitar `toPandas()` sobre todo el histórico.

Desde `starter`:
```bash
python ../solucion/ejercicio1_spark.py
python ../solucion/ejercicio2_envios.py
```
