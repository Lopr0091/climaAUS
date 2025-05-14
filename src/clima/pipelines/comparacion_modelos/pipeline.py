from kedro.pipeline import Pipeline, node, pipeline
from .nodes import comparar_modelos

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=comparar_modelos,
            inputs=[
                "score_logistic_regression",  # corregido
                "score_decision_tree",
                "score_random_forest"
            ],
            outputs="tabla_comparacion_modelos",
            name="comparar_modelos_node"
        )
    ])
