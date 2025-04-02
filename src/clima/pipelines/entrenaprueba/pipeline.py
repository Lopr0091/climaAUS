from kedro.pipeline import Pipeline, node, pipeline
from .nodes import generar_dataset_entrenamiento, entrenar_modelo

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=generar_dataset_entrenamiento,
            inputs="cultivos_info",
            outputs="entrenamiento_siembra",
            name="generar_datos_sinteticos"
        ),
        node(
            func=entrenar_modelo,
            inputs="entrenamiento_siembra",
            outputs="score_modelo",
            name="entrenar_modelo_rf"
        ),
    ])
