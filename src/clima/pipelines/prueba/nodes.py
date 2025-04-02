import pandas as pd

def cargar_datos() -> pd.DataFrame:
    df = pd.read_csv("data/01_raw/weatherAUS.csv")
    print(df.head())
    return df
