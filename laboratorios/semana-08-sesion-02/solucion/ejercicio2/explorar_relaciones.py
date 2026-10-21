from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
FIG = BASE / "figuras"
FIG.mkdir(exist_ok=True)
viajes = pd.read_csv(BASE.parents[1] / "starter" / "viajes_taxi.csv")
# TODO 1: quitar solo errores confirmados
limpios = viajes[(viajes.tarifa != 999.99) & (viajes.duracion_min >= 0)].copy()
print(f"Filas originales: {len(viajes)}; limpias: {len(limpios)}")
# TODO 2: distancia vs tarifa
plt.figure(figsize=(9,6))
plt.scatter(limpios.distancia_km, limpios.tarifa, s=10, alpha=.35)
plt.xlabel("Distancia (km)"); plt.ylabel("Tarifa"); plt.title("Distancia vs tarifa")
plt.tight_layout(); plt.savefig(FIG/"distancia_vs_tarifa.png"); plt.close()
print("Distancia cero y tarifa positiva:", len(limpios[(limpios.distancia_km==0) & (limpios.tarifa>0)]))
print("Distancia positiva y tarifa cero:", len(limpios[(limpios.distancia_km>0) & (limpios.tarifa==0)]))
por_km=limpios.loc[limpios.distancia_km>0].copy()
por_km["tarifa_por_km"]=por_km.tarifa/por_km.distancia_km
print(por_km.nlargest(10,"tarifa_por_km")[["distancia_km","tarifa","tarifa_por_km"]].to_string(index=False))
# TODO 3: propinas por metodo
propinas=limpios.groupby("metodo_pago",dropna=False).agg(
    viajes=("tarifa","size"),
    propina_promedio=("propina","mean"),
    viajes_propina_cero=("propina",lambda s:(s==0).sum()),
    porcentaje_propina_cero=("propina",lambda s:100*(s==0).mean())
)
print("\nPropinas:\n",propinas.to_string())
# TODO 4: correlacion con tarifa
columnas=["distancia_km","duracion_min","pasajeros","propina","tarifa"]
print("\nCorrelaciones:\n",limpios[columnas].corr(numeric_only=True)["tarifa"].sort_values(ascending=False).to_string())
# TODO 5: pasajeros faltantes y cero
print("\nPasajeros faltantes:", limpios.pasajeros.isna().sum())
print("Pasajeros cero:", (limpios.pasajeros==0).sum())
