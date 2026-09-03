# Exercise repository

This intentionally small repository supports the Generated-to-Verified lab.

`baseline/discount.py` is the pre-change implementation. `src/discount.py` is
Candidate C-017 after the prepared patch has been applied. The candidate's
source does not contain the validated business rule or identify any suspected
defect; learners must derive tests from the validated requirement handout.

Run learner-visible tests:

```bash
python -m pytest tests/test_visible.py -q
```

Passing this suite establishes only that the candidate is testable. Instructors
should keep `../instructor_only/test_strong.py` hidden until learners have
designed and run their own stronger tests.
