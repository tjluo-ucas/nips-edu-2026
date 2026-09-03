# Lab 2 - Candidate Generation Is Not Acceptance

## Objective

Produce or inspect a candidate patch for the discount function without treating
its provenance, explanation, or visible test result as acceptance evidence.
Agent self-evaluation and reward scores may guide another revision, but they
do not replace an independently justified oracle.

Before beginning, obtain `validated_issue17.md` from the instructor. Acceptance
examples written in Lab 1 must be updated when the validated answers differ
from learner assumptions.

## Delivery mode A — reproducible prepared candidate

Candidate C-017 is already present in `exercise_repo/src/discount.py`. Its
pre-change source, exact diff, and transparent provenance are provided in:

- `exercise_repo/baseline/discount.py`;
- `candidates/issue17_candidate.diff`;
- `candidates/issue17_provenance.yaml`.

Do not consult `instructor_only/` before completing your independent test
design.

## Delivery mode B — live coding agent

Work in a fresh copy or branch whose `src/discount.py` contains the baseline.
Complete `templates/agent_task_contract.yaml`; require the agent to implement
the validated requirement, remain within the exercise repository, preserve the
public API, and run learner-visible tests. Preserve the prompt, diff, commands,
tool results, model/tool version, and unresolved questions.

A live candidate may be correct or incorrect. If it does not expose the weak
oracle during the workshop, retain it as comparative evidence and use prepared
Candidate C-017 for Lab 3. Do not alter C-017 to manufacture a failure.

## Learner tasks

1. Record the candidate ID, provenance, and exact diff.
2. Record which commands and tests were actually executed.
3. Mark the change as one of: `generated`, `candidate`, `verified`, `approved`.
4. Explain why the current evidence is or is not sufficient.
5. Record each claim as observed, inferred, or validated.
6. Classify every recorded result using the Lab 0 signal categories.

## Important

Do not inspect the instructor-only stronger tests during this lab.

## Agent-interface checkpoint

Hold the issue, repository, and prepared candidate fixed. Compare these two
ways of exposing the task to an agent:

- **Unrestricted shell:** arbitrary commands, full raw output, no path boundary,
  and no explicit stop or escalation rule.
- **Bounded contract:** the supplied `templates/agent_task_contract.yaml`, with
  named actions, concise observations, forbidden operations, verification
  feedback, stop conditions, and human-approval gates.

Record which actions and observations differ, one failure each design can
induce, and why this comparison concerns the interface rather than model
quality. Complete the bounded contract for Candidate C-017 before continuing.
