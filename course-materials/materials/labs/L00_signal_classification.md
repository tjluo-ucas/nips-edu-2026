# Lab 0 — Classify the Signal Before Acting

## Goal

Prevent a common engineering error: treating every positive signal as proof
that a candidate is correct or ready to merge.

## Scenario

An agent proposes a change to a pricing service. The team receives these
signals:

1. `pytest`: 12 tests passed.
2. A learned reward model assigns the patch `0.91`.
3. An LLM reviewer says, “The implementation looks correct.”
4. A static analyzer reports no findings in the changed files.
5. The architect rejects the patch because it introduces mutable global state.
6. The accountable reviewer approves a revised patch for deployment.

## Task

For every signal, record:

- its class: **correctness evidence**, **revision guidance**, **model
  opinion**, or **approval judgment/decision**;
- the strongest property-scoped claim it supports;
- one conclusion it does not support; and
- the next action it permits.

Use `../templates/signal_classification.md`. A signal may have more than one
use, but name its evidentiary boundary. For example, a reward score may rank
candidates without establishing a functional property.

## Deliverable and exit condition

Submit the completed table plus one sentence explaining why
`verified ≠ approved`. Exit only when another learner can identify which
signals concern candidate properties, which guide revision, and who remains
accountable for approval.
