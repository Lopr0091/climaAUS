from kedro.pipeline import Pipeline, node
from .nodes import cargar_datos

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=cargar_datos,
            inputs=None,
            outputs="datos_crudos",
            name="cargar_datos_node"
        )
    ])
