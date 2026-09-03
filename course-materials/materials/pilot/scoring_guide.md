# Anchored Scoring Guide

## Concept questions, 0--2 each

- **0 — incorrect:** collapses generation, reward, explanation, test evidence, or approval into one correctness signal.
- **1 — partial:** identifies one valid distinction but omits signal class, scope, environment, or accountable decision.
- **2 — complete:** classifies the signal, states the supported claim and boundary, and separates evidence, revision guidance, model opinion, and approval where relevant.

## Question-specific anchors

1. Full credit classifies the passing run as scoped evidence, reward as revision/ranking guidance, LLM review as model opinion, and architect decision as approval judgment; it states that none alone proves universal correctness.
2. Full credit keeps repository/runtime observations, hypotheses, and stakeholder-validated intent distinct.
3. Full credit explains that the oracle is derived separately from validated properties and can falsify a plausible candidate or mutation.
4. Full credit cites concrete system consequences such as state, dependency direction, configuration, security, operability, or rollback.
5. Full credit names candidate/version, properties, verifier/evidence, environment, limitations, and remaining uncertainty.

## Artifact calibration

Two scorers independently score the first two artifacts, discuss disagreements,
and record a shared interpretation before scoring the remainder. Report exact
agreement and the mean absolute score difference; do not claim inter-rater
reliability from a very small sample.

## Transfer pass

Transfer passes only when the learner:

- models authorization-specific principals, resources, grants/revocations, and precedence;
- produces executable evidence not copied from the discount cases;
- states a property-scoped conclusion with remaining uncertainty;
- separates verification from the accountable approval decision.

Score 0--4: 0 missing; 1 copied procedure with no domain model; 2 partial domain
adaptation; 3 defensible independent transfer; 4 defensible transfer plus a
novel counterexample or system-level risk.
