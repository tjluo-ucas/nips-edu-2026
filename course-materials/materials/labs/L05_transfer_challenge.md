# Lab 5 - Transfer Challenge

## New problem

A research-collaboration platform controls access to project documents. Support
reports that some offboarded collaborators can still open documents through
stale membership state or previously issued share links. The security owner
asks for reliable revocation without breaking legitimate external sharing.

This task uses `transfer_repo`, a different domain with authorization,
precedence, stale state, security consequences, and audit questions. It is not
a renamed price-threshold exercise. No validated policy or step-by-step
procedure is supplied: identify the accountable stakeholders and obtain or
state the decisions that an implementation cannot safely infer.

## Your goal

Use the executable verifier feedback loop independently. Run the initial tests,
but do not treat them as a complete access-control oracle.

Produce:

- a problem/value statement and a model of principals, resources, grants,
  revocations, precedence, and relevant state transitions;
- validated decisions, explicitly unresolved questions, and acceptance examples;
- a bounded agent contract or manually prepared candidate with provenance;
- executable evidence covering policy precedence and plausible stale-state or
  bypass behavior;
- architecture, security, privacy, operability, and audit review;
- an accept/revise/reject decision with property-scoped claims and uncertainty;
- a reflection explaining which reasoning process transferred and which
  domain-specific assumptions had to be rebuilt.
- a signal-classification record showing which artifacts are evidence,
  revision guidance, model opinion, and approval judgment.

## Pass condition

The evaluator should be able to understand *why* the change is believed
acceptable without seeing the AI conversation. Merely reproducing the discount
lab's boundary tests or renaming its artifacts does not demonstrate transfer.
