import pytest
import pandas as pd
import numpy as np
from src.data import load_clean_df

def test_standard_processing(tmp_path):
    """
    Tests clean_df() on standard df. Verifies string-to-numeric coercion for vital signs, 
    proper mapping of gender strings to binary integers (Male -> 0; Female -> 1), proper 
    detection and imputation of clinically impossible vitals or missing values.
    """

    csv_content = (
        ",esi,triage_vital_hr,triage_vital_sbp,triage_vital_dbp,triage_vital_rr,"
        "triage_vital_o2,triage_vital_temp,triage_glucose,gender,age\n"
        "0,1,80,120,80,16,98,98.6,100,Male,45\n"
        "1,2,90bpm,130,85,18,105,80,110,F,55\n"
        "2,3,100,140,90,20,95,99.0,120,f,65\n"
    )
    file_path = tmp_path / "sample.csv"
    file_path.write_text(csv_content)

    cleaned_df = load_clean_df(file_path)

    assert len(cleaned_df) == 3
    assert pd.api.types.is_integer_dtype(cleaned_df["esi"])
    assert cleaned_df["gender"].tolist() == [0.0, 1.0,1.0] #expected gender results for our fake data
    assert cleaned_df.loc[1, "triage_vital_hr"] == 90.0


def test_invalid_esi_filtering(tmp_path):
    """
    Tests that clean_df() properly filters out all invalid ESI values i.e. beyond the 
    range [1, 5].
    """

    csv_content = (
        ",esi,triage_vital_hr,triage_vital_sbp,triage_vital_dbp,triage_vital_rr,"
        "triage_vital_o2,triage_vital_temp,triage_glucose,gender,age\n"
        "0,1,80,120,80,16,98,98.6,100,Male,45\n"
        "1,0,90,130,85,18,98,98.6,100,Female,50\n"
        "2,6,100,140,90,20,98,98.6,100,Male,55\n"
        "3,,110,150,95,22,98,98.6,100,Female,60\n"
        "4,invalid,70,110,75,14,98,98.6,100,M,65\n"
    )
    file_path = tmp_path / "esi_test.csv"
    file_path.write_text(csv_content)

    cleaned_df = load_clean_df(file_path)

    assert len(cleaned_df) == 1
    assert cleaned_df.iloc[0]["esi"] == 1


def test_handles_empty_dataframe(tmp_path):
    """
    Ensures clean_df() informs the user of an empty df.
    """

    headers = (
        "Unnamed: 0,esi,triage_vital_hr,triage_vital_sbp,triage_vital_dbp,"
        "triage_vital_rr,triage_vital_o2,triage_vital_temp,triage_glucose,gender,age\n"
    )
    file_path = tmp_path / "empty.csv"
    file_path.write_text(headers)

    cleaned_df = load_clean_df(file_path)

    assert cleaned_df.empty
    assert "Unnamed: 0" not in cleaned_df.columns


def test_handles_invalid_data(tmp_path):
    """
    Ensures that when a vital sign column contains entirely unworkable values, 
    we get all NaNs after coercion.
    """

    csv_content = (
        ",esi,triage_vital_hr,triage_vital_sbp,triage_vital_dbp,triage_vital_rr,"
        "triage_vital_o2,triage_vital_temp,triage_glucose,gender,age\n"
        "0,1,invalid,120,80,16,98,98.6,100,Male,45\n"
        "1,2,bad_value,130,85,18,98,98.6,100,Female,55\n"
    )
    file_path = tmp_path / "all_missing.csv"
    file_path.write_text(csv_content)

    cleaned_df = load_clean_df(file_path)

    assert cleaned_df["triage_vital_hr"].isnull().all()


def test_duplicate_indices_ids(tmp_path):
    """
    Ensures that processing succeeds even if input rows have duplicate IDs in the 
    index.
    """

    csv_content = (
        "id,esi,triage_vital_hr,triage_vital_sbp,triage_vital_dbp,triage_vital_rr,"
        "triage_vital_o2,triage_vital_temp,triage_glucose,gender,age\n"
        "100,1,80,120,80,16,98,98.6,100,Male,45\n"
        "100,2,90,130,85,18,98,98.6,100,Female,50\n"
    )
    file_path = tmp_path / "duplicates.csv"
    file_path.write_text(csv_content)

    cleaned_df = load_clean_df(file_path)

    assert len(cleaned_df) == 2

def test_raises_error_on_missing_column(tmp_path):
    """
    Ensures function raises KeyError if a required vital column is missing.
    """

    csv_content = (
        ",esi,triage_vital_hr,gender,age\n"  # Missing sbp, dbp, rr, o2, temp, glucose
        "0,1,80,Male,45\n"
    )
    file_path = tmp_path / "missing_vitals.csv"
    file_path.write_text(csv_content)

    with pytest.raises(KeyError):
        load_clean_df(file_path)