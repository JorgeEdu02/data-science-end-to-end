# Semana 5, sesión 1 — Warehouse y lake

## Antes de empezar
Un warehouse sirve datos estructurados, consultas SQL repetidas y dashboards; un lake permite almacenar formatos crudos y variados para exploración posterior. Finanzas con columnas estables: warehouse; imágenes, logs y clics exploratorios de ML: lake.

## Ejercicio 1
`solucion/ejercicio1_warehouse.py` crea tabla `pedidos`, cuenta filas y agrega `SUM(cantidad * precio_unitario)` por categoría. `JOIN` con `clientes` por `id_cliente` permite total por ciudad. `SHOW TABLES` puede estar vacío mientras una consulta usa `read_csv_auto()` directamente: eso NO significa que el archivo sea una tabla persistida. Cambiar el CSV no actualiza automáticamente una tabla ya materializada; hay que recargarla o crear otro proceso. Agrupar convierte los 10 pedidos en tantas filas como categorías distintas.

## Ejercicio 2
`solucion/ejercicio2_ventas.py` carga `ventas` y `productos`, agrega unidades, realiza join y cuenta ventas sin correspondencia. El producto `P9` no está en `productos.csv`: con `INNER JOIN` esa venta queda excluida sin error. Para descubrirlo, comparar cantidad de filas antes/después y ejecutar anti-join o left join buscando `NULL` en el lado derecho. `LEFT JOIN` conserva esa venta y asigna `NULL` a categoría y precio hasta investigar.

## Ejercicio 3 — Proyecto propio
El CSV del proyecto debe cargarse con `CREATE TABLE ... AS SELECT * FROM read_csv_auto(...)`, comparar los conteos y agregar por categoría relevante como liga o posición. Se debe verificar la definición temporal de la valoración antes de usarla en reportes. El resultado numérico no está disponible sin el CSV real.

Para correr los ejercicios 1 y 2 desde `starter`:
```bash
python ../solucion/ejercicio1_warehouse.py
python ../solucion/ejercicio2_ventas.py
```
Estos scripts utilizan archivos CSV relativos al directorio actual.

## ConcepTest
Una tabla o un join que ejecutan correctamente no garantizan integridad referencial ni completitud del resultado.
