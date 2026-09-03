# Architecture comparison repository

This repository contains two implementations of the same validated discount
behavior. Both pass the same functional test suite. They differ in dependency
direction, state, configuration access, and test isolation.

Run the shared functional tests:

```bash
python -m pip install -r ../exercise_repo/requirements.txt
python -m pytest tests/test_functional_equivalence.py -q
```

Then run `tests/test_teaching_counterexample.py` to reproduce the stale-cache
experiment. It supplies executable architecture evidence; it does not make the
merge decision automatically.

The functional suite is evidence about returned values and errors only. It is
not an architecture, security, operability, or approval oracle.
