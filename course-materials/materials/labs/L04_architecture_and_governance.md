# Lab 4 - Correct Code Can Still Be a Bad Change

## Case

`architecture_repo` contains two candidate implementations of the same
validated behavior:

- `src/pricing/candidate_a.py`;
- `src/pricing/candidate_b.py`.

Do not accept the candidate names or descriptions as evidence. Read
`architecture_context.md`, inspect imports and state, and run the shared suite:

```bash
cd architecture_repo
python -m pytest tests/test_functional_equivalence.py -q
```

Both implementations should pass these functional tests. That result is the
starting observation, not the merge decision.

## Tasks

1. Draw the dependency boundary for each implementation using file and import evidence.
2. Identify mutable state, configuration access, duplicated policy, test-isolation, security, and operability consequences.
3. Add at least one executable architecture check or deterministic experiment that distinguishes the candidates without changing the functional oracle.
4. State exactly which properties the shared tests verify and which they do not.
5. Decide whether each candidate deserves a property-scoped `verified` claim.
6. Decide which, if either, should be `approved` for merge and record the rationale in `templates/decision_record.md`.
7. Rewrite the agent task contract so the rejected risks are less likely.

## Discussion

A test suite answers only the questions encoded in the suite. Software
engineering judgment decides which additional questions matter. Conclusions
must cite repository evidence rather than the original case narrative. Keep
the decision boundary explicit: verification supports named properties;
architecture, security, policy, and operational evidence inform the accountable
approval judgment.
