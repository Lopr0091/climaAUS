from kedro.pipeline import Pipeline, node, pipeline
from .nodes import entrenar_random_forest, evaluar_random_forest

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=entrenar_random_forest,
            inputs=["X_train", "y_train"],
            outputs="modelo_random_forest",
            name="entrenar_random_forest_node",
        ),
        node(
            func=evaluar_random_forest,
            inputs=["modelo_random_forest", "X_test", "y_test"],
            outputs="score_random_forest",
            name="evaluar_random_forest_node",
        ),
    ])
