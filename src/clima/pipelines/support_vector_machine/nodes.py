import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def entrenar_svm(X_train: pd.DataFrame, y_train: pd.Series):
    modelo = SVC(kernel='rbf', probability=True, random_state=42)
    modelo.fit(X_train, y_train.values.ravel())
    return modelo

def evaluar_svm(modelo, X_test: pd.DataFrame, y_test: pd.Series):
    y_pred = modelo.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    return {"score": score}
