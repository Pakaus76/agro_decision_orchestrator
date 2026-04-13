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
- `inputs/sample_cases/case_low_water_hydraulic_instability.json`
- `inputs/sample_cases/case_borderline_hydraulic_degradation.json`

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
The system can distinguish between a stop-oriented continuity threat and a still-manageable scarcity scenario where controlled mitigation, sector prioritization, and rationing are preferable to an immediate hard stop.

#### Case 8 — Low-water continuity risk with deteriorating hydraulic stability
Observed output:
- priority: `high`
- action: `stop_and_review`
- human review: `true`
- confidence: `high`

Meaning:
The system can move back toward interruption-oriented logic when scarcity is combined with unstable flow and worsening pressure behavior, indicating that controlled mitigation is no longer operationally credible enough.

#### Case 9 — Borderline hydraulic degradation under low-water conditions
Observed output:
- priority: `high`
- action: `stop_and_review`
- human review: `true`
- confidence: `high`

Meaning:
The system currently treats even borderline hydraulic degradation as sufficient reason to stay on the interruption-oriented side once water reserves are critically low. This suggests that the effective scarcity boundary is earlier and more conservative than hoped.

Important conclusion:
Case 7, Case 8, and Case 9 together are the most important recent result because they show that Agro-DO does have a differentiated scarcity policy, but that the current threshold is conservative: stable execution still supports `adjust_operation`, while even mild degradation already tends to trigger `stop_and_review`.

---

## 6. Current project maturity

Agro-DO is no longer just a structured prototype.  
It already behaves as a governed service that distinguishes at least nine operational patterns:

- severe failure with backup → continuity response
- severe climate issue without backup → operational adjustment
- degraded visibility → human escalation with reduced confidence
- digital/physical mismatch → stop and review
- misleading sensor behavior → human escalation due to data trust risk
- low reserve / continuity threat with stronger interruption signal → stop-oriented response
- low reserve with still-manageable hydraulic conditions → controlled mitigation through operational adjustment
- low reserve with deteriorating hydraulic stability → return to stop-oriented logic
- low reserve with borderline hydraulic degradation → stop-oriented logic remains active

This means the project already has:
- differentiated behavior,
- meaningful policy structure,
- and enough validated diversity to reveal not only strengths, but transition boundaries between different policy styles.

---

## 7. Current weakness / refinement area

The most useful current refinement area is no longer simply whether the system distinguishes stable scarcity from clearly unstable scarcity.

That question has already been answered.

The current frontier is now this:

Can Agro-DO still expose any narrower transition zone before mild hydraulic degradation becomes enough to trigger `stop_and_review`?

### Current interpretation
Case 7, Case 8, and Case 9 together show:
- stable hydraulic scarcity → `adjust_operation`
- clearly unstable hydraulic scarcity → `stop_and_review`
- borderline hydraulic scarcity → `stop_and_review`

### The remaining issue
What is not yet known is whether the system has any softer transition band at all, or whether the current policy threshold is simply binary around “clearly stable” versus “not clearly stable.”

The project still needs a case where:
- low-water continuity pressure remains serious,
- hydraulic behavior is only minimally degraded,
- and the system is forced to reveal whether it still tolerates `adjust_operation` under a softer early-warning condition.

### Why this matters
The next level of product maturity is not only mapping the boundary. It is determining whether that boundary has any usable granularity.

In other words, the next refinement should help the service distinguish between:
- “clearly stable enough for controlled mitigation”
- “slightly degraded but still tolerable”
- and
- “already degraded enough to justify interruption-oriented response”

This is the current best refinement frontier.

---

## 8. The single correct next objective

## Next correct objective
Create and validate Case 10 focused on very mild early-warning hydraulic degradation under low-water conditions, so that the project can test whether any narrower transition zone exists before `stop_and_review` becomes dominant.

### Why this is the correct next step
Case 7 already showed that Agro-DO can choose `adjust_operation` under stable execution.
Case 8 already showed that Agro-DO moves to `stop_and_review` under clearly unstable execution.
Case 9 showed that even borderline degradation still remains on the `stop_and_review` side.

The next meaningful question is therefore:
Does the system tolerate any degradation at all before crossing that line?

Case 10 must test whether a very mild, early-warning degradation pattern still allows `adjust_operation`, or whether the current threshold is already triggered by any visible loss of stability.

### What must not happen before this
Do not:
- redesign the architecture,
- open API/UI work,
- reopen product identity questions,
- rewrite guardrails broadly,
- write the global external-facing validation report yet.

The next LLM must do Case 10 first.

---

## 9. Immediate next action for the next LLM

This is the section the next LLM must follow first, without asking what to do.

### 9.1 First file to create
`inputs/sample_cases/case_early_warning_hydraulic_softening.json`

### 9.2 Intent of Case 10
This case should represent a situation where:
- water reserves are low,
- continuity is threatened,
- hydraulic execution is still mostly functional,
- but weak early-warning signs suggest slight softening or minor deviation from ideal behavior.

Possible signals should suggest:
- near-normal flow with only minor inconsistency,
- pressure slightly below ideal but not fluctuating strongly,
- still-plausible controlled rationing with caution.

The purpose is to test whether Agro-DO has any narrower permissive band before it shifts into `stop_and_review`.

### 9.3 Validation sequence to follow
The next LLM must use exactly this sequence:

1. Create the case JSON
2. Validate JSON
3. Validate through the bridge
4. Execute the governed LLM run
5. Compare Case 10 behavior against Case 9, Case 8, and Case 7
6. Document the milestone
7. Commit and push

### 9.4 Expected evaluation question
The next LLM must explicitly ask itself:
- Does Agro-DO still choose `adjust_operation` when degradation is only a very mild early-warning signal?
- Or does any visible hydraulic softening already push it to `stop_and_review`?

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

When Case 10 is completed, the next LLM must update documentation using this safe pattern:

### Replace full file content
- `README.md`
- `docs/handoff/current_handoff.md`

### Append to current content
- `docs/project_log.md`
- `docs/lessons_learned.md`

And it must explicitly say which mode is being used.

---

## 13. What success looks like for the next step

Case 10 will be successful if it helps answer this:

Can Agro-DO distinguish between:
- “clearly stable enough for controlled mitigation”
- “very mild early-warning degradation that may still be tolerable”
- and
- “already degraded enough to justify interruption-oriented response”

If the service chooses `adjust_operation`, that is useful because it would reveal a narrower permissive band than currently visible.
If it chooses `stop_and_review`, that is still useful because it would confirm that the present threshold is triggered by almost any visible hydraulic degradation.

Either result is useful, but the value comes from the comparison with Case 7, Case 8, and Case 9.

---

## 14. Final instruction to the next LLM

Do not ask what the next step is.  
It is already defined:

> Create and validate Case 10 focused on very mild early-warning hydraulic degradation under low-water conditions, then compare its governed behavior with Case 9, Case 8, and Case 7.

That is the correct immediate next action.
