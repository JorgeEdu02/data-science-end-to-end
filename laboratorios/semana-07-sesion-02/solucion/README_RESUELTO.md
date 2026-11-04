# Semana 7, sesión 2 — Repaso y contrato de datos

Esta sesión está diseñada para **preguntas propias** y discusión; no tiene ejercicios de código y las respuestas personales no deben atribuirse a una conversación real.

## Preguntas de repaso propuestas con respuesta
- **Formulación:** ¿por qué una mejora de MAE no implica mejor negocio? Porque la decisión, el costo del error y el retorno pueden no cambiar.
- **Docker e IaC:** ¿por qué `depends_on` no basta? Porque arranque del proceso no significa que el servicio esté listo para conexiones; usar healthcheck o retry.
- **Kestra y calidad:** ¿por qué un flow exitoso puede producir datos malos? La ejecución no comprueba automáticamente duplicados, validez o consistencia.
- **Warehouse/dbt:** ¿por qué usar `ref()`? Registra dependencias entre modelos, ordena ejecución y centraliza transformaciones probadas.
- **Spark y streaming:** ¿cuándo sirve cada uno? Batch para resultados tolerantes a latencia; streaming cuando cada evento debe procesarse pronto.
- **Integración:** ¿cómo detectar una etapa que lee un CSV distinto? Documentar rutas y comparar recuentos, hash o claves y versiones por etapa.

## Contrato de datos
A diferencia de un diccionario informal de columnas, un **contrato** establece compromisos explícitos entre productor y consumidor sobre esquema, semántica, calidad, cambios y responsabilidad. Un `unique` o `not_null` de dbt solo cubre una restricción: no garantiza por sí mismo notificación ni acuerdo frente a cambios de fuente.

**Ejemplo para futbol:** `valuation_date` es la fecha de vigencia de una valoración y debe expresarse en un huso/convención establecido; `market_value_eur` significa euros nominales de la fecha, no precio pagado en una transferencia. La elección real del nombre debe revisarse contra las tablas del proyecto.

No se inventó una pregunta o voto de un compañero, ni el texto de una discusión no compartida.
