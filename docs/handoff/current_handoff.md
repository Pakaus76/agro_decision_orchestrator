# GLOBAL HANDOFF DOCUMENT ACTUALIZADO — Agro Decision Orchestrator

## 1. Purpose of this handoff

This handoff is designed so that the next LLM can continue the Agro Decision Orchestrator project immediately and without asking unnecessary clarification questions.

The next LLM must be able to understand:
- what Agro-DO is,
- what has already been implemented,
- what has already been validated,
- which project rules are fixed,
- what must not be changed,
- what the current refinement frontier is,
- and what the single correct next step is.

This document is intentionally operational, not decorative.

---

## 2. What Agro-DO is

Agro-DO (Agro Decision Orchestrator) is a product-oriented, governed decision-support service for greenhouse operations.

It is being developed as a real service concept for protected horticulture environments, not as a thesis-only artifact and not as an A/B/C/F-style scientific comparison product.

The product combines:
- structured greenhouse context,
- normalized operational cases,
- a validated bridge payload,
- a deterministic fallback path,
- a generative orchestration layer using OpenAI,
- and explicit policy guardrails.

The goal is to support better operational decisions in situations related to:
- irrigation continuity,
- climate correction,
- equipment health,
- sensor trust,
- degraded visibility,
- and state mismatch between digital representation and physical reality.

---

## 3. Non-negotiable decisions already fixed

The next LLM must not reopen these decisions.

### 3.1 Product direction
Agro-DO is one product-oriented service, not a sequence of competing scientific versions.

### 3.2 Generative AI
Generative AI is a mandatory part of the target architecture.

### 3.3 Deterministic logic
The deterministic path exists as:
- fallback,
- resilience,
- inspection baseline.

It is not the target identity of the product.

### 3.4 Repository language rules
- Conversation with the project manager: Spanish
- Repository files: English
- Code comments: English
- Structured technical documentation inside files: English

### 3.5 Documentation update discipline
The four core markdown files are:
- `README.md`
- `docs/project_log.md`
- `docs/lessons_learned.md`
- `docs/handoff/current_handoff.md`

Required update order:
1. `docs/project_log.md`
2. `README.md`
3. `docs/lessons_learned.md` when applicable
4. `docs/handoff/current_handoff.md`
5. Git commit and GitHub push

### 3.6 Anti-overwrite safeguard
`docs/project_log.md` and `docs/lessons_learned.md` are cumulative memory files.

They must:
- be treated as append-only by default,
- never be replaced by short summary rewrites,
- always be checked for previous entries before update.

Before editing either file:
- inspect the last visible `LOG-*` entry,
- inspect the last visible `LESSON-*` entry,
- verify that prior entries still exist,
- and assume that any much shorter replacement is wrong unless explicitly requested by the project manager.

### 3.7 File-edit instruction rule
Whenever text is provided for a file, the instruction must explicitly say one of these:
- replace the full file content,
- append this block to the current file,
- insert this block in a specific section.

This is mandatory.

---

## 4. Current repository reality

The project is already in GitHub and the repository is working.

### 4.1 Implemented structural layers
Implemented and already used:
- `src/agro_do/domain/models.py`
- `src/agro_do/domain/decision_case.py`
- `src/agro_do/domain/recommendation.py`
- `src/agro_do/bridge/loader.py`
- `src/agro_do/decision_orchestrator/orchestrator.py`
- `src/agro_do/decision_orchestrator/llm_orchestrator.py`
- `src/agro_do/integrations/openai_client.py`

### 4.2 Main environment
Implemented reference environment:
- `inputs/greenhouse_blueprints/reference_tomato_greenhouse.json`

### 4.3 Already implemented sample cases
Validated case files:
- `inputs/sample_cases/case_main_pump_degradation.json`
- `inputs/sample_cases/case_high_humidity_disease_risk.json`
- `inputs/sample_cases/case_communication_loss_partial_blindness.json`
- `inputs/sample_cases/case_manual_override_mismatch.json`
- `inputs/sample_cases/case_sensor_drift_flatline.json`
- `inputs/sample_cases/case_low_tank_supply_uncertainty.json`
- `inputs/sample_cases/case_controlled_irrigation_rationing.json`

### 4.4 Local OpenAI integration
Already working locally through:
- `.env` in the user's local repo
- `.env.example` in repo
- OpenAI integration already tested successfully

Do not ask again whether OpenAI works.  
It already works.

---

## 5. What has already been proven

The next LLM must treat the following as already validated facts, not open questions.

### 5.1 Structural validation
- domain contracts validated
- blueprint validated
- decision cases validated
- bridge payload generation validated

### 5.2 Real local generative execution
The local OpenAI path is already working.

### 5.3 Governed differentiated behavior already demonstrated

#### Case 1 — Pump degradation with backup available
Observed output:
- priority: `high`
- action: `switch_to_backup`
- human review: `true`
- confidence: `high`

Meaning:
The system can escalate to a continuity-oriented response when a serious failure has an available fallback path.

#### Case 2 — High humidity / disease risk without clear backup path
Observed output:
- priority: `high`
- action: `adjust_operation`
- human review: `true`
- confidence: `high`

Meaning:
The system can distinguish an operational correction case from a backup-switching case.

#### Case 3 — Communication loss / limited visibility
Observed output:
- priority: `high`
- action: `escalate_to_human`
- human review: `true`
- confidence: `medium`

Meaning:
The system already reduces confidence and becomes more cautious when trusted visibility is degraded.

#### Case 4 — Manual override mismatch
Observed output:
- priority: `high`
- action: `stop_and_review`
- human review: `true`
- confidence: `medium`

Meaning:
The system can stop automation when digital state may not match physical reality.

#### Case 5 — Sensor drift / flatline
Observed output:
- priority: `high`
- action: `escalate_to_human`
- human review: `true`
- confidence: `medium`

Meaning:
The system can treat data quality and sensor trust as the core problem instead of assuming a physical equipment failure.

#### Case 6 — Low tank / supply uncertainty
Observed output:
- priority: `high`
- action: `stop_and_review`
- human review: `true`
- confidence: `high`

Meaning:
The system clearly recognizes continuity-risk caused by low reserves, but this case also exposed a refinement frontier because the response may be stricter than ideal in some scarcity situations.

#### Case 7 — Controlled irrigation rationing under low-water conditions
Observed output:
- priority: `high`
- action: `adjust_operation`
- human review: `true`
- confidence: `high`

Meaning:
The system can already distinguish between a stop-oriented continuity threat and a still-manageable scarcity scenario where controlled mitigation, sector prioritization, and rationing are preferable to an immediate hard stop.

Important conclusion:
Case 7 is the most important recent result because it confirms that Agro-DO is not simply becoming more severe. It is becoming more precise inside the same resource-continuity problem family.

---

## 6. Current project maturity

Agro-DO is no longer just a structured prototype.  
It already behaves as a governed service that distinguishes at least seven operational patterns:

- severe failure with backup → continuity response
- severe climate issue without backup → operational adjustment
- degraded visibility → human escalation with reduced confidence
- digital/physical mismatch → stop and review
- misleading sensor behavior → human escalation due to data trust risk
- low reserve / continuity threat with stronger interruption signal → stop-oriented response
- low reserve with still-manageable hydraulic conditions → controlled mitigation through operational adjustment

This means the project already has:
- differentiated behavior,
- meaningful policy structure,
- and enough validated diversity to reveal not only strengths, but transition boundaries between different policy styles.

---

## 7. Current weakness / refinement area

The most useful current refinement area is no longer simply “does the service understand scarcity?”

That has already been answered.

The current frontier is now this:

Can Agro-DO identify the boundary between:
- scarcity that should still be managed through controlled mitigation,
- and scarcity that has become unsafe enough to justify a stop-oriented response?

### Current interpretation
Case 6 and Case 7 together show that the system can already separate two scarcity patterns:
- one that leads to `stop_and_review`,
- and one that leads to `adjust_operation`.

### The remaining issue
What is not yet mapped precisely is the switching frontier.

The project still needs a case where scarcity is no longer just about low reserves, but begins to combine with worsening hydraulic reliability or degraded execution feasibility.

### Why this matters
The next level of product maturity is not only distinguishing hard stop from controlled rationing. It is understanding when controlled rationing stops being the right answer.

In other words, the next refinement should help the service distinguish between:
- “serious but manageable through controlled mitigation”
- and
- “no longer stable enough for mitigation, so interruption-oriented response becomes justified”

This is the current best refinement frontier.

---

## 8. The single correct next objective

## Next correct objective
Create and validate Case 8 focused on low-water continuity risk combined with deteriorating hydraulic stability, so that the project can test the policy boundary between `adjust_operation` and `stop_and_review`.

### Why this is the correct next step
Case 6 already showed that Agro-DO recognizes continuity-risk strongly.
Case 7 already showed that Agro-DO can choose a more graduated response when flow and pressure remain stable.

The next meaningful question is therefore:
What happens when scarcity remains serious and mitigation is no longer clearly safe because hydraulic behavior starts to degrade?

Case 8 must test whether the service can identify when controlled rationing is no longer sufficient and interruption-oriented logic becomes more appropriate again.

### What must not happen before this
Do not:
- redesign the architecture,
- open API/UI work,
- reopen product identity questions,
- rewrite guardrails broadly,
- write the global external-facing validation report yet.

The next LLM must do Case 8 first.

---

## 9. Immediate next action for the next LLM

This is the section the next LLM must follow first, without asking what to do.

### 9.1 First file to create
`inputs/sample_cases/case_low_water_hydraulic_instability.json`

### 9.2 Intent of Case 8
This case should represent a situation where:
- water reserves are low,
- continuity is threatened,
- mitigation through rationing may no longer be enough,
- and the system must be tested on whether it shifts away from `adjust_operation` toward a stricter response because hydraulic execution itself is becoming unstable.

Possible signals should suggest:
- worsening pressure behavior,
- unstable flow,
- or a reduced ability to execute prioritized irrigation reliably.

### 9.3 Validation sequence to follow
The next LLM must use exactly this sequence:

1. Create the case JSON
2. Validate JSON
3. Validate through the bridge
4. Execute the governed LLM run
5. Compare Case 8 behavior against Case 7 and Case 6
6. Document the milestone
7. Commit and push

### 9.4 Expected evaluation question
The next LLM must explicitly ask itself:
- Does Agro-DO still try `adjust_operation` when hydraulic stability is already deteriorating?
- Or does it correctly move back toward a stop-oriented or stricter escalation response?

That is the key question.

---

## 10. Minimal command pattern the next LLM should follow

The next LLM should continue in the same step-by-step execution style already used in this project:

- one objective at a time,
- one step at a time,
- command first,
- then exact content to paste,
- expected output explicitly described,
- no unnecessary questions.

The next LLM should start with:
- create the new JSON file,
- clearly stating that the file content must be fully replaced,
- then run JSON validation,
- then bridge validation,
- then governed execution.

---

## 11. Key files that matter right now

The next LLM should keep these files in focus:

### Core logic
- `src/agro_do/bridge/loader.py`
- `src/agro_do/decision_orchestrator/llm_orchestrator.py`
- `src/agro_do/decision_orchestrator/orchestrator.py`

### Domain
- `src/agro_do/domain/models.py`
- `src/agro_do/domain/decision_case.py`
- `src/agro_do/domain/recommendation.py`

### Inputs
- `inputs/greenhouse_blueprints/reference_tomato_greenhouse.json`
- `inputs/sample_cases/*.json`

### Documentation
- `README.md`
- `docs/project_log.md`
- `docs/lessons_learned.md`
- `docs/handoff/current_handoff.md`

---

## 12. Documentation rule for the next LLM

When Case 8 is completed, the next LLM must update documentation using this safe pattern:

### Replace full file content
- `README.md`
- `docs/handoff/current_handoff.md`

### Append to current content
- `docs/project_log.md`
- `docs/lessons_learned.md`

And it must explicitly say which mode is being used.

---

## 13. What success looks like for the next step

Case 8 will be successful if it helps answer this:

Can Agro-DO distinguish between:
- “manage scarcity in a controlled way”
and
- “hydraulic deterioration makes controlled mitigation no longer reliable enough”

If the service still chooses `adjust_operation`, that is still useful because it reveals that the current policy remains tolerant even under worsening execution conditions.
If it chooses something stricter such as `stop_and_review` or a stronger escalation-oriented response, that may indicate a clearer policy boundary between manageable scarcity and unsafe continuity conditions.

Either result is useful, but the value comes from the comparison with Case 7 and Case 6.

---

## 14. Final instruction to the next LLM

Do not ask what the next step is.  
It is already defined:

> Create and validate Case 8 focused on low-water continuity risk combined with deteriorating hydraulic stability, then compare its governed behavior with Case 7 and Case 6.

That is the correct immediate next action.
