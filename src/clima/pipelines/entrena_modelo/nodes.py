import pandas as pd
from sklearn.ensemble import RandomForestClassifier #Este usa Random Forest
from sklearn.metrics import accuracy_score
import joblib

def entrenar_modelo(X_train: pd.DataFrame, y_train: pd.Series):
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X_train, y_train)
    joblib.dump(modelo, "data/06_models/modelo_entrenado.pkl")
    return modelo

def evaluar_modelo(modelo, X_test: pd.DataFrame, y_test: pd.Series) -> pd.DataFrame:
    y_pred = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return pd.DataFrame({"accuracy": [accuracy]})
