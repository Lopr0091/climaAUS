import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generar_graficos(df: pd.DataFrame) -> None:
    # Matriz de correlación
    plt.figure(figsize=(12, 10))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title("Matriz de Correlación")
    plt.show()

    # Histogramas
    print("\n--- Histogramas de variables numéricas ---")
    df.select_dtypes(include=["float64", "int64"]).hist(bins=30, figsize=(20, 15))
    plt.tight_layout()
    plt.show()

    # Boxplots para detectar outliers
    print("\n--- Boxplots para detectar valores atípicos ---")
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
    for col in numeric_cols:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot de {col}")
        plt.show()

    # Gráfico de barras por mes
    print("\n--- Gráfico mensual ---")
    if 'Date' in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        df["Mes"] = df["Date"].dt.month
        mensual = df.groupby("Mes")[["MinTemp", "MaxTemp", "Rainfall"]].mean()

        mensual.plot(kind="bar", figsize=(10, 6), title="Promedios mensuales")
        plt.xlabel("Mes")
        plt.ylabel("Promedio")
        plt.tight_layout()
        plt.show()
