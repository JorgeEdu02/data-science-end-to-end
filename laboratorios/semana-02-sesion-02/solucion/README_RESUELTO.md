# Semana 2, sesión 2 — Viabilidad y riesgos

## Lectura
**ORA Score:** bajo el supuesto simplificado de combinar probabilidades, P(éxito) = P(éxito técnico) × P(éxito comercial). Si cualquiera es cercana a cero, el proyecto es inviable en conjunto. Un modelo excelente pero jamás utilizado no genera valor.

## Ejercicio 1: filtro de spam
**Predicción:** spam o legítimo por mensaje; datos históricos etiquetados, metadatos y contenido permitidos por la política del servicio.
**Acción:** clasificar el correo en bandeja o spam, ofreciendo restauración por el usuario.
**Juicio:** el usuario puede corregir falsos positivos y negativos.
**Resultado:** caída de spam en bandeja conservando una tasa de falsos positivos aceptable.
**Riesgo 1:** spammers cambian sus tácticas, invalida el supuesto de distribución estable. Verificar drift y recall por semana.
**Riesgo 2:** etiquetas erróneas, invalida el supuesto de calidad de labels. Auditar muestras y usar feedback.

## Ejercicio 2: recomendaciones odontológicas
**Predicción:** probabilidad de conveniencia de cada tratamiento, con datos clínicos autorizados; es una herramienta de apoyo, no un diagnóstico automático.
**Datos difíciles:** historiales estandarizados entre clínicas, registro de resultados y acceso compatible con privacidad.
**Acción:** proponer opciones; **juicio:** odontólogo decide. **Resultado:** tasa de tratamientos adecuados y seguimiento de resultados clínicos.
**Riesgo 1:** entrenar en una sucursal no generaliza a otras; validación externa por sede.
**Riesgo 2:** automatización complaciente del juicio clínico; registrar revisiones y errores.

**Watson vs Stitch Fix:** la generalización clínica sin validación externa se parece más al problema discutido de Watson. Stitch Fix integra criterio humano de estilistas, inventario y logística. En las diapositivas, la opción correcta del contraste es **B**.

## Ejercicio 3 — Canvas ilustrativo (valoraciones de futbolistas)
1. **Problema y usuario:** analistas de scouting quieren estimar cambios futuros de valoración y priorizar jugadores a revisar.
2. **Predicción:** valor de mercado en una fecha futura definida.
3. **Datos:** valores pasados, rendimiento, edad, club, liga y posición; verificar disponibilidad efectiva y cobertura temporal de cada fuente, sin afirmar acceso donde aún no se probó.
4. **Acción:** priorizar jugadores para análisis y negociación.
5. **Juicio:** analista deportivo valida la predicción antes de decidir.
6. **Resultado:** reducción de error frente a baselines y utilidad en decisiones documentadas.
7. **Riesgos:** (a) datos posteriores al corte / leakage; verificar auditoría temporal de joins; severidad alta. (b) cambios de liga y mercado / drift; evaluar por temporada y liga; severidad alta. (c) valor publicado no refleja precio de traspaso efectivo; validar definición de target; severidad alta.

**Premortem propuesto:** el sistema falla al tomar información de la temporada futura como feature, inflando el MAE offline. Este es un escenario ilustrativo, no una conversación real con un compañero.

**Pregunta para compañero propuesta:** ¿cómo verificas que tu variable objetivo tiene la misma definición y escala en todas las fuentes?

La retroalimentación real de un compañero y una votación de clase no se pueden inventar.

## Pregunta final
Un notebook falla en otra máquina por diferencias de Python, paquetes, binarios del sistema, rutas y configuraciones; Docker fija el entorno reproducible.
