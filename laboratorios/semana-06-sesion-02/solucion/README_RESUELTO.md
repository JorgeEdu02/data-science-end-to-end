# Semana 6, sesión 2 — Streaming

## Inicio
Procesar eventos al llegar reduce latencia si la decisión caduca rápidamente. Aumenta complejidad por brokers, offsets, particiones, reintentos, duplicados y eventos tardíos.

## Ejercicio 1
El productor necesita publicar con `producer.send("pedidos", evento)`. `print` solo escribe en terminal. El consumidor debe usar `auto_offset_reset="earliest"` con un grupo nuevo o sin `group_id` para recuperar eventos previos; si inicia en latest, solo ve eventos futuros. `json.dumps(...).encode("utf-8")` se deshace mediante `json.loads(bytes.decode("utf-8"))`. Un segundo productor agrega 10 eventos: el topic retendrá 20 si no se reinicia el broker ni se configura retención que los borre. El consumidor resuelto cuenta por categoría.

## Ejercicio 2
Ocho lecturas: bodega 3, camara_fria 2, techo 3. Hay **2 alertas** de techo por 31,5 y 33,0 grados, ya que el umbral es mayor que 30. El consumidor imprime conforme consume el flujo, no al final. En operación continua, conviene quitar el timeout de 10 segundos o diseñar un servicio siempre activo. Consumidores de grupos distintos ven las mismas lecturas; consumidores del mismo grupo comparten particiones y procesamiento, con límites si hay una sola partición.

## Ejercicio 3 — Proyecto de futbol
**Decisión propuesta:** batch, no streaming, si la estimación de valor se actualiza por temporadas o semanas y esperar horas no elimina valor. El productor/consumidor de un streaming deportivo solo se justificaría si el objetivo fuera puntuar eventos de un partido en vivo.

## Ejecución
Copia scripts resueltos de `solucion/` sobre los `starter/` del laboratorio y levanta Redpanda desde `starter` con `docker compose up -d`. Ejecuta productor y consumidor. No se han verificado mensajes realmente publicados en Redpanda desde este entorno.
