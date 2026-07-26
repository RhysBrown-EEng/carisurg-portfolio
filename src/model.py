import random
import pandas as pd
import time
import timeit

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import f1_score, recall_score

from utils import format_time_period

def build_model(model_name, cfg, seed):

    if model_name not in cfg["final_models"]:
        raise ValueError(
            f"Unknown model '{model_name}'. Valid options are: {cfg['final_models']}"
        )

    print(f"Training {model_name}")
    params = cfg["params"][model_name]

    if (model_name == "random_forest"):
        final_model = RandomForestClassifier(**params, random_state = seed)
    elif (model_name == "logistic_regression"):
        final_model = LogisticRegression(**params, random_state = seed)
    elif (model_name == "ensemble"):
        rf_params = cfg["params"]["random_forest"]
        lr_params = cfg["params"]["logistic_regression"]

        rf_model = RandomForestClassifier(**rf_params, random_state = seed)
        lr_model = LogisticRegression(**lr_params, random_state = seed)

        final_model = VotingClassifier(
            **params, 
            estimators= [("rf_ensemble", rf_model), ("lr_ensemble", lr_model)]
        )

    return final_model

def train_and_time_model(original_model, X_train, y_train):

    trained_model = original_model

    start_time = time.perf_counter()
    trained_model.fit(X_train, y_train)
    stop_time = time.perf_counter()

    training_time = stop_time-start_time

    return trained_model, training_time

def evaluate_model(model_name, model, X_test, y_test, training_time, explainability):

    pred = model.predict(X_test)

    random_idx = random.randint(0, len(X_test) - 1)
    single_sample = X_test.iloc[[random_idx]] if hasattr(X_test, 'iloc') else X_test[[random_idx]]

    inference_time = timeit.timeit(lambda: model.predict(single_sample), number=100) / 100.0

    # Convert multiclass labels to binary for ESI level 1 (1 vs not 1)
    y_test_class1 = (y_test == 1).astype(int)
    pred_class1 = (pred == 1).astype(int)

    benchmark = {
        "Model": model_name,
        "Accuracy": round(model.score(X_test, y_test), 2), # Changed X_test_scaled to X_test (parameter)
        "Recall ESI 1": round(recall_score(y_test_class1, pred_class1), 2),
        "Macro F1": round(f1_score(y_test, pred, average="macro"), 2),
        "Training Time": format_time_period(training_time),
        "Inference Time": format_time_period(inference_time),
        "Explainability": explainability
    }

    print(pd.DataFrame([benchmark]))

    