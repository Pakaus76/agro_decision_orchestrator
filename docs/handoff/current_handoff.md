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

### 3.8 Mandatory compliance with lessons learned
Everything written in `docs/lessons_learned.md` is mandatory for future assistants working on this project.

This means:
- lessons learned are not optional advice,
- they must be treated as binding operational rules,
- and any future assistant must check them before preparing edits, documentation updates, or project actions.

If a future assistant sees a conflict between convenience and a rule captured in `docs/lessons_learned.md`, the lessons learned rule takes precedence unless the project manager explicitly decides otherwise.

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
- `inputs/sample_cases/case_early_warning_hydraulic_softening.json`
- `inputs/sample_cases/case_slight_hydraulic_degradation_threshold.json`
- `inputs/sample_cases/case_confirmatory_near_threshold_hydraulics.json`
- `inputs/sample_cases/case_sector_prioritization_under_water_constraint.json`
- `inputs/sample_cases/case_tighter_sector_prioritization_under_water_constraint.json`
- `inputs/sample_cases/case_collapse_boundary_sector_prioritization.json`

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

#### Case 10 — Early-warning hydraulic softening under low-water conditions
Observed output:
- priority: `high`
- action: `adjust_operation`
- human review: `true`
- confidence: `high`

Meaning:
The system still tolerates controlled mitigation when hydraulic softening remains very mild and flow/pressure are mostly functional. This confirms that a narrow permissive band exists before the policy flips to interruption-oriented logic.

#### Case 11 — Slight hydraulic degradation near the threshold
Observed output:
- priority: `high`
- action: `stop_and_review`
- human review: `true`
- confidence: `high`

Meaning:
The system already flips back to interruption-oriented logic once degradation becomes slightly stronger than the Case 10 pattern. This places the switching threshold very close to the early-warning side.

#### Case 12 — Confirmatory near-threshold hydraulics
Observed output:
- priority: `high`
- action: `stop_and_review`
- human review: `true`
- confidence: `high`

Meaning:
The conservative side of the threshold reproduces under a confirmatory near-threshold case. This confirms that the flip observed between Case 10 and Case 11 is stable enough for the current stage of the project.

#### Case 13 — Sector prioritization under constrained water continuity
Observed output:
- priority: `high`
- action: `adjust_operation`
- human review: `true`
- confidence: `high`

Meaning:
The system can move beyond global stop-versus-continue logic and recommend a differentiated continuity allocation across sectors. It explicitly prioritized Sector A, reduced Sector B, and suspended Sector C under constrained water conditions while hydraulic execution remained viable.

#### Case 14 — Tighter sector prioritization under constrained water continuity
Observed output:
- priority: `high`
- action: `adjust_operation`
- human review: `true`
- confidence: `high`

Meaning:
The system can intensify the prioritization regime under tighter reserve pressure. It protected Sector A only and suspended Sectors B and C, showing that selective continuity remains viable deeper into the constrained allocation family than the previous case.

#### Case 15 — Collapse-boundary sector prioritization
Observed output:
- priority: `high`
- action: `stop_and_review`
- human review: `true`
- confidence: `high`

Meaning:
The system finally abandons continuity once even top-priority-only protection becomes too fragile. This confirms the collapse boundary of the prioritization family.

Important conclusion:
Case 13 through Case 15 together show a complete prioritization spectrum:
- broader selective continuity,
- one-sector-only continuity,
- and full collapse into interruption.

This is one of the strongest maturity signals in the project so far.

---

## 6. Current project maturity

Agro-DO is no longer just a structured prototype.  
It already behaves as a governed service that distinguishes at least fifteen operational patterns:

- severe failure with backup → continuity response
- severe climate issue without backup → operational adjustment
- degraded visibility → human escalation with reduced confidence
- digital/physical mismatch → stop and review
- misleading sensor behavior → human escalation due to data trust risk
- low reserve / continuity threat with stronger interruption signal → stop-oriented response
- low reserve with still-manageable hydraulic conditions → controlled mitigation through operational adjustment
- low reserve with deteriorating hydraulic stability → return to stop-oriented logic
- low reserve with borderline hydraulic degradation → stop-oriented logic remains active
- low reserve with very mild early-warning hydraulic softening → controlled mitigation remains viable
- low reserve with slight threshold-near degradation → stop-oriented logic resumes
- low reserve with confirmatory near-threshold hydraulics → stop-oriented logic confirmed
- constrained water continuity with sector prioritization → prioritized selective continuity through operational adjustment
- tighter constrained continuity with one-sector protection → stricter selective continuity through operational adjustment
- collapse-boundary prioritization under extreme water constraint → full interruption with human review

This means the project already has:
- differentiated behavior,
- meaningful policy structure,
- a stable scarcity-family threshold,
- and a complete prioritization family under constrained continuity.

---

## 7. Current weakness / refinement area

The most useful current refinement area is no longer the internal allocation logic of constrained continuity.

That family is now sufficiently characterized for the current stage.

The current frontier is now this:

What does Agro-DO do when continuity has collapsed internally, but an alternative recovery path may still exist externally?

### Current interpretation
The prioritization family is now complete:
- broader selective continuity,
- one-sector-only continuity,
- and full interruption once even that last strategy becomes too fragile.

### The remaining issue
What has not yet been explored is a new family where the decision depends on the existence of:
- emergency alternative water supply,
- temporary backup sourcing,
- tanker delivery,
- neighboring reserve sharing,
- or other recovery paths that may change the recommendation after internal continuity has collapsed.

### Why this matters
The next level of product maturity is broader recovery intelligence, not more internal allocation variation in a family that is already well mapped.

In other words, the next refinement should help the service distinguish between:
- “internal continuity collapsed and nothing else is available”
- “internal continuity collapsed but emergency recovery path exists”
- and
- “continue only after activating a backup continuity path”

This is the current best refinement frontier.

---

## 8. The single correct next objective

## Next correct objective
Create and validate Case 16 focused on emergency alternative water supply after internal continuity collapse, so that Agro-DO must reason about external recovery options rather than only internal prioritization.

### Why this is the correct next step
Case 15 already showed the collapse boundary of the prioritization family. Continuing to micro-sample that same family would produce diminishing returns.

The next meaningful question is therefore:
If internal continuity has collapsed, can Agro-DO change its recommendation when an emergency alternative water path exists?

Case 16 should test whether the presence of a credible backup water source, tanker supply, or emergency replenishment path changes the recommendation relative to Case 15.

### What must not happen before this
Do not:
- redesign the architecture,
- open API/UI work,
- reopen product identity questions,
- return to more internal prioritization micro-cases in the same family for now.

The next LLM must do Case 16 first.

---

## 9. Immediate next action for the next LLM

This is the section the next LLM must follow first, without asking what to do.

### 9.1 First file to create
`inputs/sample_cases/case_emergency_alternative_water_supply.json`

### 9.2 Intent of Case 16
This case should represent a situation where:
- internal continuity has effectively collapsed under extreme reserve pressure,
- but a credible external recovery path exists,
- such as tanker supply, emergency backup source, or rapid external replenishment.

Possible signals should suggest:
- internal reserves are critically low,
- direct internal continuity is no longer credible on its own,
- but there is a near-term emergency supply option that could justify a different operational recommendation.

The purpose is to test whether Agro-DO can reason about backup continuity through external recovery instead of treating all collapse cases as identical.

### 9.3 Validation sequence to follow
The next LLM must use exactly this sequence:

1. Create the case JSON
2. Validate JSON
3. Validate through the bridge
4. Execute the governed LLM run
5. Compare the result against Case 15
6. Document the milestone
7. Commit and push

### 9.4 Expected evaluation question
The next LLM must explicitly ask itself:
- Does Agro-DO still choose `stop_and_review` even when a credible emergency water path exists?
- Or does it move toward an operationally adjusted recovery-oriented recommendation?

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

When Case 16 is completed, the next LLM must update documentation using this safe pattern:

### Replace full file content
- `README.md`
- `docs/handoff/current_handoff.md`

### Append to current content
- `docs/project_log.md`
- `docs/lessons_learned.md`

### Preserve README structure
- `README.md` must preserve its current structure, including the project tree section.
- Any README update must carry forward the strongest prior structural version and must never degrade a previously validated section.

And it must explicitly say which mode is being used.

---

## 13. What success looks like for the next step

Case 16 will be successful if it helps answer this:

Can Agro-DO distinguish between:
- “internal continuity collapsed with no recovery path”
- “internal continuity collapsed but external emergency recovery is available”
- and
- “operational adjustment is justified only because the backup path exists”

If the service changes the recommendation relative to Case 15, that is useful because it shows broader recovery-path intelligence.
If it remains in `stop_and_review`, that is still useful because it reveals that current policy treats external supply recovery conservatively.

Either result is useful, but the value comes from moving into a genuinely new family rather than overworking an already-closed one.

---

## 14. Final instruction to the next LLM

Do not ask what the next step is.  
It is already defined:

> Create and validate Case 16 focused on emergency alternative water supply after internal continuity collapse, then compare its governed behavior with Case 15.

That is the correct immediate next action.
