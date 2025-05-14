from kedro.pipeline import Pipeline, node, pipeline
from .nodes import entrenar_svm, evaluar_svm

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=entrenar_svm,
            inputs=["X_train", "y_train"],
            outputs="modelo_svm",
            name="entrenar_svm_node",
        ),
        node(
            func=evaluar_svm,
            inputs=["modelo_svm", "X_test", "y_test"],
            outputs="score_svm",
            name="evaluar_svm_node",
        ),
    ])
