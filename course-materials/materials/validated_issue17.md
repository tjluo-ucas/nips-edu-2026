# Issue 17 — Validated Requirement Handoff

Distribute this handout only after learners have recorded the assumptions and
questions produced in Lab 1. It represents the product owner's validated
answers, not facts that may be inferred from the original one-sentence request.

## Validated behavior

- A negative order total is invalid for every customer and raises `ValueError`.
- A non-member receives no promotional discount.
- A member qualifies when the order total is **at least 100.00**.
- The discount is 10% of the order total, rounded to two decimal places.
- The discount may not exceed 25.00.

## Acceptance responsibility

These rules define intended behavior, but they do not prove that a candidate is
correct, secure, maintainable, or appropriate for production. Learners must
create an independent oracle, execute it, preserve evidence, and record any
remaining uncertainty.
