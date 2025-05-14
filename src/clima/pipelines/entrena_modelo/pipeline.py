from kedro.pipeline import Pipeline, node, pipeline
from .nodes import entrenar_modelo, evaluar_modelo

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=entrenar_modelo,
            inputs=["X_train", "y_train"],
            outputs="modelo_entrenado",
            name="entrenar_modelo_node",
        ),
        node(
            func=evaluar_modelo,
            inputs=["modelo_entrenado", "X_test", "y_test"],
            outputs="score_modelo",
            name="evaluar_modelo_node",
        ),
    ])
