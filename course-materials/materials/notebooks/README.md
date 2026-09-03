# Verification-centered executable notebook

`verifier_feedback_loop.ipynb` is a no-API-key interactive walkthrough of
candidate verification, counterexample-driven revision, and claim calibration.
It reads Candidate C-017 from the packaged exercise repository but does not
modify it. The notebook explicitly stops before accountable engineering
approval, which is exercised in the architecture and transfer labs.

Run from the package root:

```bash
jupyter nbconvert \
  --to notebook \
  --execute materials/notebooks/verifier_feedback_loop.ipynb \
  --output verifier_feedback_loop.executed.ipynb
```

The reproducible build executes the notebook and also produces a standalone
HTML rendering for learners without Jupyter.
