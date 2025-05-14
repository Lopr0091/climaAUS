import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def entrenar_random_forest(X_train: pd.DataFrame, y_train: pd.Series):
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X_train, y_train.values.ravel())
    return modelo

def evaluar_random_forest(modelo, X_test: pd.DataFrame, y_test: pd.Series) -> pd.DataFrame:
    y_pred = modelo.predict(X_test)
    return pd.DataFrame([{
        "modelo": "RandomForest",
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, average="macro"),
        "recall": recall_score(y_test, y_pred, average="macro"),
        "f1_score": f1_score(y_test, y_pred, average="macro"),
    }])

