import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def guardar_graficos(df: pd.DataFrame) -> None:
    carpeta = "data/08_reporting/figuras"
    os.makedirs(carpeta, exist_ok=True)

    # Matriz de correlación
    correlaciones = df.corr(numeric_only=True)
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlaciones, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Matriz de Correlación")
    ruta = os.path.join(carpeta, "matriz_correlacion.png")
    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    plt.show()

    # Histogramas
    print("\n--- Histogramas de variables numéricas ---")
    fig = df.select_dtypes(include=["float64", "int64"]).hist(bins=30, figsize=(20, 15))
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta, "histogramas.png"), dpi=300, bbox_inches="tight")
    plt.show()

    # Boxplots individuales
    print("\n--- Boxplots para detectar valores atípicos ---")
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
    for col in numeric_cols:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot de {col}")
        ruta_box = os.path.join(carpeta, f"boxplot_{col}.png")
        plt.savefig(ruta_box, dpi=300, bbox_inches="tight")
        plt.show()

    # Gráfico mensual
    print("\n--- Gráfico mensual ---")
    if 'Date' in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        df["Mes"] = df["Date"].dt.month
        mensual = df.groupby("Mes")[["MinTemp", "MaxTemp", "Rainfall"]].mean()
        mensual.plot(kind="bar", figsize=(10, 6), title="Promedios mensuales")
        plt.xlabel("Mes")
        plt.ylabel("Promedio")
        plt.tight_layout()
        plt.savefig(os.path.join(carpeta, "promedios_mensuales.png"), dpi=300, bbox_inches="tight")
        plt.show()
