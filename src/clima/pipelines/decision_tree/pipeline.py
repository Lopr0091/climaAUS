from kedro.pipeline import Pipeline, node, pipeline
from .nodes import entrenar_decision_tree, evaluar_decision_tree

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=entrenar_decision_tree,
            inputs=["X_train", "y_train"],
            outputs="modelo_decision_tree",
            name="entrenar_decision_tree_node",
        ),
        node(
            func=evaluar_decision_tree,
            inputs=["modelo_decision_tree", "X_test", "y_test"],
            outputs="score_decision_tree",
            name="evaluar_decision_tree_node",
        ),
    ])
