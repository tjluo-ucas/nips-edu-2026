# Teaching Verification-Centered Software Engineering with Coding Agents
## NeurIPS 2026 Education Track teaching materials

This package teaches one bounded technical concept: **verification-centered software engineering** for coding agents:

`Intent -> Validated Specification -> Agent+ACI+Environment -> Candidate -> Verifier -> Evidence/Counterexample -> Revision -> Scoped Claim -> Engineering Approval`

The primary object of improvement is the learner's evidence and judgment, not
the agent. Correctness evidence, revision guidance, model opinion, and approval
are explicitly classified rather than collapsed into one feedback signal.

The materials are designed for advanced undergraduate or graduate learners with basic programming, Git, APIs, and unit-testing experience. They are tool-agnostic: learners may use any coding agent, or instructors may provide candidate patches directly.


## Teaching lineage

The resource is an AI-agent-era evolution of a sustained software engineering teaching practice:

- **Advanced Software Engineering (ASE), 2008-2019** - problem/value understanding, requirements, modeling, architecture, verification, and project-based engineering.
- **Intelligent Software Engineering (ISE), 2019-2026** - extends that foundation with intelligent software, AI-assisted engineering, agent-mediated implementation, independent verification, and engineering judgment.

This lineage is complemented by published teaching research: Min Yao and Tiejian Luo, *Practice and Reflection on the Cultivation of Creativity in Software Engineering Teaching*, Journal of Engineering Studies, 16(5), 2024.

**Authors:** Tiejian Luo (University of Chinese Academy of Sciences), Chenxi Luo (La Trobe University), Moon-Kuen Mak (University of Chinese Academy of Sciences), and Wei Xiang (La Trobe University). **Corresponding author:** Tiejian Luo (`tjluo@ucas.ac.cn`).

## Suggested formats

- 90-minute primer: slides + notebook + Labs 2-3; does not assess transfer.
- 150-minute core workshop: Labs 1-5 + pre/post assessment, with a compact transfer segment.
- Half-day studio: Labs 1-5 with extended transfer implementation, presentations, and debrief.

## Files

- `01_instructor_guide.md` - teaching narrative, timing, facilitation and misconceptions.
- `02_learner_guide.md` - concise concept handout.
- `slides/` - synchronized learner-facing PDF deck and A4 instructor notes,
  plus editable PPTX, self-contained HTML, Markdown source, and styling. The two
  PDFs are complementary; see `slides/README.md`.
- `03_slide_outline.md` - compact facilitation map retained for instructors.
- `notebooks/` - executed verifier-loop notebook and standalone HTML rendering.
- `04_assessment_and_rubric.md` - pre/post questions, signal/evidence rubric, transfer rubric.
- `05_supplementary_readings.md` - complementary agent research and explicit scope boundary.
- `labs/` - six learner activities (Lab 0--5).
- `validated_issue17.md` - requirement-owner answers released after Lab 1 assumptions are recorded.
- `candidates/` - exact prepared candidate diff and transparent provenance.
- `exercise_repo/` - baseline and prepared Candidate C-017 for weak-vs-strong verification.
- `architecture_repo/` - two executable, functionally equivalent candidates for architecture judgment.
- `transfer_repo/` - non-isomorphic document-authorization assessment repository.
- `instructor_only/` - stronger tests and teaching notes that should be withheld during the learner phase.
- `templates/` - agent task contract, evidence ledger, verification checklist, and decision record.
- `pilot/` - protocol, instruments, scoring anchors, empty data template, and tested analysis script.

## Core rule

An AI-generated change starts as **candidate**, not **verified**. Only independent evidence and human judgment may promote the state:

`generated -> candidate -> verified -> approved`

## Recommended evidence collected from learners

1. Problem statement and intended user value.
2. User story/use case and acceptance criteria.
3. Agent task contract or candidate patch provenance.
4. Test/verification evidence.
5. Architecture/security review notes.
6. Final accept/revise/reject decision with rationale.
7. Transfer performance on a new task.

## Controlled release sequence

1. Use `L00_signal_classification.md` to establish the evidence/guidance/opinion/approval distinction.
2. Give learners Lab 1 and the scenario, but not the validated handoff.
3. After assumptions and questions are recorded, release `validated_issue17.md`.
4. Use a live agent in a fresh baseline branch or distribute prepared Candidate C-017 with its provenance.
5. Present the formal deck only through “Lab 3: the weak verifier passes,” then pause. Do not distribute the complete deck or notebook before learners commit their own falsification cases; both contain the worked counterexample.
6. Withhold `instructor_only/` until learners have executed their own stronger oracle.
7. Use `architecture_repo/` for evidence-backed architecture judgment.
8. Use `transfer_repo/` only for the final non-isomorphic assessment.

`instructor_only/` is a spoiler boundary, not a security control. Because the
accepted resource will be public, use fresh instructor-authored variants for
summative/high-stakes assessment. The bundled suite supports reproducible
formative teaching.

## License / originality

These materials were created specifically for the NeurIPS 2026 Education Track
submission. Educational content is CC BY 4.0 and code is MIT licensed. See
`../LICENSE.md`, `../MANIFEST.md`, and `../THIRD_PARTY.md`.
