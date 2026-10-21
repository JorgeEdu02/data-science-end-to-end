# Resolución del laboratorio — Semana 8, sesión 2

Se mantienen intactas las plantillas originales. Esta carpeta contiene la resolución de los ejercicios 1 y 2 y un script adaptable al dataset propio del ejercicio 3.

## Ejecución

Desde la raíz del repositorio:

```bash
python -m pip install pandas matplotlib
python laboratorios/semana-08-sesion-02/solucion/ejercicio1/explorar_taxis.py
python laboratorios/semana-08-sesion-02/solucion/ejercicio2/explorar_relaciones.py
```

Los scripts leen directamente `starter/viajes_taxi.csv` del laboratorio y generan figuras en subcarpetas `figuras/`.

## Antes de empezar

**¿Qué responde el EDA?** Distribución de variables, faltantes, valores atípicos, errores de registro y relaciones que podrían afectar el modelado.

**Univariado vs. bivariado.** Para una variable: `describe()`, histogramas, conteos y boxplots. Para relaciones: gráficos de dispersión, agrupaciones y correlaciones según los tipos de datos.

**Pregunta de apertura.** Quince tarifas erróneas de 999.99 pueden sesgar promedios, MSE y el ajuste del modelo. No se detectan necesariamente mirando solo la predicción final.

## Ejercicio 1

**Respuesta 1:** El máximo de tarifa (999.99) y el mínimo negativo de duración permiten sospechar errores.

**Respuesta 2:** No todos los atípicos IQR son errores: deben investigarse individualmente antes de descartarlos. Tarifas fijas o trayectos largos pueden ser legítimos.

**Resultados sobre el CSV original:**
- 3000 registros, 10 columnas.
- 15 tarifas de 999.99 y 10 duraciones negativas.
- Q1 de tarifa = 13.99, Q3 = 32.5525, IQR = 18.5625.
- Límites IQR = -13.85375 y 60.39625; 334 observaciones fuera de límites.
- Tras retirar únicamente los 25 errores confirmados, quedan 2975 registros.

**ConcepTest:** El README original no incluye el enunciado ni las opciones A/B/C/D, por lo que no se puede justificar un voto específico.

## Ejercicio 2

**Hallazgo 1:** Distancia y tarifa tienen correlación de Pearson 0.9602; aun así, hay 25 recorridos con distancia cero y tarifa positiva. Deben investigarse.

**Hallazgo 2:** Los 888 registros de pago en efectivo tienen propina registrada en cero (media 0). En los 2027 pagos por tarjeta la propina media registrada es 4.7288 y no hay ceros. Los 60 registros sin método de pago tienen media 3.3507 y 16 propinas cero. Esto puede reflejar cómo se registran las propinas, no necesariamente cuánto dan los pasajeros.

**Hallazgo 3:** La duración real se correlaciona fuertemente con la tarifa (0.9559), pero si la predicción ocurre al solicitar el taxi, esa duración no está disponible. Usarla produciría fuga temporal (data leakage). Puede emplearse una *duración estimada* disponible antes del viaje.

**Otros resultados:** Correlaciones con tarifa: propina 0.6329 y pasajeros -0.0511. Tras limpiar, hay 119 valores faltantes de pasajeros y 19 registros con cero pasajeros.

## Ejercicio 3 — proyecto propio

`ejercicio3/explorar_proyecto.py` es una plantilla desarrollada, **no un análisis ya realizado del proyecto propio**. Se debe reemplazar la ruta `datos_proyecto.csv` por el dataset de la semana 7 y configurar los nombres reales de `OBJETIVO` y `VARIABLE`.

En un proyecto de predicción de pérdida de valor de futbolistas, conviene comprobar con números: (1) faltantes en variables clave, (2) posible desbalance de clases, y (3) variables obtenidas después de la fecha de predicción que ocasionen leakage. No se presentan cifras sin disponer de ese dataset.

## Antes de la próxima sesión

Una característica `es_ruta_jfk` puede derivarse del origen/destino, y `hora_inicio` de la fecha/hora. Ambos deben estar disponibles al momento de la predicción; la hora puede codificarse cíclicamente con seno/coseno.
