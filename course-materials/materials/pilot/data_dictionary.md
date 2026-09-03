# Pilot Data Dictionary

| Field | Type / allowed values | Meaning |
|---|---|---|
| participant_id | anonymous string | Random ID with no identity mapping in package |
| agent_experience | none, some, frequent | Prior coding-agent experience |
| pre_score | integer 0--10 | Form A concept score |
| post_score | integer 0--10 | Form B concept score |
| discovered_before_release | 0 or 1 | Learner produced a failing independent case before hidden-suite release |
| evidence_trace_score | integer 0--4 | Artifact rubric score |
| architecture_score | integer 0--4 | Evidence-backed architecture judgment |
| transfer_score | integer 0--4 | Non-isomorphic transfer score |
| transfer_pass | 0 or 1 | Meets every transfer pass condition |
| completion_minutes | positive number | Time through post-test or withdrawal |
| completed | 0 or 1 | Completed full protocol |
| setup_incidents | non-negative integer | Count of setup interventions |

Free-text responses are stored separately only when consent and de-identification
allow it. Do not place names, emails, raw prompts, or secrets in the CSV.
