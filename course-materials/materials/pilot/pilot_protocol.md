# Formative Pilot Protocol

## Purpose

Evaluate whether the resource teaches one technical concept: a
verification-centered lifecycle in which engineers classify signals, revise
candidates, make property-scoped claims, and decide approval.

## Research questions

1. Can learners distinguish correctness evidence, revision guidance, model opinion, and approval judgment?
2. Can learners expose an inadequate verifier before seeing the instructor suite?
3. Can learners distinguish property-scoped verification from approval?
4. Can learners transfer the loop from pricing to document authorization?
5. Which instructions, setup steps, or artifacts create avoidable friction?

## Participants

- Target: 6--12 advanced undergraduate or graduate learners.
- Prerequisites: basic Python, Git/diffs, and unit testing.
- Record prior coding-agent experience only as `none`, `some`, or `frequent`.
- Participation should not affect course grades unless separately approved and disclosed.

## Ethics and data protection

- Use random participant IDs; collect no names, email addresses, prompts containing personal data, or API keys.
- Explain that participation and survey responses are voluntary.
- Store the linkage between participant and ID nowhere in this package.
- Report aggregates; suppress free text that could identify a participant.
- Obtain institutional ethics/IRB review before treating the activity as human-subjects research or publishing research claims. A local teaching-quality exercise does not automatically authorize research use.

## 150-minute session

| Time | Activity | Evidence captured |
|---:|---|---|
| 0--10 | Consent/briefing and pre-test | five concept scores |
| 10--25 | Signal classification, technical model, and verifier independence; deck only through the weak-verifier prompt | classification record and notes |
| 25--45 | Lab 1 and requirement handoff | assumptions and evidence ledger |
| 45--75 | Candidate C-017 and learner-designed verifier | first counterexample time |
| 75--95 | Revision and property-scoped claim | test log and claim |
| 95--120 | Executable architecture comparison | decision record |
| 120--142 | Authorization transfer | transfer artifacts |
| 142--150 | Post-test and friction survey | scores and feedback |

Do not release the complete deck, executed notebook, or `instructor_only/`
before each learner has committed their own stronger tests. The complete deck
and notebook are post-attempt explanations and contain the exact counterexample.
Do not coach learners toward the threshold or revocation precedence after the
validated handoff.

## Primary measures

- concept score gain, total 0--10;
- signal-classification score and error types;
- independent defect discovery before instructor-suite release;
- evidence-trace score, 0--4;
- architecture-judgment score, 0--4;
- transfer score, 0--4, and transfer pass;
- completion time and setup/friction incidents.

## Reporting rules

- Report participant count and missing fields.
- Label this a formative pilot; do not make causal learning claims without an appropriate design.
- Report failures and withdrawals, not only successful learners.
- Keep automated repository test results separate from human learning outcomes.
- If fewer than six learners complete, present individual-case observations and avoid unstable percentages.
