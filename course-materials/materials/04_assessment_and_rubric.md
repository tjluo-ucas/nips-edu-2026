# Assessment and Rubric
> **Teaching context:** This assessment operationalizes the evolution from Advanced Software Engineering (ASE, 2008-2019) to Intelligent Software Engineering (ISE, 2019-2026), with emphasis on independent evidence, creativity, and transferable engineering judgment.


## A. Pre/Post Concept Questions

Score each 0-2: 0 incorrect, 1 partial, 2 complete.

Use the question-specific anchors and scorer-calibration procedure in
`pilot/scoring_guide.md`; do not infer learning gains from uncalibrated totals.

1. Classify each signal as correctness evidence, revision guidance, model opinion, or approval judgment: a passing test run, a reward score, an LLM review, and an architect's merge decision. State what action each permits.
2. Give one example of an observed fact, an AI inference, and a validated requirement for the same feature.
3. Why might two implementations that pass identical tests deserve different merge decisions?
4. What belongs in a bounded agent task contract?
5. What is the relationship between natural-language intent, specification, implementation, and verification?

Maximum: 10.

## B. Artifact Rubric

| Dimension | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Problem/value | Missing | Feature-only | User stated | Scenario + value | Measurable value + assumptions |
| Specification | Missing | Vague | Basic acceptance | Boundary cases | Explicit oracle + traceability |
| Agent boundary | None | Prompt only | Scope stated | Tools/stops stated | Least privilege + escalation |
| Verification | None | Existing tests only | Adds tests | Strong boundary/property evidence | Multiple independent evidence types |
| Architecture judgment | None | Style comments | Local coupling | System consequences | Trade-off with justified decision |
| Evidence trace | None | Claims only | Some artifacts | Claims linked to artifacts | Reproducible evidence package |
| Reflection | None | Outcome only | Identifies AI error | Identifies AI/test/human error | Generalizes lesson to transfer task |
| Signal discipline | Collapses all signals | Names one distinction | Separates evidence from opinion | Also separates guidance from approval | Classifies signals and states their action limits |

Maximum: 32. Recommended pass: 23, with no zero in Verification, Evidence trace, or Signal discipline.

## C. Transfer Rubric

A learner reaches **independent mastery** when they can apply the loop to a new task without being told which tests or architecture risks to inspect.

Transfer pass conditions:
- produces a problem/value statement;
- creates a testable specification;
- uses or evaluates an AI candidate within explicit boundaries;
- discovers at least one insufficiency in the initial evidence;
- separates correctness evidence, revision guidance, model opinion, and accountable approval;
- makes and defends an accept/revise/reject decision;
- provides reproducible artifacts.

## D. Suggested learning analytics

Do not grade token count, number of prompts, or lines of AI-generated code. Useful measures include:

- first-pass verification rate;
- human correction rate;
- proportion of claims backed by executable or source evidence;
- signal-classification error rate;
- quality of architecture review;
- transfer score.
