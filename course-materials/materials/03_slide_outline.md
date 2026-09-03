# Instructor Facilitation Map

The learner-facing deck is `slides/verifier_feedback_loops.pdf`; its
page-aligned teaching companion is
`slides/Instructor_Notes_Verification_Centered_SE.pdf`. The former controls
projection and staged disclosure; the latter explains each slide's purpose,
analogy, and classroom application. HTML and Markdown versions are in the same
directory. This compact map supports shortening or reordering the deck.

1. **Title and differentiation:** improve the engineering decision, not the agent.
2. **Why now and scope:** longer agent tasks; training/RL/search optimization are out of scope.
3. **Signal model:** evidence != revision guidance != model opinion != approval.
4. **Full lifecycle:** `I -> S -> Agent+ACI -> C -> V -> E/F -> R/K -> J`.
5. **State model:** generated -> candidate -> property-scoped verified -> approved.
6. **Independence:** model explanation is not a verifier oracle.
7. **Weak verifier demonstration:** Candidate C-017 passes visible tests.
8. **Counterexample:** the exact threshold is untested.
9. **Revision:** local change followed by full verifier rerun.
10. **Claim calibration:** name properties, environment, and residual risks.
11. **Architecture judgment:** functionally equivalent candidates can differ structurally.
12. **Specification risk:** a strong verifier cannot repair wrong intent.
13. **Bounded-agent contract:** actions, observations, guardrails, and escalation.
14. **Research links:** four failure surfaces plus the module's fifth approval layer.
15. **Assessment:** epistemic calibration, artifacts, and authorization transfer.
16. **Takeaway:** evidence scopes the claim; accountable judgment approves or rejects.
