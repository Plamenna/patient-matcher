from pathlib import Path

from matcher.load import EXPECTED_COLUMNS, load_documents

HEADER = "doc_id,source,doc_type,received_date,patient_name,birth_date,ahv_number,address,sex\n"


def _write_csv(tmp_path: Path, body: str) -> Path:
    path = tmp_path / "documents.csv"
    path.write_text(HEADER + body, encoding="utf-8")
    return path


def test_real_file_loads_all_rows_and_columns() -> None:
    df = load_documents()
    assert len(df) == 30
    assert list(df.columns) == EXPECTED_COLUMNS


def test_birth_date_and_ahv_are_kept_as_raw_text(tmp_path: Path) -> None:
    # "11.02.70" must not become a float; AHV dots must stay for later validation.
    path = _write_csv(tmp_path, "E003,Lab,lab_report,2025-06-21,BERNASCONI MARCO,11.02.70,756.2104.4830.19,,M\n")
    row = load_documents(path).iloc[0]
    assert row["birth_date"] == "11.02.70"
    assert row["ahv_number"] == "756.2104.4830.19"


def test_missing_values_become_empty_string(tmp_path: Path) -> None:
    path = _write_csv(tmp_path, "E002,Studio,prescription,2025-11-04,M. Bernasconi,11.02.1970,,,M\n")
    row = load_documents(path).iloc[0]
    assert row["ahv_number"] == ""
    assert row["address"] == ""


def test_name_na_is_not_treated_as_missing(tmp_path: Path) -> None:
    # A literal "NA" could be a real initial/name; only truly empty cells are missing.
    path = _write_csv(tmp_path, "E009,Src,lab_report,2025-01-01,NA,01.01.1980,,,F\n")
    assert load_documents(path).iloc[0]["patient_name"] == "NA"


def test_quoted_name_with_comma_stays_one_field(tmp_path: Path) -> None:
    path = _write_csv(tmp_path, 'E001,Src,lab_report,2025-01-01,"Bernasconi, Marco",11.02.1970,,,M\n')
    assert load_documents(path).iloc[0]["patient_name"] == "Bernasconi, Marco"
