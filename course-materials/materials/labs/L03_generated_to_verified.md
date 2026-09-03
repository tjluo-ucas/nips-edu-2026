# Lab 3 - Strengthen the Oracle

## Starting point

Prepared Candidate C-017 passes all learner-visible tests. Its implementation
contains no comment or docstring identifying a suspected defect.

## Challenge

Assume you do not trust that the current tests adequately represent the requirement.

1. Identify equivalence classes and boundaries for order totals and customer status.
2. Add at least four tests that would falsify plausible incorrect implementations.
3. Ask: What mutation of the implementation would still pass the old tests?
4. After you have designed and executed your stronger tests, request the instructor's withheld suite and compare it with yours.
5. Repair the candidate if a stronger test exposes a defect.

## Deliverables

- added tests;
- failing evidence (if any);
- final passing evidence;
- one paragraph: "What did the original test suite fail to establish?"

## Concept link

This lab operationalizes the EvalPlus lesson: weak test suites can overestimate
generated-code correctness. A failing counterexample is correctness evidence
against a candidate and can also guide revision; the repaired candidate still
requires a scoped claim rather than a universal “correct” label.
