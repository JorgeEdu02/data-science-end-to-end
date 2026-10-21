from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
CSV = BASE.parents[1] / "starter" / "viajes_taxi.csv"
FIG = BASE / "figuras"
FIG.mkdir(exist_ok=True)
viajes = pd.read_csv(CSV)
print("DIMENSIONES:", viajes.shape)
print("\nTIPOS:\n", viajes.dtypes)
print("\nFALTANTES:\n", viajes.isna().sum())
print("\nRESUMEN:\n", viajes.describe(include="all").to_string())
print("\nTARIFA 999.99:", (viajes.tarifa == 999.99).sum())
print("DURACION NEGATIVA:", (viajes.duracion_min < 0).sum())
q1, q3 = viajes.tarifa.quantile([0.25, 0.75])
iqr = q3-q1
li, ls = q1-1.5*iqr, q3+1.5*iqr
atipicos = viajes[(viajes.tarifa < li) | (viajes.tarifa > ls)]
print(f"Q1={q1:.4f}; Q3={q3:.4f}; IQR={iqr:.4f}")
print(f"Limites: {li:.4f}, {ls:.4f}; atipicos={len(atipicos)}")
print(atipicos.head(20).to_string(index=False))
plt.figure(figsize=(9,5))
plt.hist(viajes.tarifa.dropna(), bins=45)
plt.xlabel("Tarifa"); plt.ylabel("Viajes"); plt.title("Tarifa antes de limpiar")
plt.tight_layout(); plt.savefig(FIG/"distribucion_tarifa_cruda.png"); plt.close()
plt.figure(figsize=(9,3))
plt.boxplot(viajes.tarifa.dropna(), vert=False)
plt.xlabel("Tarifa"); plt.title("Atipicos")
plt.tight_layout(); plt.savefig(FIG/"boxplot_tarifa_cruda.png"); plt.close()
limpios = viajes[(viajes.tarifa != 999.99) & (viajes.duracion_min >= 0)].copy()
print("FILAS LIMPIAS:", len(limpios))
plt.figure(figsize=(9,5))
plt.hist(limpios.tarifa.dropna(), bins=45)
plt.xlabel("Tarifa"); plt.ylabel("Viajes"); plt.title("Tarifa despues de limpiar")
plt.tight_layout(); plt.savefig(FIG/"distribucion_tarifa_limpia.png"); plt.close()
