# Ejecucion de productor y consumidor

Desde la carpeta original `starter`, copia los scripts terminados de `solucion` para sustituir los TODO y levanta Redpanda con `docker compose up -d`. Inicia el productor y despues el consumidor.

El consumidor usa `auto_offset_reset="earliest"` y `group_id=None` para leer desde el principio en cada corrida. El topico persiste eventos entre ejecuciones: si publicas dos veces, veras 20 pedidos u 16 lecturas, no 10 u 8. No se ha ejecutado Redpanda en este entorno.

Para el proyecto de futbol, el procesamiento batch es suficiente cuando los datos se actualizan semanal o diariamente y las decisiones no caducan en segundos. Streaming se justificaria para eventos en vivo, no para valoraciones historicas.
