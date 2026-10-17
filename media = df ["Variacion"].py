media = df ["Variacion"].mean()
mediana = df["Variacion"].median()

plt.figure(figsize=(9, 4.5))
plt.hist(df["Variacion"], bins=60, color=AZUL, edgecolor="white", linewidth=0.3)
plt.axvline(0, color=GRIS, linewidth=1)
plt.axvline(mediana, color=ROJO, linewidth=1.5, linestyle="--",
            label=f"mediana {mediana*100:.2f} %")
plt.title("84 porciento de los dias se mueve menos de 5 porciento")
plt.xlabel("Variacion diaria")
plt.ylabel("Numero de dias")
plt.legend(frameon=False)
plt.savefig("g1_distribucion.png", dpi=150, bbox_inches="tight")