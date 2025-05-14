import joblib

modelo = joblib.load("data/06_models/modelo_entrenado.pkl")
print(list(modelo.feature_names_in_))
