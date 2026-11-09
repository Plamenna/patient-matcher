# Exercise P2, attempt 2: Patient matcher (new data)

Time limit: 45 minutes, plus 10 minutes of follow-up questions.
AI tools allowed. Record yourself (Cmd + Shift + 5, save to this folder), think aloud, commit after each step.

## Context

HealthX builds one profile per patient from documents sent by labs, hospitals, GP practices and pharmacies. Before facts can be merged, every document must be linked to the right person.

The documents rarely share an identifier. Names are written in different orders and cases, with accents or without, abbreviated, misread by OCR, or changed after marriage. Dates come in several formats. The Swiss social security number (AHV) is sometimes present, sometimes not.

In healthcare the two possible errors are not equal:

- **False merge**: two different people put into one profile. A doctor may see another person's diagnosis or medication. This is dangerous.
- **Missed match**: one person split into two profiles. Information is incomplete, which is bad but visible.

## Input

`data/documents.csv`: 30 document headers, already extracted from the documents. Same columns as before:

| Column | Notes |
| --- | --- |
| `doc_id` | unique per document |
| `source` | who sent it |
| `doc_type` | lab_report, discharge_summary, referral_letter, prescription, consultation_note |
| `received_date` | ISO date |
| `patient_name` | as written on the document |
| `birth_date` | as written; may be empty |
| `ahv_number` | Swiss AHV number as written; may be empty |
| `address` | as written; may be empty |
| `sex` | M / F |

## Task

Write Python that assigns every document to a patient.

## Output (in `output/`, never in `data/`)

1. **`output/patients.json`**: one entry per patient, with at least a `patient_id`, the `doc_ids` linked to it, and the name(s) and birth date you decided on.
2. **For every document**: its `patient_id`, plus *why* it was linked (which fields matched, or a score).
3. **A review list, built by the code**: documents or pairs where the decision is uncertain or the data conflicts, each with a reason.

## Deliverables

1. Code, with the matching logic in functions that can be tested.
2. Tests, starting with the cases where a false merge could happen.
3. The output files.
4. `NOTES.md`: filled in before you code, updated at the end.

## Domain note

An AHV number has the form `756.XXXX.XXXX.XX`. The last digit is a check digit calculated with the EAN-13 algorithm over the first 12 digits.

## How to work this time

1. **Before the timer** (setup, not counted): `uv sync`, check `uv run pytest` runs, `git init`, start the recording.
2. **Minutes 0–10**: read the data, fill in `NOTES.md` yourself (questions, rules, outputs, tests, steps). Think aloud. Send me your questions.
3. **Minutes 10–40**: ask Claude Code to implement one step of `NOTES.md` at a time. Read each diff, run the tests, commit.
4. **Minutes 40–45**: check the output against the Output section above, update `NOTES.md` with what is left.

Do not open `../P2/reference_solution` or any answer key during the exercise.
