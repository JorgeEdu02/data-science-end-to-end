# Semana 1, sesión 2 — Ciclo de vida de un proyecto de ciencia de datos

## Antes de empezar
En software convencional el programador escribe reglas y pruebas sobre comportamientos relativamente determinados; en ML el sistema aprende patrones de datos y exige recolectar, etiquetar, entrenar, evaluar y monitorear las distribuciones de entrada. Una etapa distintiva es entrenar y validar estadísticamente el modelo con ejemplos representativos, no solo ejecutar lógica escrita a mano.

## Las siete fases
1. **Formular:** definir predicción, beneficiario, costo del error y métricas de negocio.
2. **Datos:** identificar fuentes, etiquetas, calidad, sesgos y disponibilidad.
3. **Features:** transformar datos en variables disponibles al momento de predecir.
4. **Modelo:** elegir línea base y alternativas; entrenar y validar sin leakage.
5. **Desplegar:** integrar predicción con una decisión operativa real.
6. **Monitorear:** vigilar drift, desempeño, fallos y resultado de negocio.
7. **Comunicar:** informar supuestos, métricas, riesgos y límites a usuarios.
Iteración: si monitoreo detecta drift, se retorna a datos, features y reentrenamiento; si la métrica no corresponde a valor real, se vuelve a formular.

## Ejercicio 1: filtro de spam
- **Datos y etiquetas:** correos históricos y etiquetas de usuario/administrador, con separación temporal de entrenamiento y prueba.
- **Fase subestimada:** monitoreo: los emisores modifican el contenido para evadir filtros.
- **Mapa de siete fases:** formular minimizar spam y correos legítimos bloqueados; datos reunir mensajes etiquetados; features extraer términos, remitente y enlaces; modelo comparar clasificador simple contra otro con precision/recall; desplegar al recibir correos; monitorear falsos positivos, falsos negativos y drift; comunicar desempeño y política de revisión de spam.

## Ejercicio 2: Zillow Offers
El hecho de que el sistema escalara no demuestra que el modelo y el negocio fueran robustos ante cambios de mercado. Según los datos del enunciado, el anuncio de cierre fue el 2 de noviembre de 2021, con 304 millones USD de pérdida trimestral, 9.680 casas compradas en ese trimestre mencionadas por el caso y 2.000 despidos. Se atribuye como **hipótesis principal de la discusión**, no hecho aislado demostrado, una insuficiente detección o control del riesgo de mercado en monitoreo y toma de decisiones. El diseño del negocio y sus límites de riesgo también son críticos.

Mapa: formular margen de compra-reventa; datos transacciones, condiciones y tendencias inmobiliarias; features ubicación, estado y temporalidad; modelo estimaciones del precio futuro; despliegue compra basada en estimación y reglas; monitoreo exposición a inventario y desviaciones entre oferta y precio de reventa; comunicar incertidumbre, exposición y pérdidas. El material no permite atribuir una causa técnica única con certeza.

## Ejercicio 3: tres casos con evidencia
**Amazon (caso A):** los datos históricos de 10 años con mayoría masculina sesgaron el entrenamiento; en 2015 se identificaron penalizaciones de términos como *women's*; la causa documentada se relaciona con datos y evaluación de equidad. La empresa disolvió el equipo a inicios de 2017. Mitigación: auditoría de proxies, evaluación por subgrupo, corrección y monitoreo antes de uso real.

**Google Flu Trends (caso B):** no detectó la pandemia de H1N1 en 2009, sobreestimó más del 50% en 2011-2012 y reportó cifras mayores que las reales en 100 de 108 semanas entre agosto de 2011 y septiembre de 2013. Cambios del buscador en 2011-2012 alteraron la fuente de datos. Se requieren validación temporal, monitoreo de drift y comparación frente al baseline de los CDC.

**Epic Sepsis (caso C):** validación externa en 38.455 hospitalizaciones (2018-2019) mostró AUC 0,63, sensibilidad 33% y alertas para 18% de pacientes, frente al AUC reportado de 0,76-0,83. Problema de generalización y evaluación externa antes de desplegar; no se debe asumir que el resultado del proveedor se reproduce en cada hospital.

**ConcepTest:** las alternativas A-D no aparecen en el README; no es posible reconstruir una votación real ni discusión con un compañero.

## Pregunta final
Desde el principio deben definirse límites de exposición, señales de degradación, métricas de margen realmente realizado, revisiones de riesgo, alertas y reglas de suspensión o reducción de compras, no solo una métrica offline de predicción.
