# Teaching Verification-Centered Software Engineering with Coding Agents

[![Course site](https://img.shields.io/badge/course-live-096b50)](https://tjluo-ucas.github.io/nips-edu-2026/)
[![Education Track](https://img.shields.io/badge/NeurIPS%202026-Education%20Track-12251f)](https://tjluo-ucas.github.io/nips-edu-2026/)
[![Materials](https://img.shields.io/badge/materials-CC%20BY%204.0-d9f26a)](course-materials/LICENSE.md)

This repository hosts the public course site, teaching materials, runnable
examples, assessment instruments, and reproducible source for a NeurIPS 2026
Education Track resource.

**Live course site:** <https://tjluo-ucas.github.io/nips-edu-2026/>

## Educational premise

Coding agents can generate and revise patches, but generation is not a
software-engineering completion criterion. The module teaches learners to
validate intent, constrain an agent's interface, challenge a candidate with
independent evidence, revise from counterexamples, state a property-scoped
claim, and make a separate accountable approval decision.

> Our learner—not the agent—is the primary object of improvement.

```text
Intent → Validated specification → Bounded agent + environment → Candidate
       → Verifier → Evidence/counterexample → Revision → Scoped claim
       → Architecture/security/policy judgment → Approve or reject
```

Learners keep four signal classes distinct:

1. **Correctness evidence** — what named property is supported?
2. **Revision guidance** — what candidate or edit should be tried next?
3. **Model opinion** — what does the model assert or explain?
4. **Approval judgment** — should an accountable owner advance the change?

## Audience and format

- Advanced undergraduate and graduate AI/software-engineering learners.
- Prerequisites: basic Python, Git/diffs, and unit testing.
- Core format: a 150-minute workshop; 90-minute and half-day variants are
  documented in the instructor guide.
- No paid model API, external dataset, or production credential is required.

## Start here

| Resource | Purpose |
|---|---|
| [Course website](https://tjluo-ucas.github.io/nips-edu-2026/) | Concept overview, workshop route, and resource navigation |
| [Two-page paper](downloads/main.pdf) | Contribution, learner level, linked research, and teaching summary |
| [16:9 classroom deck](downloads/verifier_feedback_loops.pdf) | Learner-facing projection and staged activities |
| [A4 instructor notes](downloads/Instructor_Notes_Verification_Centered_SE.pdf) | Page-aligned teaching intent, analogy, and facilitation guidance |
| [Complete source ZIP](downloads/verification-centered-se-source-package.zip) | One-download archive of the submission source and teaching package |
| [Browsable course source](course-materials/) | Paper source, labs, code, tests, notebook, rubrics, and build tools |

### Why there are two slide PDFs

The PDFs are synchronized at 26 pages but are deliberately not
interchangeable. Page *n* of the A4 Instructor Notes explains page *n* of the
16:9 classroom deck. Teachers project the concise classroom deck and use the
notes privately to understand each slide's objective, explanatory analogy, and
classroom implementation.

## Repository map

```text
.
├── index.html, styles.css       # GitHub Pages course site
├── downloads/                   # Paper, two teaching PDFs, complete source ZIP
└── course-materials/
    ├── paper/                   # NeurIPS paper source
    ├── materials/
    │   ├── labs/                # Lab 0–5
    │   ├── notebooks/           # Executable verifier walkthrough
    │   ├── exercise_repo/       # Weak-verifier candidate exercise
    │   ├── architecture_repo/   # Functionally equal, structurally different candidates
    │   ├── transfer_repo/       # Authorization-domain transfer task
    │   ├── templates/           # Contracts, ledgers, checklists, decision records
    │   ├── pilot/               # Protocol, instruments, empty data, analysis
    │   └── instructor_only/     # Worked tests and answer key; contains spoilers
    ├── tools/                   # Validation and packaging utilities
    ├── Makefile                 # Reproducible commands
    └── BUILD.md                 # Environment and build instructions
```

## Run the executable materials

```bash
git clone https://github.com/tjluo-ucas/nips-edu-2026.git
cd nips-edu-2026/course-materials
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
make PYTHON="$PWD/.venv/bin/python" test
```

The test target validates the prepared candidate behavior, executable
architecture counterexample, authorization-transfer starter, pilot analysis,
and expected threshold counterexample. See
[`course-materials/BUILD.md`](course-materials/BUILD.md) for paper, notebook,
slide, and packaging prerequisites.

## Teaching sequence and spoiler boundary

Begin with signal classification, then validate the requirement before
revealing the prepared candidate. Stop the classroom deck after the weak
verifier passes; release worked counterexamples and `instructor_only/` only
after learners have committed their own falsification attempts. Because this
repository is public, instructors should use fresh variants for summative or
high-stakes assessment.

## Evidence and claim boundary

The package is **pilot-ready** and includes a protocol plus tested analysis
code. It contains no participant records and makes no human learning-outcome
claim. Automated repository tests demonstrate artifact behavior, not teaching
effectiveness.

## Authors

Tiejian Luo\* · Chenxi Luo · Moon-Kuen Mak · Wei Xiang<br>
La Trobe University · University of Chinese Academy of Sciences<br>
\* Corresponding author: Tiejian Luo — <tjluo@ucas.ac.cn>

## License and third-party material

Original educational materials are licensed under CC BY 4.0; original code is
MIT licensed. The official NeurIPS style file and referenced research remain
under their respective terms. See
[`course-materials/LICENSE.md`](course-materials/LICENSE.md),
[`MANIFEST.md`](course-materials/MANIFEST.md), and
[`THIRD_PARTY.md`](course-materials/THIRD_PARTY.md).
