# Modelado dbt: soluciones de ejercicios 1 y 2

Para ejecutar los proyectos dbt, conserva los archivos de configuracion y datos de la carpeta `starter/ejercicio1` o `starter/ejercicio2` y **copia los modelos solucionados sobre sus correspondientes archivos `models/`** en ese proyecto. Desde la carpeta starter/ejercicioN:

```bash
python cargar_raw.py
dbt run --profiles-dir .
dbt test --profiles-dir .
```

El ejercicio 2 corrige un duplicado exacto de `id_venta=4` en staging mediante `SELECT DISTINCT`, conservando los datos raw sin alterarlos. `stg_ventas` debe tener 12 filas y 12 IDs unicos frente a 13 filas raw. Despues `python comprobar.py` debe validar las 5 condiciones.

Ejercicio 3 depende del esquema, tablas y fuente reales de tu proyecto. No se deben inventar resultados de `dbt run` o `dbt test`.
