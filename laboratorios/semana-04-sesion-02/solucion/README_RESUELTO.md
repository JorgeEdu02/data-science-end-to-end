# Semana 4, sesión 2 — Diagnóstico de calidad

## Inicio
Un modelo puede entrenar y mostrar métricas plausibles con duplicados, faltantes sistemáticos, fechas mal interpretadas y sesgos. **Validez de ejecución no equivale a validez de datos**. De un vistazo, la consistencia semántica y los mecanismos de ausencia son difíciles de detectar.

## Ejercicio 1 — Sensores
El archivo tiene 10 filas; 2 filas duplicadas exactas, por lo que quedan 8. `isna()` detecta una temperatura realmente vacía, pero `N/D` se convierte en NaN adicional al ejecutar `pd.to_numeric(..., errors="coerce")`: quedan 2 temperaturas faltantes. Las fechas `01/02/2026` y `03/02/2026` se deben leer explícitamente como día/mes/año, no inferir libremente. La función resuelta usa `%d/%m/%Y` o `%Y-%m-%d` según separador.

## Ejercicio 2 — Pedidos
El archivo de 13 registros contiene 2 duplicados exactos (queda en 11), el campo `cantidad` tiene 2 valores ausentes y `monto` presenta dos indicadores textuales de ausencia, `sin dato` y `-`, que pasan a NaN con `errors="coerce"`. `pedido_id=P07` conserva dos registros distintos: no se elimina automáticamente porque quizá sean correcciones, modificaciones o un error de captura. La columna `cantidad` es flotante cuando incluye NaN, aunque los enteros que sí aparecen no tengan decimales, ya que el esquema numérico ordinario de pandas representa esos faltantes con float.

Las verificaciones de `comprobar` del Ejercicio 2 deberían dar 5 `OK` al ejecutar desde `starter` copiando `solucion/ejercicio2_pedidos.py`. No se ejecutó el script aquí.

## Ejercicio 3 — Diagnóstico del dataset propio
Se necesita el CSV realmente generado por el pipeline del proyecto. Pasos: (1) `duplicated()`, `isna().sum()`, `dtypes`; (2) inspección de valores únicos y conversiones verificadas; (3) documentar severidad, evidencia y estrategia de remediación antes de limpiar. Para valoraciones de futbolistas, comprobar fecha, jugador-valoración únicos, unidades monetarias, duplicados de temporadas y faltantes dependientes de liga.

## ConcepTest
Si un sensor se apaga con temperaturas extremas, la ausencia es MNAR; eliminar o imputar la media introduce sesgo. Primero investigar el mecanismo de ausencia. No reconstruir votos personales sin las opciones.

## Próxima sesión
La utilidad predictiva de una variable se contrasta con una línea base y validación, respetando disponibilidad temporal y evitando leakage.
