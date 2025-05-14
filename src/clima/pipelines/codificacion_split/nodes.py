import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def codificar_y_split(df: pd.DataFrame):
    X = df.drop("cultivo", axis=1)
    y = df["cultivo"]

    # Detectar columnas categóricas
    columnas_categoricas = X.select_dtypes(include="object").columns.tolist()

    # Filtrar columnas con cardinalidad razonable (menos de 100 valores únicos)
    columnas_categoricas_validas = [
        col for col in columnas_categoricas if X[col].nunique() < 100
    ]

    # Guardar trazabilidad
    pd.Series(columnas_categoricas).to_csv("data/08_reporting/categoricas_todas.csv", index=False)
    pd.Series(columnas_categoricas_validas).to_csv("data/08_reporting/categoricas_utilizadas.csv", index=False)

    # Codificar
    encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    X_codificado = pd.DataFrame(
        encoder.fit_transform(X[columnas_categoricas_validas]),
        columns=encoder.get_feature_names_out(columnas_categoricas_validas),
        index=X.index
    )

    # Combinar
    X_numerico = X.drop(columns=columnas_categoricas)
    X_final = pd.concat([X_numerico.reset_index(drop=True), X_codificado.reset_index(drop=True)], axis=1)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X_final, y, test_size=0.2, random_state=42, stratify=y
    )

    return X_train, X_test, y_train, y_test, pd.Series(columnas_categoricas_validas), encoder
