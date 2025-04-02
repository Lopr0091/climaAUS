from kedro.pipeline import node, Pipeline, pipeline
from .nodes import duplicar_dataset, explorar_preparacion

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=duplicar_dataset,
                inputs="datos_crudos",
                outputs="datos_limpios",
                name="duplicar_dataset"
            ),
            node(
                func=explorar_preparacion,
                inputs="datos_limpios",
                outputs="datos_limpios_actualizados",
                name="explorar_preparacion_node",
            ),
        ]
    )
