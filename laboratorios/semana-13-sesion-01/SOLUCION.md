# Semana 13, sesion 1: respuestas del laboratorio

## Antes de empezar

**Gobernanza de modelos (IBM):** politicas, inventario, documentacion, validacion y gestion de riesgos durante todo el ciclo de vida; permite rastrear responsables, cambios y decisiones.

**Inventario:** nombre, proposito, propietario, datos y metodo de entrenamiento, versiones, metricas, validaciones, riesgos y estado de despliegue. Permite reproducir una decision sin haber entrenado el modelo.

Fuente: https://www.ibm.com/think/topics/model-governance

## Apertura

Un archivo sobrescrito no permite identificar que version hizo una prediccion historica. El registro conserva cada version y sus metricas; el alias produccion selecciona la version aprobada. Cada respuesta incluye version_modelo.

## Ejercicio 1

1. **Antes de TODO:** registrar imprime Version None y no crea versiones. Versiones no lista nada; promover lanza una excepcion por modelo o alias ausente. No hay version disponible para asignar a produccion.
2. **TODO 1:** dos registros desde cero generan versiones 1 y 2; la primera no se borra al registrar la segunda.
3. **TODO 2/3:** el servicio arrancado con alias en v2 responde v2. Mover el alias a v1 sin reiniciar no cambia su modelo cargado: sigue v2. Despues de reiniciar responde v1.
4. **TODO 4:** falla test_cada_prediccion_dice_que_version_la_calculo antes del cambio. Prueba que cada respuesta identifica la version, no solo la pagina /salud.
5. **Tarifas reales:** anotar la salida de /predecir con el viaje Midtown a JFK para cada version al ejecutarlas. El enunciado no provee esas dos predicciones, asi que no se inventan.

## ConcepTest

El README no trae las opciones A-D. Idea esencial: mover el alias no cambia automaticamente un modelo ya cargado en memoria; se necesita recarga o redeploy. El voto debe elegirse con las alternativas reales de clase.

## Ejercicio 2

1. En un registro inicialmente vacio se espera **version 2 (gradient boosting)** en produccion: mejora el recall respecto a la primera; la tercera no la supera.
2. La logistica muy regularizada puede tener mayor precision, pero menor recall. Se rechaza porque la regla exige mejorar el recall. Si los falsos positivos son mas caros, evaluar precision o costo esperado total antes de aprobar.
3. En MLflow, Models > fraude-pagos > version 3: etiquetas validacion=rechazada y comparada_con=2, mas las metricas guardadas en la corrida.
4. Una segunda corrida desde cero registra seis versiones. Como datos y semillas son iguales y la regla exige un recall **estrictamente** mayor, la version 2 permanece en produccion.

## Ejercicio 3

Hay una implementacion demostrativa en psets/proyecto/ usando el problema de taxis. Ver README-semana13.md y docs/despliegue.md. La promocion exige MAE menor; las decisiones se etiquetan en MLflow. El contenedor usa el modelo y el numero de version exportados, sin consultar el registro.

## Proxima sesion

Un modelo puede responder rapido y mal. Se necesita comparar predicciones con verdad y vigilar cambios en entradas y salidas, no solo salud y latencia.
