# NOTES – Patient matcher
- what is received_date is it the date of receiving the document or is it 
- do we include all documents like prescriptions and consultations note or we filter only diagnosis 
- the address is the patient address or the address of the source not the patient. 
- is it fine if we create a list of names we are not sure that are the same because we have no sufficient evidence are the same from the data . Is this a good way.  
<!--
Fill this file in YOURSELF during minutes 0–10, before asking Claude Code for any code.
Write short bullet points, not prose. Say each point aloud while you type it: this file is
the evidence of your thinking that the interviewer will look at.
Delete these comments as you fill the sections.
-->

## 1. What I see in the data
- The patient_name needed to be clean, for some rows starting surname and then name , for some rows capitlas letters
- needed to be clean the dates of birth different formats (its the column with at least missing values , first to be used for matching)
- AVS also to be used for matching 
  
<!--
After 3–5 minutes of reading the CSV (Data Wrangler or head), write facts, not plans:
-Which columns are always filled, which are often empty (rough % is enough)?
- Which formats appear in birth_date? In patient_name (order, case, initials, brackets)?
- Anything that looks like OCR, typos, duplicates?
-->



## 2. Questions for the interviewer and my assumptions

<!--
Questions you would ask before coding. For each one, write the assumption you take
if nobody answers. Example format:
- Q: ... ? -> Assumption: ...
Aim for 3–5. Think about: missing data, conflicting data, what "same person" means,
what to do with exact duplicates, what the output must contain.
-->



## 3. Matching rules (my decisions)
  
<!--
<!The core of the exercise. Write rules in the ORDER they are checked.
Each rule: condition -> outcome (MATCH / NO_MATCH / REVIEW) + one-line reason.
Remember: a false merge is worse than a missed match. When unsure, REVIEW.
Questions to answer for yourself:
- Which field is the strongest identifier? What if it is invalid or missing?
- When do two different birth dates still mean the same person?
- When is a matching name NOT enough?
- What do you do when one document could belong to two different patients?
- Is the address evidence for a match, or only a tie-breaker?
-->

- define three status names that are matched, birth_date and patient_name are matched
1. If patient_name are the same, then check if  birth_date are the same. if yes and ahv_number is not missing and are the same, then the id_doc columns are conyaining documents for thre same patient. so the patents matched. 
2. Partially matched if the 
3. match, no missing neither patient_name neighter birth_date will be status match . At the end cross check if the ahv_number are fully matched (if not missing)
4. 
3.

## 4. Normalisation I need before comparing

<!--
What must be cleaned so the rules above can compare values?
List per field (name, birth date, AHV) the transformations, e.g. accents, case,
name order, formats, OCR characters. Note what you will NOT handle (and why).
-->

- Name: 
- Birth date:
- AHV:

## 5. Output (copied from the README, my checklist)

<!--
Rewrite the README's Output section as a checklist you tick at minute 40.
Also decide the exact JSON shape of patients.json here (a small example).
-->

- [ ]
- [ ]
- [ ]

## 6. Tests I will write first

<!--
The dangerous cases: pairs that must NOT be merged, and pairs that must go to REVIEW.
Then 2–3 cases that MUST match (variants of the same person).
Name each test as a sentence, e.g. "different valid AHV numbers never match".
-->

- [ ]
- [ ]
- [ ]

## 7. Steps (what I will ask Claude Code, one at a time)

<!--
Break the work into 4–6 steps of ~5 minutes each. Each step should end with tests passing
and a commit. Example of a good step: "Step 2: parse_birth_date() with the formats in
section 4, plus tests". Keep the last step for the output file.
-->

1. load_documents(): read data/documents.csv into  dataframe pandas
2.  normalise_name(): nameparser → extract name components, unicodedata / Unidecode → normalize accents and characters.
3.  compare_name () : RapidFuzz compare spelling variations return the score of comparison as a list of the names and score 
4.  matched_patients(): use Splink to create the matched and save in one file json with the id of the patient created by you , id_documents : all of the id_doc  that the patient has in one line separated by coma 



## 8. At the end: what is done, what is left

<!--
Minutes 40–45. Be honest:
- Which rules are implemented and tested?
- What did you leave out, and what would you do next with one more hour?
- How would this work with 1 million documents instead of 30?
-->

-
