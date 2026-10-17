import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

GRIS = "#B9C3D1"
AZUL = "#1C4C9A"
ROJO = "#B2182B"
NARANJA = "#D1C9B9"

sns.set_theme(style="whitegrid")

df = pd.read_csv("coin_Bitcoin.csv")
#Conversion de valor de fecha
df["Date"] = pd.to_datetime(df["Date"])
#Variacion anual
df["Variacion"] = (df["Close"] - df["Open"]) / df["Open"]
df["Anio"] = df["Date"].dt.year
df["Media30"] = df["Close"].rolling(window=30).mean()



#Grafica 3

con_volumen = df[df["Volume"] > 0].copy()
con_volumen["Movimiento"] = con_volumen["Variacion"].abs()

plt.figure(figsize=(9, 4.5))
sns.scatterplot(data=con_volumen, x="Volume", y="Movimiento",
                s=12, alpha=0.35, color=AZUL, edgecolor=None)

plt.xscale("log")
plt.title("Mas volumen no garantiza mas movimiento")
plt.xlabel("Volumen operado (escala logaritmica)")
plt.ylabel("Movimiento del dia (variacion absoluta)")
plt.savefig("s3_relacion.png", dpi=150, bbox_inches="tight")
plt.show()