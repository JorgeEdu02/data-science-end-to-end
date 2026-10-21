"""Configurar ruta y nombres reales de columnas del dataset de Semana 7."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE=Path(__file__).resolve().parent
FIG=BASE/"figuras"
FIG.mkdir(exist_ok=True)
RUTA_CSV=BASE/"datos_proyecto.csv"
OBJETIVO="perdio_valor"  # Cambiar por la columna real
VARIABLE="edad"  # Cambiar por el predictor real

datos=pd.read_csv(RUTA_CSV)
for nombre in (OBJETIVO,VARIABLE):
    if nombre not in datos.columns:
        raise ValueError(f"Falta {nombre}. Columnas: {datos.columns.tolist()}")
print("Filas y columnas:",datos.shape)
print("\nTipos:\n",datos.dtypes)
print("\nFaltantes:\n",datos.isna().sum())
print("\nResumen:\n",datos.describe(include="all").to_string())
y=pd.to_numeric(datos[OBJETIVO],errors="coerce")
plt.figure(figsize=(8,5))
plt.hist(y.dropna(),bins=40)
plt.title("Distribucion: "+OBJETIVO)
plt.tight_layout();plt.savefig(FIG/"distribucion_objetivo.png");plt.close()
q1,q3=y.quantile([.25,.75])
iqr=q3-q1
if y.dropna().nunique()<=2:
    print("\nObjetivo binario; conteos por clase:")
    print(datos[OBJETIVO].value_counts(dropna=False).to_string())
else:
    atipicos=datos.loc[(y<q1-1.5*iqr)|(y>q3+1.5*iqr)]
    print("\nAtipicos IQR:",len(atipicos))
    print(atipicos.head(10).to_string(index=False))
if pd.api.types.is_numeric_dtype(datos[VARIABLE]) and datos[VARIABLE].nunique()>12:
    plt.figure(figsize=(8,5))
    plt.scatter(datos[VARIABLE],y,alpha=.25,s=12)
    plt.xlabel(VARIABLE);plt.ylabel(OBJETIVO)
else:
    datos.groupby(VARIABLE,dropna=False)[OBJETIVO].mean().plot(kind="bar",figsize=(8,5))
    plt.ylabel("Promedio del objetivo");plt.xlabel(VARIABLE)
plt.tight_layout();plt.savefig(FIG/"relacion_objetivo_feature.png");plt.close()
print("\nObjetivo nulo:",datos[OBJETIVO].isna().sum())
print("\nResumen por variable:\n",datos.groupby(VARIABLE,dropna=False)[OBJETIVO].agg(["count","mean"]).to_string())
print("\nDuplicados:",datos.duplicated().sum())
print("\nCorrelaciones:\n",datos.select_dtypes("number").corr()[OBJETIVO].sort_values(ascending=False).to_string())
