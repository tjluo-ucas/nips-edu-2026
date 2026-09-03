# Course Materials Source

This directory contains the browsable, reproducible source for
**Teaching Verification-Centered Software Engineering with Coding Agents**.
For the course overview and direct PDF downloads, start at the
[repository README](../README.md) or the
[live course site](https://tjluo-ucas.github.io/nips-edu-2026/).

## Source contents

- `paper/` — two-page paper source and official style file;
- `materials/labs/` — Lab 0 signal classification through Lab 5 transfer;
- `materials/notebooks/` — executable, no-API-key walkthrough;
- `materials/exercise_repo/` — weak-verifier candidate exercise;
- `materials/architecture_repo/` — executable architecture counterexample;
- `materials/transfer_repo/` — document-authorization transfer task;
- `materials/templates/` — task contract, evidence ledger, verification
  checklist, signal record, and decision record;
- `materials/pilot/` — formative protocol, instruments, empty dataset, and
  tested analysis;
- `tools/` and `Makefile` — validation and packaging automation.

## Quick verification

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
make PYTHON="$PWD/.venv/bin/python" test
```

See [`BUILD.md`](BUILD.md) for the complete environment and build procedure.
The public `instructor_only/` directory contains spoilers and must be withheld
during a live formative attempt.
