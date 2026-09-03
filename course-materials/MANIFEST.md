# Submission Manifest and Originality Statement

- Concept: verification-centered software engineering with coding agents,
  separating correctness evidence, revision guidance, and approval judgment.
- Paper: two-page Education Track PDF and source.
- Audience: advanced undergraduate and graduate learners with basic Python,
  Git/diff, and unit-testing knowledge.
- Human pilot status: protocol-ready; no participant results claimed.

| Artifact | Role | License |
|---|---|---|
| `materials/slides/verifier_feedback_loops.pdf` | 26-slide learner-facing projection deck | CC BY 4.0 |
| `materials/slides/Instructor_Notes_Verification_Centered_SE.pdf` | 26-page, slide-aligned instructor companion | CC BY 4.0 |
| `materials/slides/` | HTML/PPTX deck, Markdown source, notes, and styling | CC BY 4.0 |
| `materials/notebooks/` | Executable interactive explanation | CC BY 4.0 + MIT code |
| `materials/labs/` | Six staged learning activities (Lab 0--5) | CC BY 4.0 |
| `materials/labs/L00_signal_classification.md` | Signal-classification checkpoint | CC BY 4.0 |
| `materials/05_supplementary_readings.md` | Instructor reading map and scope boundary | CC BY 4.0 |
| `materials/exercise_repo/` | Weak-verifier candidate exercise | MIT |
| `materials/architecture_repo/` | Executable architecture comparison | MIT |
| `materials/transfer_repo/` | Authorization transfer task | MIT |
| `materials/candidates/` | Candidate diff and provenance | MIT / CC BY 4.0 metadata |
| `materials/templates/` | Agent, evidence, verification, and decision templates | CC BY 4.0 |
| `materials/templates/signal_classification.md` | Signal classification record | CC BY 4.0 |
| `materials/pilot/` | Pilot protocol, instruments, and analysis | CC BY 4.0 + MIT code |
| `materials/instructor_only/` | Spoiler tests and notes | CC BY 4.0 + MIT code |

The two slide PDFs are complementary and not interchangeable: page *n* of the
A4 Instructor Notes explains the teaching purpose, analogy, and implementation
of page *n* in the 16:9 learner-facing projection deck. Instructors project the
first and use the second to prepare and facilitate the lesson accurately.

Generated artifacts include `paper/main.pdf`, slide HTML/PDF/PPTX, instructor-notes PDF, notebook HTML,
release ZIP files, and checksums. `paper/neurips_2026.sty` is the official
conference template and excluded from the originality claim.

Generated release ZIPs exclude local reference-paper PDFs, obsolete nested
archives, build caches, and operating-system metadata. The staged learner ZIP
also excludes the worked Slides/Notebook, validated handoff, facilitation map,
pilot data, and instructor-only answers; instructors release these at the
points specified in `materials/README.md`.

No learner data, identifiers, API keys, model credentials, or claimed
human-subject results are included. `pilot_data.csv` contains only a header.
