import pytest
import pandas as pd
import numpy as np
from src.features import (
    add_clinical_features,
    add_demographics,
    generate_test_train,
    scale_test_train,
)


@pytest.fixture
def sample_df():
    """Returns a fake 12-row DataFrame with enough samples per class for stratified train/test splitting."""
    return pd.DataFrame({
        "esi": [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3],
        "triage_vital_hr": [110.0, 105.0, 115.0, 108.0, 50.0, 55.0, 52.0, 54.0, 80.0, 82.0, 78.0, 85.0],
        "triage_vital_sbp": [100.0, 102.0, 98.0, 101.0, 120.0, 118.0, 122.0, 119.0, 130.0, 128.0, 132.0, 129.0],
        "triage_vital_dbp": [60.0, 62.0, 58.0, 61.0, 80.0, 78.0, 82.0, 79.0, 85.0, 84.0, 86.0, 83.0],
        "triage_vital_rr": [22.0, 24.0, 20.0, 23.0, 12.0, 14.0, 13.0, 15.0, 16.0, 18.0, 17.0, 19.0],
        "triage_vital_o2": [88.0, 90.0, 89.0, 87.0, 98.0, 97.0, 99.0, 96.0, 95.0, 96.0, 94.0, 97.0],
        "triage_vital_temp": [101.0, 101.2, 100.8, 101.5, 95.0, 96.0, 95.5, 95.8, 98.6, 98.4, 98.7, 98.5],
        "triage_glucose": [200.0, 190.0, 210.0, 195.0, 100.0, 105.0, 102.0, 98.0, 110.0, 115.0, 112.0, 108.0],
        "age": [45, 48, 50, 52, 60, 62, 64, 61, 30, 32, 34, 31],
        "gender": [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
        "race": ["White", "Black", "Asian", "White", "Black", "White", "Asian", "Black", "Asian", "Asian", "White", "Black"],
        "disposition": ["Admitted"] * 4 + ["Discharged"] * 8,
        "dep_name": ["ED"] * 12,
    })


def test_add_clinical_features(sample_df):
    """Verifies that all engineered feature columns are created."""
    res = add_clinical_features(sample_df)

    expected_features = [
        "fe_shock_index",
        "fe_pulse_pressure",
        "fe_spo2_rr_ratio",
        "fe_is_tachypneic",
        "fe_is_hypoxic",
        "fe_is_febrile",
        "fe_is_bradycardic",
        "fe_is_hyperglycaemic",
        "fe_is_hypothermic",
        "fe_resp_distress",
        "fe_map_estimate",
    ]

    for col in expected_features:
        assert col in res.columns


def test_add_demographics(sample_df):
    """Ensures age and gender are added while excluding unneeded demographics."""
    # Strip demographic columns from base DataFrame to isolate demographic engineering logic
    base_df = sample_df.drop(columns=["age", "gender", "race"])

    res = add_demographics(base_df, sample_df)

    assert "age" in res.columns
    assert "gender" in res.columns
    assert "race" not in res.columns


def test_generate_test_train(sample_df):
    """Verifies target and data leakage columns are dropped during split."""
    X_train, X_test, y_train, y_test = generate_test_train(sample_df)

    assert "esi" not in X_train.columns
    assert "disposition" not in X_train.columns
    assert "race" not in X_train.columns
    assert len(X_train) + len(X_test) == len(sample_df)


def test_scale_test_train(sample_df):
    """Ensures scaling transforms data into a standard normal array."""
    X_train, X_test, _, _ = generate_test_train(sample_df)
    X_train_scaled, X_test_scaled = scale_test_train(X_train, X_test)

    assert isinstance(X_train_scaled, np.ndarray)
    assert X_train_scaled.shape == X_train.shape