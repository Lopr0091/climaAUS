import joblib
import pandas as pd

# Cargar X_train para obtener las columnas en el orden correcto
X_train = pd.read_csv("data/05_model_input/X_train.csv", encoding="latin1")

# Guardar columnas en el orden usado durante entrenamiento
joblib.dump(X_train.columns.tolist(), "data/06_models/columnas_modelo.pkl")

print("✅ columnas_modelo.pkl guardado correctamente.")
