import pandas as pd
import matplotlib.pyplot as plt

def comparar_modelos(score_logistic: dict, score_decision_tree: dict, score_random_forest: dict) -> pd.DataFrame:
    df_resultados = pd.DataFrame([
        {"modelo": "Logistic Regression", **score_logistic},
        {"modelo": "Decision Tree", **score_decision_tree},
        {"modelo": "RandomForest", **score_random_forest}
    ])

    # Asegurar columnas numéricas
    metricas = ["accuracy", "precision", "recall", "f1_score"]
    df_resultados[metricas] = df_resultados[metricas].astype(float)

    # Mostrar tabla
    print("📋 Tabla comparativa:")
    print(df_resultados)

    # Graficar
    df_plot = df_resultados.set_index("modelo")
    ax = df_plot.plot(kind="bar", figsize=(10, 6), ylim=(0, 1))
    plt.title("Comparación de modelos de clasificación")
    plt.ylabel("Score")
    plt.xlabel("Modelo")
    plt.tight_layout()
    plt.savefig("data/08_reporting/grafico_comparacion_modelos.png")
    plt.show()

    return df_resultados
