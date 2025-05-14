from kedro.pipeline import Pipeline
from clima.pipelines.prueba import pipeline as prueba_pipeline
from clima.pipelines.exploracion import pipeline as exploracion_pipeline
from clima.pipelines.entrenaprueba import pipeline as entrenaprueba_pipeline
from clima.pipelines.exploragrafico import pipeline as exploragrafico_pipeline
from clima.pipelines.preparacion import pipeline as preparacion_pipeline
from clima.pipelines.preparagrafico import pipeline as preparagrafico_pipeline
from clima.pipelines.union_datasets import pipeline as union_datasets_pipeline
from clima.pipelines.codificacion_split import pipeline as codificacion_split_pipeline
from clima.pipelines.entrena_modelo import pipeline as entrena_modelo_pipeline
from clima.pipelines.logistic_regression import pipeline as logistic_regression_pipeline
from clima.pipelines.decision_tree import pipeline as decision_tree_pipeline
from clima.pipelines.support_vector_machine import pipeline as support_vector_machine_pipeline
from clima.pipelines.random import pipeline as random_pipeline
from clima.pipelines.comparacion_modelos import pipeline as comparacion_modelos_pipeline


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
        "union_datasets": union_datasets_pipeline.create_pipeline(),
        "codificacion_split": codificacion_split_pipeline.create_pipeline(),
        "entrena_modelo": entrena_modelo_pipeline.create_pipeline(),
        "logistic_regression": logistic_regression_pipeline.create_pipeline(),
        "decision_tree": decision_tree_pipeline.create_pipeline(),
        "support_vector_machine": support_vector_machine_pipeline.create_pipeline(),
        "random": random_pipeline.create_pipeline(),
        "comparacion_modelos": comparacion_modelos_pipeline.create_pipeline(),


    }

    return pipelines
