# Semana 7, sesión 1 — Laboratorio integrador

La sesión **no introduce ejercicios aislados nuevos**: requiere una integración real con el dataset de tu proyecto. No es válido marcar tareas con check sin haberlas ejecutado.

## Cadena a verificar
1. Docker: imagen de tu script con dependencias, volumen para persistir datos y comparar salida con ejecución local.
2. Infraestructura: servicios de almacenamiento accesibles mediante nombres de red y volumen persistente.
3. Orquestación: flow Kestra usa la imagen correcta y tiene reintentos y una programación justificada.
4. Calidad: archivo *limpio* derivado del archivo crudo, con conteos y reglas documentadas.
5. Warehouse: carga de salida limpia y recuento idéntico.
6. dbt: staging, intermedia y marts conectados al mismo DuckDB, con `dbt debug/run/test` satisfactorios.
7. Batch: Spark lee la misma fuente limpia y produce agregaciones equivalentes a pandas o dbt.
8. Streaming opcional: justificar necesidad antes de montarlo; un proyecto de valoraciones históricas normalmente puede operar batch.

## Evidencia que falta capturar en Codespaces
Logs y códigos de salida de `docker build`, `docker run`, `docker compose up`, ejecuciones de Kestra, `dbt run/test`, conteo en DuckDB y resultados de Spark. No se han marcado como completados esos pasos ni se han inventado métricas.

## Pregunta sobre contratos
Un contrato de datos debe especificar nombres, tipos, significado, claves, unidad, valores válidos, propietario, compatibilidad y políticas de cambio. Una prueba de dbt detecta ciertos incumplimientos en un momento, pero no reemplaza el acuerdo explícito de productores y consumidores.

**Entrega de esta sesión:** el pipeline y evidencias de ejecución del proyecto propio, que todavía requieren el acceso y la ejecución de ese entorno.
