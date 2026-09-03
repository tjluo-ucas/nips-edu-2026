# Reproducible Build

## Prerequisites

- Python 3.9 or later and pytest 8.4.2;
- Jupyter nbconvert with a Python kernel;
- Pandoc 3.x;
- TeX Live with `beamer`, `environ`, `natbib`, `wrapfig`, and the standard
  NeurIPS template dependencies. The package's `neurips_2026.sty` is included.

No model API key, network service, dataset download, or production credential
is needed for the educational examples.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
make PYTHON="$PWD/.venv/bin/python" all
```

Individual targets are `test`, `notebook`, `slides`, `paper`, and `package`.
Outputs are written under `build/` except the canonical generated paper,
slide, and notebook renderings stored beside their sources.

The `slides` target rebuilds the learner-facing PDF, HTML, and PPTX from
Markdown. `Instructor_Notes_Verification_Centered_SE.pdf` is the synchronized
26-page A4 teaching companion distributed with the source package; page *n*
corresponds to slide *n*. See `materials/slides/README.md` for their distinct
roles.

If TeX Live reports a missing package, install it explicitly, for example:

```bash
tlmgr install environ trimspaces wrapfig
```

Expected teaching behavior: learner-visible tests pass; prepared Candidate
C-017 produces one expected threshold counterexample; both architecture
candidates pass shared functional tests while an executable cache experiment
distinguishes their system behavior; transfer starter tests pass while a
characterization test exposes unresolved revocation precedence; empty pilot
data reports `NO_HUMAN_DATA`.
