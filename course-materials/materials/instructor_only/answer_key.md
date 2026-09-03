# Instructor Answer Key

## Lab 0

- A passing test run is correctness evidence only for the named candidate,
  cases/properties, environment, and oracle.
- A learned reward score is normally revision or ranking guidance; its numeric
  precision does not turn it into a verified property.
- An LLM review is model opinion unless independently grounded evidence is
  supplied and checked.
- A static-analysis no-finding is scoped correctness/security evidence for the
  configured rules, files, and tool version, not proof of no defect.
- An architect's rejection is an approval judgment based on system
  consequences. Accountable approval remains a decision, not another test.

The expected explanation is: verification supports bounded property claims;
approval additionally considers architecture, security, policy, operations,
and accountable authority.

## Lab 1
A strong solution explicitly asks whether the threshold is inclusive, distinguishes member status, captures invalid negative totals, and does not assume unspecified behavior without marking it as an assumption.

## Lab 2
Visible tests passing promotes the patch only to **candidate**, not verified.

## Lab 3
The key withheld case is exactly 100.00 for a member. The deliberately defective implementation uses `>` rather than `>=`. Learners should ideally invent this boundary independently.

## Lab 4
Candidate B is preferable even though both pass the shared functional tests.
Repository evidence shows that Candidate A creates mutable process-global state,
reads environment configuration inside the domain function, duplicates input
validation, and can return a stale cached result after configuration changes.
Candidate B uses the policy and validation boundaries and remains deterministic
for explicit inputs. Both may support the narrow claim “the shared examples
pass under default configuration”; only B should normally be approved under the
documented architecture constraints.

## Transfer
Reward process transfer and evidence quality, not similarity to an instructor
implementation. Strong work recognizes that revocation precedence, stale
membership, share-link invalidation, cache/session behavior, audit evidence,
and stakeholder authority require explicit decisions. Do not require one
universal policy; require a validated policy, tests that would falsify it, and
a decision whose scope and uncertainty are explicit.
