from kedro.pipeline import Pipeline, node, pipeline
from .nodes import entrenar_logistic_regression, evaluar_logistic_regression

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=entrenar_logistic_regression,
            inputs=["X_train", "y_train"],
            outputs="modelo_logistic_regression",
            name="entrenar_logistic_regression_node",
        ),
        node(
            func=evaluar_logistic_regression,
            inputs=["modelo_logistic_regression", "X_test", "y_test"],
            outputs="score_logistic_regression",
            name="evaluar_logistic_regression_node",
        ),
    ])
