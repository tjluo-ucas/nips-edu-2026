# Instructor Guide: Verification-Centered Software Engineering with Coding Agents


## Course lineage and authors


> **Course lineage.** This module comes from a long-running curriculum: Advanced Software Engineering (2008-2019), followed by Intelligent Software Engineering (2019-2026). The agentic-era activities extend, rather than replace, the established emphasis on real problems, modeling, architecture, verification, creativity, and reflective engineering judgment.

This resource is derived from the **Intelligent Software Engineering** course, which evolved from the earlier **Advanced Software Engineering** teaching practice. Authors: **Chenxi Luo** and **Wei Xiang** (La Trobe University), **Moon-Kuen Mak** and **Tiejian Luo** (University of Chinese Academy of Sciences). Corresponding author: **Tiejian Luo** (`tjluo@ucas.ac.cn`).

A related published teaching-study anchor is: **Min Yao and Tiejian Luo (2024), _Practice and Reflection on the Cultivation of Creativity in Software Engineering Teaching_, Journal of Engineering Studies, 16(5)**. It documents the course team's emphasis on creativity cultivation and reflective software engineering pedagogy, which this AI-agent-era module extends.

## 1. Teaching thesis and technical scope

AI coding agents make implementation cheaper, but candidate generation is not
evidence. This workshop teaches **verification-centered software engineering**:
the engineer validates intent, bounds the agent interface, challenges a
candidate, distinguishes evidence from revision guidance, scopes a defensible
claim, and makes a separate approval decision. **Our learner—not the agent—is
the primary object of improvement.**

### Complementary to self-improving-agent courses

Research seminars such as Stanford CS329A study mechanisms that improve the
agent: test-time compute, learned verifiers, search/planning, reinforcement
learning, tool use, memory, and agent-system design. This 150-minute reusable
module addresses the complementary engineering problem created by that
progress: how to review and govern the resulting software change.

| Self-improving-agent seminar | This module |
|---|---|
| Optimize agent/model performance | Improve evidence and engineering judgment |
| Search, reward, RL, planner design | Intent, ACI bounds, independent verification |
| Benchmark score | Property-scoped claim and justified approval |
| Original agent research project | Executable labs and non-isomorphic transfer |

Deliberately out of scope: model training, RL, inference-time scaling, MCTS,
planner optimization, prompt optimization, memory systems, and meta-agents.

The pedagogical lineage is a long-running software engineering practice centered on: problem/value, use cases and user stories, business/data modeling, architecture and refactoring, interfaces, security/performance, automated verification, and Git/GitLab continuous integration. Agentic development changes the implementation stage, not the obligation to understand and verify the system.

## 2. Core loop and outer engineering frame

Core technical loop:

`I -> validate S -> (Agent + ACI, X) -> C -> V -> E/F -> R -> C' or K -> J -> approve/reject`

Three signals must remain distinct:

1. **Correctness evidence:** what property has been demonstrated?
2. **Revision guidance:** what should the agent or learner try next?
3. **Approval judgment:** should this change enter the software lifecycle?

Model explanation is recorded as opinion/rationale, not independent evidence.

The following engineering frame supplies intent before the loop and accountable
approval after it. It is context for the single concept, not a list of separate
AI methods.

1. **Problem** - Who has what problem, in what scenario, and what value would software create?
2. **Model** - What users, use cases, domain concepts, workflows, and constraints matter?
3. **Specify** - What behavior and evidence would make a change acceptable?
4. **AI Candidate** - Let an agent or prepared patch propose an implementation within a bounded task.
5. **Verify** - Run independent tests/properties/checks and strengthen them when evidence is weak.
6. **Judge** - Ask whether the change is not only functionally correct, but architecturally and operationally appropriate.
7. **Reflect/Transfer** - Identify what the AI, tests, and humans missed, then repeat on a non-isomorphic task.

## 3. Timing options

### Using the two slide PDFs

Use `slides/verifier_feedback_loops.pdf` as the concise, learner-facing 16:9
projection deck. Use the same-numbered page in
`slides/Instructor_Notes_Verification_Centered_SE.pdf` for the teaching intent,
analogy, and facilitation application behind that slide. The A4 notes are a
private preparation/teaching companion, not a second deck to project. This
pairing helps an instructor preserve the conceptual distinctions and staged
release while adapting the explanation to learners.

### 90-minute primer (not the full assessed intervention)
- 15 min - concept and independent-evidence distinction.
- 20 min - executed notebook walkthrough.
- 40 min - Labs 2-3: weak verifier, counterexample, revision.
- 15 min - scoped claims and discussion.

### 150-minute core workshop
- 10 min - briefing and pre-test.
- 15 min - scope, signal classification, technical model, and verifier independence.
- 20 min - Lab 1 and validated-requirement handoff.
- 30 min - Candidate C-017, interface checkpoint, and learner-designed verifier.
- 20 min - revision and property-scoped claim.
- 25 min - Lab 4 architecture-policy verifier.
- 22 min - Lab 5 authorization transfer.
- 8 min - post-test and friction survey.

### Half-day studio

Extend Lab 5 implementation time and add presentations and debrief.

## 4. Facilitation prompts

Use these questions repeatedly:

- What is **observed**, what is **inferred**, and what has been **validated**?
- What would falsify your claim that the patch is correct?
- What behavior is not represented in the current tests?
- If every test passes, what could still make this a bad change?
- Which tool/action should the agent not be allowed to perform?
- What evidence would convince a reviewer who did not see the prompt?
- Could you apply the same process to a different system tomorrow?

## 5. Common misconceptions

### Misconception A: "The model explained its reasoning, therefore the patch is trustworthy."
Correction: explanations are not executable evidence.

### Misconception B: "All tests pass, therefore the implementation is correct."
Correction: tests establish only the behaviors they actually exercise. The EvalPlus result is a concrete motivation for stronger test suites.

### Misconception C: "If the code is functionally correct, it is good software."
Correction: architecture, security, performance, maintainability, operability, and value remain engineering concerns.

### Misconception D: "A more autonomous agent is always a better agent."
Correction: useful autonomy depends on interfaces, permissions, feedback, and stop conditions. Bounded tools make actions inspectable and auditable.

### Misconception E: "Formal verification eliminates specification risk."
Correction: machine-checkable proof is only as meaningful as the specification. CLEVER is useful precisely because semantic specification alignment is itself challenging.

### Misconception F: "A high reward or revision score is correctness evidence."
Correction: a revision score can rank the next candidate without establishing a property. Require learners to classify the signal before acting on it.

### Misconception G: "Approval is just one more verifier output."
Correction: architecture, security, compliance, rollback, and accountable ownership require a distinct engineering decision even after named checks pass.

## 6. Instructor preparation

- Give learners Lab 1 and the scenario before releasing the validated business rule.
- After learners record assumptions and clarification questions, distribute `validated_issue17.md`.
- Give learners `exercise_repo/tests/test_visible.py` but withhold `instructor_only/test_strong.py` and `instructor_only/answer_key.md`.
- Stop the deck after “Lab 3: the weak verifier passes.” Release the remaining slides and executed notebook only after learners commit and run their own falsification cases; the full artifacts deliberately contain the worked counterexample.
- For the reproducible path, distribute Candidate C-017 in `exercise_repo/src/discount.py` together with `candidates/issue17_candidate.diff` and `candidates/issue17_provenance.yaml`. Do not describe its latent behavior.
- For a live-agent variant, start from `exercise_repo/baseline/discount.py` in a fresh branch and require a completed agent task contract. Preserve the live result even if it differs from C-017; use C-017 for the weak-oracle comparison when needed.
- Run Lab 4 against the executable `architecture_repo`; require file, import, state, and experiment evidence rather than accepting the candidate descriptions as rationale.
- Reserve `transfer_repo` for the final assessment so learners cannot rehearse its authorization policy during the discount labs.
- Ask learners to preserve artifacts rather than only report final answers.
- Run the pre-test before revealing the concepts.

## 7. Debrief structure

Finish with three columns on a whiteboard:

| Candidate generation | Verification evidence | Engineering judgment |
|---|---|---|
| What AI produced | What independently supports/refutes it | Whether the change belongs in the system |

The central learning outcome is the ability to keep these columns separate.
