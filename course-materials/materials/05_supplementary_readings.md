# Supplementary Reading Map and Scope Boundary

The four linked research papers in the core module remain the required
readings. The resources below help instructors position this module relative
to courses and systems that improve agent performance. They are context, not
additional learner prerequisites.

| Resource | What it contributes | Boundary for this module |
|---|---|---|
| [Stanford CS329A: Self-Improving AI Agents](https://cs329a.stanford.edu/) | Verifiers, test-time compute, planning, learning from feedback, memory, and long-horizon agents | Complementary course context. Our primary object of improvement is the engineer's evidence and approval judgment, not the agent policy. |
| [Weak Verifiers in Agentic Systems](https://arxiv.org/abs/2506.18203) | Verifiers can themselves be imperfect | Ask what validates a verifier; do not replace scoped evidence with verifier confidence. |
| [RLEF: Grounding Code LLMs in Execution Feedback](https://proceedings.mlr.press/v267/gehring25a.html) | Execution feedback can train a code model | Learning from feedback may improve generation; it does not by itself establish evidence sufficiency or authorize deployment. |
| [CodeMonkeys](https://arxiv.org/abs/2501.14723) | Test-time scaling can generate, test, and rank many repository patches | A selected candidate remains a candidate until its property claims and system consequences are independently reviewed. |
| [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499) | Longer task horizons motivate stronger controls and evidence trails | Used as motivation, not as a claim that this module trains or benchmarks autonomous long-horizon agents. |

## Explicitly out of scope

This module does not teach reinforcement learning, inference-time search,
MCTS/planner design, prompt optimization, memory systems, or meta-agents. It
teaches the lifecycle around an agent-produced candidate:

`intent → validated specification → bounded generation → verification → revision → scoped claim → engineering approval`

The organizing question is not “How do we make the agent improve itself?” but
“What evidence permits an accountable engineer to revise, claim, or approve?”
