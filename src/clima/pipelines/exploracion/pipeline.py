from kedro.pipeline import Pipeline, node
from .nodes import explorar_datos

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=explorar_datos,
                inputs="datos_crudos",
                outputs=None,
                name="explorar_datos_node",
            ),
        ]
    )
