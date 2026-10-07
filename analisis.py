from pathlib import Path
import pandas as pd

def analizar_datos_sensores():
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR / "data"
    INPUT_FILE = DATA_DIR / "mediciones.csv"
    OUTPUT_FILE = DATA_DIR / "alertas.csv"

    if not INPUT_FILE.exists():
        print(f"⚠️ ¡Atención! No se encontró el archivo: {INPUT_FILE}")
        print("Por favor asegúrate de colocar 'mediciones.csv' dentro de la carpeta 'data/'.")
        return

    df = pd.read_csv(INPUT_FILE)

    print("===========================================")
    print("   RESULTADOS DEL ANÁLISIS DE SENSORES     ")
    print("===========================================\n")

    total_registros = len(df)
    sensores_unicos = df["id_sensor"].nunique()
    print(f"1. Total de registros analizados: {total_registros:,}")
    print(f"   Total de sensores distintos: {sensores_unicos}\n")

    print("2. Temperatura promedio por planta:")
    temp_prom = df.groupby("planta")["temperatura"].mean()
    for planta, temp in temp_prom.items():
        print(f"   - Planta '{planta}': {temp:.2f} °C")
    print()

    max_temp = df["temperatura"].max()
    max_registros = df[df["temperatura"] == max_temp]
    print(f"3. Temperatura máxima registrada: {max_temp:.2f} °C")
    for _, row in max_registros.iterrows():
        print(f"   - Sensor ID: {row['id_sensor']} | Fecha/Hora: {row['timestamp']} | Planta: {row['planta']}")
    print()

    df_alertas = df[df["temperatura"] > 85.0]
    total_alertas = len(df_alertas)
    print(f"4. Cantidad de lecturas con alerta (> 85 °C): {total_alertas}\n")

    print("5. Planta(s) con mayor cantidad de alertas de temperatura (> 85 °C):")
    if total_alertas > 0:
        alertas_planta = df_alertas["planta"].value_counts()
        max_alertas = alertas_planta.max()
        top_plantas = alertas_planta[alertas_planta == max_alertas]
        for planta, conteo in top_plantas.items():
            print(f"   - Planta '{planta}': {conteo} alerta(s)")
    else:
        print("   - No se registraron alertas.")
    print()

    df_alertas.to_csv(OUTPUT_FILE, index=False)
    print(f"6. Archivo de alertas exportado exitosamente a:\n   {OUTPUT_FILE}\n")
    print("===========================================")

if __name__ == "__main__":
    analizar_datos_sensores()
