from kedro.pipeline import Pipeline, node, pipeline
from .nodes import guardar_graficos

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=guardar_graficos,
            inputs="datos_limpios",
            outputs=None,
            name="guardar_graficos"
        )
    ])
