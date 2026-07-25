from data import load_clean_df
from features import generate_test_train, scale_test_train
from model import build_model

DATA_PATH = "../data/yaleemmlc_admissionprediction_triage.csv"

# cfg  = load_config(args.config)

clean_df = load_clean_df(DATA_PATH)
X_train_plus, X_test_plus,y_train, y_test = generate_test_train(clean_df)
X_train_plus_scaled, X_test_plus_scaled = scale_test_train(X_train_plus, X_test_plus)
ensemble_model = build_model()


