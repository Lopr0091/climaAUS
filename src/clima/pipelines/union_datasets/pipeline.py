from kedro.pipeline import Pipeline, node, pipeline
from .nodes import unir_datasets

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=unir_datasets,
            inputs=["datos_limpios", "entrenamiento_siembra"],
            outputs="datos_unidos",
            name="unir_datasets_node"
        )
    ])
