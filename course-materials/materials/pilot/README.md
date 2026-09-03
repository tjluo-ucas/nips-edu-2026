# Small-Pilot Kit

Status: **protocol and instruments ready; no human-participant results are
claimed in this package**.

This kit supports a 6--12 learner formative pilot of the 150-minute workshop.
It tests whether learners can classify signals and transfer the
verification--revision--approval lifecycle, while exposing usability problems
before submission or classroom adoption.

## Files

- `pilot_protocol.md` — research questions, session sequence, safeguards, and reporting rules;
- `instruments.md` — pre-test, post-test, learner friction survey, and facilitator observations;
- `scoring_guide.md` — anchored 0--2 concept-question scoring and transfer decision rules;
- `data_dictionary.md` — anonymous fields and allowed values;
- `pilot_data.csv` — header-only data sheet; no fabricated participants;
- `analyze_pilot.py` — standard-library analysis that emits JSON and Markdown;
- `test_analyze_pilot.py` — synthetic unit test for the analysis logic.

## Run analysis

```bash
python materials/pilot/analyze_pilot.py \
  materials/pilot/pilot_data.csv \
  --json build/pilot-summary.json \
  --markdown build/pilot-summary.md
```

Do not insert invented rows to make the paper appear evaluated. If no pilot can
be completed, report the package as pilot-ready and present only automated
artifact validation.
