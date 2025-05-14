import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

def entrenar_logistic_regression(X_train: pd.DataFrame, y_train: pd.Series):
    modelo = LogisticRegression(max_iter=1000, multi_class='multinomial', solver='lbfgs')
    modelo.fit(X_train, y_train.values.ravel())  # .ravel() para evitar el warning
    return modelo

def evaluar_logistic_regression(modelo, X_test: pd.DataFrame, y_test: pd.Series):
    y_pred = modelo.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    return pd.DataFrame({"accuracy": [score]})
