from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "documents.csv"

EXPECTED_COLUMNS = [
    "doc_id",
    "source",
    "doc_type",
    "received_date",
    "patient_name",
    "birth_date",
    "ahv_number",
    "address",
    "sex",
]


def load_documents(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load documents as raw text so no value is changed before our own normalisation.

    Everything is read as str: pandas would otherwise turn "11.02.70" into a float
    or "NA" into NaN. Missing cells become "" so later functions handle one kind of empty.
    """
    df = pd.read_csv(path, dtype=str, keep_default_na=False, encoding="utf-8")
    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"documents.csv is missing columns: {sorted(missing)}")
    return df[EXPECTED_COLUMNS]
