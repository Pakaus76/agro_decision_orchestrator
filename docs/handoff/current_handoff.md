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

Important conclusion:
Case 13 and Case 14 together show that Agro-DO is no longer only a threshold-sensitive continuity controller. It is becoming a governed allocation engine that can progressively tighten continuity according to agronomic and business priority under constrained water conditions.

---

## 6. Current project maturity

Agro-DO is no longer just a structured prototype.  
It already behaves as a governed service that distinguishes at least fourteen operational patterns:

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

This means the project already has:
- differentiated behavior,
- meaningful policy structure,
- a stable scarcity-family threshold,
- and now a deeper prioritization family under constrained continuity.

---

## 7. Current weakness / refinement area

The most useful current refinement area is no longer whether Agro-DO can prioritize at all, nor whether it can tighten prioritization.

Those questions have already been answered positively.

The current frontier is now this:

At what point does the prioritization family itself collapse from “still viable selective continuity” into a stricter stop-oriented response?

### Current interpretation
Case 13 and Case 14 together show:
- selective continuity can remain viable across more than one sector under constrained water,
- and it can remain viable even when narrowed down to the top-priority sector only,
- provided hydraulic execution still supports that allocation.

### The remaining issue
What has not yet been explored is a harder collapse-boundary case where:
- Sector A remains top priority,
- but the reserve margin becomes so narrow that even protecting only Sector A may no longer be credible,
- and Agro-DO must decide whether selective continuity still makes sense or whether it should finally escalate.

### Why this matters
The next level of product maturity is not only prioritization. It is understanding the collapse boundary of prioritization.

In other words, the next refinement should help the service distinguish between:
- “broad selective continuity still viable”
- “only top-priority continuity viable”
- and
- “even top-priority continuity no longer worth sustaining”

This is the current best refinement frontier.

---

## 8. The single correct next objective

## Next correct objective
Create and validate Case 15 focused on collapse-boundary prioritization under water constraint, so that Agro-DO must decide whether even the top-priority sector should still be sustained or whether the situation now justifies a stricter response.

### Why this is the correct next step
Case 13 showed that Agro-DO could prioritize across multiple sectors under constrained continuity.
Case 14 showed that Agro-DO could tighten that logic down to Sector A only.

The next meaningful question is therefore:
What happens when reserves become so constrained that even one-sector protection may no longer be a credible continuity strategy?

Case 15 should test whether the service:
- still recommends a highly restrictive prioritization-oriented `adjust_operation`,
- or escalates to `stop_and_review` because even the top-priority continuity strategy has collapsed.

### What must not happen before this
Do not:
- redesign the architecture,
- open API/UI work,
- reopen product identity questions,
- return to threshold micro-variation in the already-closed hydraulic family.

The next LLM must do Case 15 first.

---

## 9. Immediate next action for the next LLM

This is the section the next LLM must follow first, without asking what to do.

### 9.1 First file to create
`inputs/sample_cases/case_collapse_boundary_sector_prioritization.json`

### 9.2 Intent of Case 15
This case should represent a situation where:
- water reserves are even tighter than in Case 14,
- hydraulic execution is still technically available but only with minimal credibility,
- Sector A remains the only possible candidate for protection,
- Sector B and Sector C are already fully sacrificed,
- and the real question is whether protecting even Sector A still makes sense.

Possible signals should suggest:
- extremely low reserve margin,
- hydraulic execution still technically possible but with poor continuity confidence,
- a real strategic dilemma between one-sector survival and a stricter stop-oriented response.

The purpose is to identify the collapse boundary of the prioritization family.

### 9.3 Validation sequence to follow
The next LLM must use exactly this sequence:

1. Create the case JSON
2. Validate JSON
3. Validate through the bridge
4. Execute the governed LLM run
5. Compare the result against Case 14 and Case 13
6. Document the milestone
7. Commit and push

### 9.4 Expected evaluation question
The next LLM must explicitly ask itself:
- Does Agro-DO still keep `adjust_operation` when only one-sector protection remains barely credible?
- Or does it finally escalate once even top-priority continuity becomes too fragile?

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

When Case 15 is completed, the next LLM must update documentation using this safe pattern:

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

Case 15 will be successful if it helps answer this:

Can Agro-DO distinguish between:
- “broad selective continuity still viable”
- “only top-priority continuity viable”
- and
- “even top-priority continuity no longer worth sustaining”

If the service still chooses a highly restrictive `adjust_operation`, that is useful because it means the prioritization band is wider than expected.
If it chooses `stop_and_review`, that is still useful because it reveals the collapse boundary of the prioritization family.

Either result is useful, but the value comes from locating the point where selective continuity finally stops being credible.

---

## 14. Final instruction to the next LLM

Do not ask what the next step is.  
It is already defined:

> Create and validate Case 15 focused on collapse-boundary sector prioritization under water constraint, then compare its governed behavior with Case 14 and Case 13.

That is the correct immediate next action.
