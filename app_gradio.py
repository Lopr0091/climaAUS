import pandas as pd
from sqlalchemy import create_engine
import joblib
import gradio as gr

# Configurar conexión a MySQL
usuario = "root"
contraseña = ""
host = "localhost"
puerto = "3306"
base_de_datos = "clima_aus"
engine = create_engine(f"mysql+pymysql://{usuario}:{contraseña}@{host}:{puerto}/{base_de_datos}")

# Cargar modelo y encoder
modelo = joblib.load("data/06_models/modelo_entrenado.pkl")
encoder = joblib.load("data/06_models/encoder.pkl")

# Cargar columnas categóricas válidas
columnas_categoricas = pd.read_csv("data/08_reporting/categoricas_utilizadas.csv", header=None).squeeze("columns").tolist()

# Obtener nombres de columnas del modelo
columnas_modelo = joblib.load("data/06_models/columnas_modelo.pkl")

def predecir(MinTemp, MaxTemp, Rainfall, WindGustSpeed, WindSpeed9am, WindSpeed3pm,
             Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, Temp9am, Temp3pm,
             mes, temperatura, lluvia, siembra_apropiada, Location, region, RainTomorrow):

    # Crear DataFrame base
    entrada = pd.DataFrame([{
        "MinTemp": MinTemp,
        "MaxTemp": MaxTemp,
        "Rainfall": Rainfall,
        "WindGustSpeed": WindGustSpeed,
        "WindSpeed9am": WindSpeed9am,
        "WindSpeed3pm": WindSpeed3pm,
        "Humidity9am": Humidity9am,
        "Humidity3pm": Humidity3pm,
        "Pressure9am": Pressure9am,
        "Pressure3pm": Pressure3pm,
        "Temp9am": Temp9am,
        "Temp3pm": Temp3pm,
        "mes": mes,
        "temperatura": temperatura,
        "lluvia": lluvia,
        "siembra_apropiada": siembra_apropiada,
        "Location": Location,
        "region": region,
        "RainTomorrow": RainTomorrow
    }])

    # Separar numéricas y categóricas
    entrada_num = entrada.drop(columns=columnas_categoricas)
    entrada_cat = encoder.transform(entrada[columnas_categoricas])
    entrada_cat_df = pd.DataFrame(entrada_cat, columns=encoder.get_feature_names_out(columnas_categoricas))

    # Combinar
    entrada_final = pd.concat([entrada_num.reset_index(drop=True), entrada_cat_df.reset_index(drop=True)], axis=1)

    # Asegurar orden de columnas
    entrada_final = entrada_final.reindex(columns=columnas_modelo, fill_value=0)

    # Predecir
    prediccion = modelo.predict(entrada_final)[0]
    return f"🌾 Cultivo recomendado: {prediccion}"

# Interfaz
demo = gr.Interface(
    fn=predecir,
    inputs=[
        gr.Number(label="MinTemp"),
        gr.Number(label="MaxTemp"),
        gr.Number(label="Rainfall"),
        gr.Number(label="WindGustSpeed"),
        gr.Number(label="WindSpeed9am"),
        gr.Number(label="WindSpeed3pm"),
        gr.Number(label="Humidity9am"),
        gr.Number(label="Humidity3pm"),
        gr.Number(label="Pressure9am"),
        gr.Number(label="Pressure3pm"),
        gr.Number(label="Temp9am"),
        gr.Number(label="Temp3pm"),
        gr.Number(label="mes"),
        gr.Number(label="temperatura"),
        gr.Number(label="lluvia"),
        gr.Number(label="siembra_apropiada"),
        gr.Textbox(label="Location"),
        gr.Textbox(label="region"),
        gr.Radio(["Yes", "No"], label="RainTomorrow", value="No")
    ],
    outputs="text",
    title="Predicción de Cultivo",
    description="Ingresa datos climáticos y condiciones para obtener una predicción de cultivo recomendado."
)

demo.launch()
