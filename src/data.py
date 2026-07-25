import pandas as pd
import numpy as np

def load_clean_df(path):


    df_raw = pd.read_csv(path, index_col=0)

    VITALS = ["triage_vital_hr", "triage_vital_sbp", "triage_vital_dbp", "triage_vital_rr",
          "triage_vital_o2", "triage_vital_temp", "triage_glucose"]
    df = df_raw.copy()

    # drop any stray index column (e.g. "Unnamed: 0") that pandas adds — it is not real data
    df = df.drop(columns=[c for c in df.columns if c.startswith("Unnamed")], errors="ignore")

    # force the vitals to be NUMBERS; unparseable text (e.g. "120bpm") becomes NaN
    for col in VITALS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # the ESI label must be 1-5. Drop rows where it is missing or out of range 
    # this is important since a row with no valid triage label cannot teach a triage model.
    df["esi"] = pd.to_numeric(df["esi"], errors="coerce")
    df = df[df["esi"].isin([1, 2, 3, 4, 5])].copy()

    # blank out physically impossible vitals so they don't poison the model
    df.loc[(df["triage_vital_temp"] < 90) | (df["triage_vital_temp"] > 110), "triage_vital_temp"] = np.nan
    df.loc[df["triage_vital_o2"] > 100, "triage_vital_o2"] = np.nan

    # encode gender to 0/1 (handles odd casings like "m" / "MALE")
    df["gender"] = df["gender"].astype(str).str.strip().str.lower().map(
        {"male": 0, "m": 0, "female": 1, "f": 1})

    # fill remaining missing NUMBERS with the column median (simple and defensible)
    for col in VITALS + ["age", "gender"]:
        df[col] = df[col].fillna(df[col].median())

    df["esi"] = df["esi"].astype(int)

    return df

