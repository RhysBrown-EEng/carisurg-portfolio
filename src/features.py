import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def add_clinical_features(old_df):
  """
    Creates newly engineered features to improve the performance of the model.
    Args: Raw Dataframe with no engineered features
    Returns: New Dataframe with engineered features

  """

  new_df = old_df.copy()

  new_df["fe_shock_index"]    = new_df["triage_vital_hr"] / new_df["triage_vital_sbp"]       # HR / SBP         (uses BP)
  new_df["fe_pulse_pressure"] = new_df["triage_vital_sbp"] - new_df["triage_vital_dbp"]      # SBP - DBP        (uses BP)
  new_df["fe_spo2_rr_ratio"]  = new_df["triage_vital_o2"] / new_df["triage_vital_rr"]        # oxygen vs effort (NO BP)

  new_df["fe_is_tachypneic"] = (new_df["triage_vital_rr"]   > 20).astype(int)   # fast breathing
  new_df["fe_is_hypoxic"]    = (new_df["triage_vital_o2"]   < 92).astype(int)   # low oxygen
  new_df["fe_is_febrile"]    = (new_df["triage_vital_temp"] >= 100.4).astype(int)  # fever

  new_df["fe_is_bradycardic"]    = (new_df["triage_vital_hr"] < 60.0).astype(int)
  new_df["fe_is_hyperglycaemic"]    = (new_df["triage_glucose"] >= 180.0).astype(int)
  new_df["fe_is_hypothermic"]    = (new_df["triage_vital_temp"] < 96.8).astype(int)
  new_df["fe_resp_distress"]    = (new_df["triage_vital_o2"] < 90.0).astype(int) |(new_df["triage_vital_rr"] > 20).astype(int)

  new_df["fe_map_estimate"] = new_df["triage_vital_dbp"] + new_df["fe_pulse_pressure"] / 3.0

  return new_df

def add_demographics(X_fe, df):
    """Bolt the encoded demographics onto an existing feature frame (aligned by row)."""
    rows = X_fe.index
    #extra = demo_1hot.loc[rows].copy() #this line included unwanted demographic features like race
    extra = pd.DataFrame(index=rows)

    #Include age and gender back in final dataset.

    extra["age"] = df.loc[rows, "age"]         # numeric already
    extra["gender"] = df.loc[rows, "gender"]   # 0/1 already
    return pd.concat([X_fe, extra], axis=1)

def generate_test_train(df):
    TARGET = "esi"

    # Vital-sign columns measured at the front door:
    VITALS = ["triage_vital_hr", "triage_vital_sbp", "triage_vital_dbp", "triage_vital_rr",
            "triage_vital_o2", "triage_vital_temp", "triage_glucose"]
    # Who the patient is (some of these are fairness-sensitive — handle with care):
    DEMOGRAPHICS = ["age", "gender", "ethnicity", "race", "lang", "religion",
                    "maritalstatus", "employstatus", "insurance_status"]
    # Administrative / arrival details:
    ADMIN = ["dep_name", "arrivalmode", "arrivalmonth", "arrivalday", "arrivalhour_bin"]
    # OUTCOMES of the visit — known only AFTER triage, so they must never be model inputs:
    LEAKAGE = ["disposition", "previousdispo"]

    FEATURES = [c for c in df.columns if c != TARGET and c not in LEAKAGE + ADMIN + DEMOGRAPHICS]

    X, y = df[FEATURES], df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42)
    print("train:", X_train.shape[0], "| test:", X_test.shape[0])

    X_train_fe = add_clinical_features(X_train)
    X_test_fe  = add_clinical_features(X_test)

    X_train_plus = add_demographics(X_train_fe, df)
    X_test_plus = add_demographics(X_test_fe, df)

    return X_train_plus, X_test_plus,y_train, y_test 

def scale_test_train(X_train_plus, X_test_plus):
    plus_scaler = StandardScaler()

    X_train_plus_scaled = plus_scaler.fit_transform(X_train_plus)
    X_test_plus_scaled  = plus_scaler.transform(X_test_plus)

    return X_train_plus_scaled, X_test_plus_scaled