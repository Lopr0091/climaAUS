import pandas as pd
import random
import os
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def generar_dataset_entrenamiento(cultivos_info: pd.DataFrame) -> pd.DataFrame:
    print("📋 Primeras filas del CSV de cultivos:")
    print(cultivos_info.head())
    print("🧼 Columnas con valores nulos:")
    print(cultivos_info.isnull().sum())

    condiciones = []
    intentos = 0

    while len(condiciones) < 1000 and intentos < 5000:
        cultivo = cultivos_info.sample(1).iloc[0]
        mes = random.randint(1, 12)
        temp = random.uniform(5, 40)
        lluvia = random.uniform(100, 900)

        regiones = cultivo["regiones"]
        if not isinstance(regiones, str):
            intentos += 1
            continue

        region = random.choice([r.strip() for r in regiones.split(",")])

        es_apropiado = (
            cultivo["mes_inicio"] <= mes <= cultivo["mes_fin"] and
            cultivo["temp_min"] <= temp <= cultivo["temp_max"] and
            cultivo["lluvia_min"] <= lluvia <= cultivo["lluvia_max"]
        )

        condiciones.append({
            "mes": mes,
            "temperatura": round(temp, 1),
            "lluvia": round(lluvia, 1),
            "region": region,
            "cultivo": cultivo["cultivo"],
            "siembra_apropiada": int(es_apropiado)
        })

        intentos += 1

    df = pd.DataFrame(condiciones)
    print(f"🔍 Se generaron {len(df)} registros sintéticos:")
    print(df.head())

    return df

def entrenar_modelo(df: pd.DataFrame) -> pd.DataFrame:
    le_region = LabelEncoder()
    le_cultivo = LabelEncoder()
    df["region"] = le_region.fit_transform(df["region"])
    df["cultivo"] = le_cultivo.fit_transform(df["cultivo"])

    X = df[["mes", "temperatura", "lluvia", "region", "cultivo"]]
    y = df["siembra_apropiada"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    score = clf.score(X_test, y_test)
    print(f"📊 Score del modelo actual: {score:.4f}")

    # Guardar con historial
    csv_path = "data/08_reporting/score_modelo.csv"
    nueva_fila = pd.DataFrame({
        "fecha": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "score": [score]
    })

    if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
        historial = pd.read_csv(csv_path)
        historial_actualizado = pd.concat([historial, nueva_fila], ignore_index=True)
    else:
        historial_actualizado = nueva_fila

    historial_actualizado.to_csv(csv_path, index=False)

    print("\n📈 Historial de scores:")
    print(historial_actualizado.tail())

    return nueva_fila
