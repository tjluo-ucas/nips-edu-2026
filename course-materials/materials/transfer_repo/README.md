# Transfer repository: project-document access

This repository is used only for the non-isomorphic transfer assessment. It
models authorization state rather than prices or numeric thresholds.

Run the initial learner-visible tests:

```bash
python -m pip install -r ../exercise_repo/requirements.txt
python -m pytest tests/test_visible.py -q
```

The initial tests are evidence about three examples, not proof of a complete
authorization policy. The repository intentionally does not contain a hidden
answer comment or a complete validated requirement.

`tests/test_expected_insufficiency.py` characterizes the starter when active
and revoked membership coexist. Its result exposes a missing policy decision;
only stakeholder validation can establish whether the observed behavior is a
defect and what revision is authorized.
