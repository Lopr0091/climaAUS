import os
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.SettingWithCopyWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)

archivo_limpio = "data/03_primary/datos_limpios.csv"

def duplicar_dataset(df: pd.DataFrame) -> pd.DataFrame:
    if os.path.exists(archivo_limpio):
        print("Cargando...")
        return pd.read_csv(archivo_limpio)

    print("Limpiando...")

    df_copia = df.copy()

    columnas_a_eliminar = [
        "Evaporation", "Sunshine", "Cloud9am", "Cloud3pm",
        "WindGustDir", "WindDir9am", "WindDir3pm",
        "RainToday", "RISK_MM"
    ]

    columnas_presentes = [col for col in columnas_a_eliminar if col in df_copia.columns]
    df_copia.drop(columns=columnas_presentes, inplace=True)

    print(f"Columnas eliminadas: {columnas_presentes}")
    print(f"Columnas finales: {list(df_copia.columns)}")

    df_copia.to_csv(archivo_limpio, index=False)
    return df_copia

def explorar_preparacion(df: pd.DataFrame) -> pd.DataFrame:
    columnas_a_eliminar = [
        "Evaporation", "Sunshine", "Cloud9am", "Cloud3pm",
        "WindGustDir", "WindDir9am", "WindDir3pm",
        "RainToday", "RISK_MM"
    ]
    print(f"Columnas a eliminadas: {columnas_a_eliminar}")
    num_filas = df.shape[0]
    print("Shape inicial: ", df.shape)

    print("\n--- Valores nulos ---")
    print(df.isnull().sum())

    print("\n--- Porcentaje valores nulos ---")
    porcentaje_nulos = (df.isnull().sum() / num_filas * 100).round(2)
    print(porcentaje_nulos.astype(str) + "%")

    print("\n--- Quitando filas con menos de 9% de nulos... ---")
    columnas_menos_9 = porcentaje_nulos[porcentaje_nulos < 9].index.tolist()
    df_filtrado = df.dropna(subset=columnas_menos_9)
    print(f"Filas antes: {num_filas}, después: {df_filtrado.shape[0]}")

    print("\n--- Rellenando >9% ---")
    columnas_mas_9 = porcentaje_nulos[porcentaje_nulos >= 9].index.tolist()
    for col in columnas_mas_9:
        if df_filtrado[col].dtype in ['float64', 'int64']:
            mediana = df_filtrado[col].median()
            print(f" '{col}' con mediana: {mediana}")
            df_filtrado[col] = df_filtrado[col].fillna(mediana)

    print("\n--- Outliers antes de eliminar extremos ---")
    columnas_numericas = df_filtrado.select_dtypes(include=["float64", "int64"]).columns
    for col in columnas_numericas:
        Q1 = df_filtrado[col].quantile(0.25)
        Q3 = df_filtrado[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inf = Q1 - 1.5 * IQR
        limite_sup = Q3 + 1.5 * IQR
        outliers = df_filtrado[(df_filtrado[col] < limite_inf) | (df_filtrado[col] > limite_sup)]
        porcentaje_outliers = (len(outliers) / df_filtrado.shape[0]) * 100
        print(f"{col}: {len(outliers)} outliers ({porcentaje_outliers:.2f}%)")

    # 🔧 Filtrado: Rainfall no se filtra por outliers
    for col in columnas_numericas:
        if col == "Rainfall":
            continue
        Q1 = df_filtrado[col].quantile(0.25)
        Q3 = df_filtrado[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inf = Q1 - 1.5 * IQR
        limite_sup = Q3 + 1.5 * IQR
        df_filtrado = df_filtrado[(df_filtrado[col] >= limite_inf) & (df_filtrado[col] <= limite_sup)]

    print("\n--- Outliers después de eliminar extremos ---")
    for col in columnas_numericas:
        Q1 = df_filtrado[col].quantile(0.25)
        Q3 = df_filtrado[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inf = Q1 - 1.5 * IQR
        limite_sup = Q3 + 1.5 * IQR
        outliers = df_filtrado[(df_filtrado[col] < limite_inf) | (df_filtrado[col] > limite_sup)]
        porcentaje_outliers = (len(outliers) / df_filtrado.shape[0]) * 100
        print(f"{col}: {len(outliers)} outliers ({porcentaje_outliers:.2f}%)")

    print("\nShape final después de eliminar outliers:", df_filtrado.shape)

    df_filtrado.to_csv(archivo_limpio, index=False)
    print(f"\nModificaciones guardadas en {archivo_limpio}")

    return df_filtrado
