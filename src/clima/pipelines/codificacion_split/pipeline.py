from kedro.pipeline import node, Pipeline, pipeline
from .nodes import codificar_y_split

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=codificar_y_split,
            inputs="datos_unidos",
            outputs=[
                "X_train",
                "X_test",
                "y_train",
                "y_test",
                "categoricas_excluidas",
                "encoder"
            ],
            name="codificar_y_split_node"
        )
    ])
