import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))
sys.path.append(str(ROOT_DIR / "src"))

from src.data import load_clean_df
from src.features import generate_test_train, scale_test_train
from src.model import build_model, evaluate_model, train_and_time_model
from src.utils import load_config, parse_args

args = parse_args()

cfg  = load_config(args.config)

clean_df = load_clean_df(cfg["data"]["raw_path"])
X_train_plus, X_test_plus,y_train, y_test = generate_test_train(clean_df)
X_train_plus_scaled, X_test_plus_scaled = scale_test_train(X_train_plus, X_test_plus)
untrained_ensemble_model = build_model("logistic_regression", cfg, cfg["seed"])

trained_ensemble_model, training_time = train_and_time_model(
    untrained_ensemble_model,
    X_train_plus_scaled,
    y_train
)

evaluate_model(
    "Ensemble Model",
    trained_ensemble_model, 
    X_test_plus_scaled, 
    y_test, 
    training_time, 
    "Medium. Model is comprised of Logistic Regression and Random_Forest. Two readily explainable models"
)




