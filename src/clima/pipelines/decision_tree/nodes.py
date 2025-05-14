import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def entrenar_decision_tree(X_train: pd.DataFrame, y_train: pd.Series):
    modelo = DecisionTreeClassifier(random_state=42)
    modelo.fit(X_train, y_train.values.ravel())
    return modelo

def evaluar_decision_tree(modelo, X_test: pd.DataFrame, y_test: pd.Series) -> pd.DataFrame:
    y_pred = modelo.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    return pd.DataFrame([{"score": score}])  # ✅ ahora es un DataFrame
