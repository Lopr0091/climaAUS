import pandas as pd

def explorar_datos(df: pd.DataFrame) -> None:
    num_filas = df.shape[0]
    print("\n--- Exploración de Datos ---")
    print(f"Shape del dataset: {df.shape}")
    
    print("\n--- Columnas y tipos de datos ---")
    print(df.dtypes)
    
    print("\n--- Head ---")
    print(df.head())

    print("\n--- valores nulos ---")
    print(df.isnull().sum())

    print("\n--- Porcentaje de valores nulos ---")
    print((df.isnull().sum() / num_filas * 100).round(2).astype(str) + "%")

    print("\n--- Estadística descriptiva ---")
    print(df.describe().T)  # Transpuesta para visualización más cómoda

    print("\n--- Conteo de valores únicos por columna ---")
    for col in df.columns:
        print(f"{col}: {df[col].nunique()} valores únicos")

    print("\n--- Detección de outliers usando la regla del IQR ---")
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]
        print(f"{col}: {outliers.shape[0]} outliers")

    print("\n--- Agrupación por Location: media de temperatura y lluvia ---")
    if 'Location' in df.columns:
        agrupado = df.groupby("Location")[["MinTemp", "MaxTemp", "Rainfall"]].mean().sort_values("Rainfall", ascending=False)
        print(agrupado.head())

    print("\n--- Agrupación mensual ---")  # Para la estacionalidad
    if 'Date' in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        df["Mes"] = df["Date"].dt.month
        mensual = df.groupby("Mes")[["MinTemp", "MaxTemp", "Rainfall"]].mean()
        print(mensual)
