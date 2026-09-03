# Learner Guide: Verification-Centered Software Engineering with Coding Agents

## The central idea


> **Course lineage.** This module comes from a long-running curriculum: Advanced Software Engineering (2008-2019), followed by Intelligent Software Engineering (2019-2026). The agentic-era activities extend, rather than replace, the established emphasis on real problems, modeling, architecture, verification, creativity, and reflective engineering judgment.

The lifecycle in this module is:

`I -> validate S -> (Agent + ACI, X) -> C -> V -> E/F -> R -> C' or K -> J -> approve/reject`

Here `I` is stakeholder intent, `S` the validated specification, `X` the
environment, `C` a candidate, `V` an independent verifier, `E/F` evidence or a
counterexample, `R` revision guidance, `K` a scoped claim, and `J` accountable
engineering judgment. A passing verifier supports only the properties it checks.

## Three signals

- **Correctness evidence:** what property is supported by an independent check?
- **Revision guidance:** what candidate or edit should be tried next?
- **Approval judgment:** should the change proceed given architecture, security,
  policy, rollback, and accountability?

An agent explanation is model opinion. It may help investigation but is not an
independent oracle. More search can improve a candidate; it does not define the
evidence required to accept it.

This is not a model-training, RL, planner, search-scaling, or prompt-optimization
module. The agent is fixed or bounded so that you can improve the evidence and
decision.

When code generation becomes cheap, the scarce work moves toward:

- understanding the problem and value;
- specifying intended behavior;
- constraining agent actions;
- designing evidence;
- understanding system consequences;
- deciding whether a change should be accepted.

## Four states

`generated -> candidate -> verified -> approved`

- **Generated:** an AI or human produced something.
- **Candidate:** it is sufficiently concrete to evaluate.
- **Verified:** independent evidence supports the required properties.
- **Approved:** an accountable human/process accepts the change for the next lifecycle step.

Never collapse these states into `generated -> merged`.

## Three distinctions

1. `Evidence != revision guidance != model opinion != approval`
2. `Observed fact != AI inference != validated requirement`
3. `Tests pass != sufficient evidence`
4. `Functionally correct != architecturally appropriate`

## Your workflow

### Problem
Describe user, scenario, pain, desired outcome, and measurable value.

### Model
Write a user story/use case and identify the domain concepts and constraints.

### Specify
Create acceptance examples and a verification plan before asking an agent to implement.

### AI Candidate
Use an explicit task boundary: objective, scope, allowed tools, forbidden actions, acceptance criteria, stop conditions.

### Verify
Use tests, properties, static checks, security checks, performance checks, or stronger formal mechanisms as appropriate.

### Judge
Ask: Is the evidence sufficient? Is the architecture appropriate? What remains uncertain?

### Transfer
Repeat on a different problem without procedural hints.
