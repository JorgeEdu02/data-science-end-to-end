# Semana 2, sesión 1 — Problemas de negocio y métricas

## Lectura
Antes de elegir ML: describir la decisión de negocio, definir qué se predice, comprobar los datos y etiquetas, identificar quién actuará, definir línea base, costo de errores, métrica y umbral. Una heurística simple es preferible cuando basta para resolver el problema con menor costo, mayor transparencia y menos mantenimiento.

## Ejercicio 1: plataforma de streaming
**Predicción:** probabilidad de que una suscripción activa se cancele en los próximos 30 días.
**Datos:** historial de uso, pagos, antigüedad, interacciones y cancelaciones pasadas, observados antes del instante de predicción.
**Métrica del modelo:** PR-AUC, recall entre clientes contactados y calibración.
**Métrica de negocio:** reducir la tasa de cancelación al menos 15% frente a grupo control, neta del costo de los incentivos.
**Acción:** contactar al usuario si P(cancelación) >= 0,70 como umbral inicial para pilotaje; calibrar según costo y capacidad.
**Si el umbral baja a 0,30:** por definición se contacta a tantos o más usuarios; sin distribución de probabilidades no se puede calcular cuántos más. El costo de retención normalmente aumenta.

## Ejercicio 2: abandono universitario
**Dato adicional:** historial académico, asistencia, situación de matrícula y etiqueta clara de abandono; se deben proteger datos personales y limitar el acceso.
**Predicción:** probabilidad de no matricularse el siguiente semestre.
**Métrica:** tasa de rematriculación 20% mayor respecto de un grupo comparable o control, junto a equidad de la intervención.
**Acción:** oferta de tutoría si P(abandono) >= 0,60 (umbral orientativo de la guía).
**Umbral 0,90:** estudiantes con riesgo entre 0,60 y 0,90 quedarían sin atención pese a poder beneficiarse; aumenta la posibilidad de falsos negativos.

## Ejercicio 3 — Ejemplo para el proyecto de valor de futbolistas
**Predicción propuesta:** valor de mercado futuro del jugador para una fecha de corte definida, o variación del valor respecto del periodo previo. Se debe elegir una definición, no mezclarlas.
**Datos:** historial de valoraciones, edad, minutos, posición, rendimiento, liga, club y fecha, todas disponibles antes del corte. No utilizar el valor futuro como feature.
**Métrica técnica:** MAE en escala monetaria con validación temporal, comparado con persistencia del último valor.
**Métrica de negocio:** reducción de error de estimaciones utilizado en evaluación deportiva versus baseline.
**Umbral operativo:** revisión manual si la variación esperada excede 20% y el modelo supera un nivel de confianza definido por validación. El 20% es una propuesta, no un umbral ya validado.
**Errores más costosos:** sobrevalorar un fichaje puede generar pérdidas; subvalorar podría hacer perder una oportunidad.

ConcepTest: el README omite opciones y no permite verificar votos personales.

## Pregunta final
La viabilidad requiere demostrar acceso a datos con calidad, etiquetas históricas, un usuario que cambie una decisión, valor operativo medible y condiciones de implementación aceptables.
