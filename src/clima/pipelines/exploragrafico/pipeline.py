from kedro.pipeline import Pipeline, node
from .nodes import generar_graficos

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=generar_graficos,
                inputs="datos_crudos",
                outputs=None,
                name="generar_graficos_node",
            ),
        ]
    )
