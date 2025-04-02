from kedro.pipeline import Pipeline
from clima.pipelines.prueba import pipeline as prueba_pipeline
from clima.pipelines.exploracion import pipeline as exploracion_pipeline
from clima.pipelines.entrenaprueba import pipeline as entrenaprueba_pipeline
from clima.pipelines.exploragrafico import pipeline as exploragrafico_pipeline
from clima.pipelines.preparacion import pipeline as preparacion_pipeline
from clima.pipelines.preparagrafico import pipeline as preparagrafico_pipeline
def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines."""

    pipelines = {
        "prueba": prueba_pipeline.create_pipeline(),
        "exploracion": exploracion_pipeline.create_pipeline(),
        "entrenaprueba": entrenaprueba_pipeline.create_pipeline(),
        "exploragrafico": exploragrafico_pipeline.create_pipeline(),
        "preparacion": preparacion_pipeline.create_pipeline(),
        "preparagrafico": preparagrafico_pipeline.create_pipeline(),
        "__default__": prueba_pipeline.create_pipeline(),
    }

    return pipelines
