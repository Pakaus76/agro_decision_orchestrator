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
- `inputs/sample_cases/case_emergency_alternative_water_supply.json`

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

#### Case 16 — Emergency alternative water supply after internal continuity collapse
Observed output:
- priority: `high`
- action: `switch_to_backup`
- human review: `true`
- confidence: `high`

Meaning:
The system changes its recommendation when a credible emergency external water supply exists. It no longer treats the scenario as a pure collapse-to-stop case and instead recommends backup-oriented recovery focused on the highest-priority sector.

Important conclusion:
Case 16 is the most important recent result because it proves Agro-DO can now reason not only about degradation and internal allocation, but also about external recovery paths.

---

## 6. Current project maturity

Agro-DO is no longer just a structured prototype.  
It already behaves as a governed service that distinguishes at least sixteen operational patterns:

- severe failure with backup → continuity response
- severe climate issue without backup → operational adjustment
- degraded visibility → human escalation with reduced confidence
- digital-physical mismatch → stop and review
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
- internal collapse with confirmed emergency external water supply → backup-oriented recovery through `switch_to_backup`

This means the project already has:
- differentiated behavior,
- meaningful policy structure,
- a stable scarcity-family threshold,
- a complete prioritization family,
- and a first external recovery family.

---

## 7. Current weakness / refinement area

The most useful current refinement area is no longer whether Agro-DO can reason about external recovery at all.

That question has already been answered positively.

The current frontier is now this:

How credible must an external recovery path be before Agro-DO changes its recommendation away from interruption?

### Current interpretation
Case 16 shows:
- internal continuity may already be collapsed,
- but a credible confirmed emergency tanker arrival can shift the decision to `switch_to_backup`.

### The remaining issue
What has not yet been explored is a harder recovery case where:
- external supply exists,
- but it is delayed, uncertain, partially confirmed, or operationally weak,
- and Agro-DO must decide whether that backup path is still strong enough to justify recovery-oriented action.

### Why this matters
The next level of product maturity is not only recognizing that backup exists. It is calibrating how backup credibility changes the recommendation.

In other words, the next refinement should help the service distinguish between:
- “confirmed recovery path strong enough to switch”
- “recovery path exists but is weak or uncertain”
- and
- “recovery path too weak to change the collapse recommendation”

This is the current best refinement frontier.

---

## 8. The single correct next objective

## Next correct objective
Create and validate Case 17 focused on uncertain or delayed emergency alternative water supply, so that Agro-DO must decide whether a weaker recovery path still justifies backup-oriented action.

### Why this is the correct next step
Case 16 already showed that a strong confirmed emergency supply can change the recommendation. The next meaningful question is therefore not whether recovery exists, but whether the recovery path is credible enough.

Case 17 should test whether Agro-DO:
- still recommends `switch_to_backup`,
- downgrades to `adjust_operation`,
- or returns to `stop_and_review`
when the emergency external supply is less certain or more delayed than in Case 16.

### What must not happen before this
Do not:
- redesign the architecture,
- open API/UI work,
- reopen product identity questions,
- return to more prioritization micro-cases in the already-closed internal allocation family.

The next LLM must do Case 17 first.

---

## 9. Immediate next action for the next LLM

This is the section the next LLM must follow first, without asking what to do.

### 9.1 First file to create
`inputs/sample_cases/case_uncertain_emergency_alternative_water_supply.json`

### 9.2 Intent of Case 17
This case should represent a situation where:
- internal continuity has collapsed,
- an external emergency recovery path exists,
- but it is delayed, uncertain, partially confirmed, or otherwise weaker than the tanker case in Case 16.

Possible signals should suggest:
- internal reserves remain critically low,
- direct continuity is still not viable internally,
- but a possible external recovery path may arrive too late or with too much uncertainty to fully justify confidence.

The purpose is to test whether Agro-DO calibrates recovery recommendations according to backup credibility rather than treating all external supply cases equally.

### 9.3 Validation sequence to follow
The next LLM must use exactly this sequence:

1. Create the case JSON
2. Validate JSON
3. Validate through the bridge
4. Execute the governed LLM run
5. Compare the result against Case 16 and Case 15
6. Document the milestone
7. Commit and push

### 9.4 Expected evaluation question
The next LLM must explicitly ask itself:
- Does Agro-DO still choose `switch_to_backup` when emergency supply is weaker or delayed?
- Or does it return toward a stricter interruption-oriented response when backup credibility drops?

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

When Case 17 is completed, the next LLM must update documentation using this safe pattern:

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

Case 17 will be successful if it helps answer this:

Can Agro-DO distinguish between:
- “confirmed recovery path strong enough to switch”
- “weaker or delayed recovery path”
- and
- “recovery path too weak to change the collapse recommendation”

If the service still chooses `switch_to_backup`, that is useful because it means backup tolerance is wider than expected.
If it chooses `stop_and_review`, that is still useful because it reveals that current recovery logic is conservative with weak backup paths.
If it chooses another intermediate response, that is also valuable because it suggests a more nuanced recovery calibration.

Either result is useful, but the value comes from testing backup credibility rather than simply backup existence.

---

## 14. Final instruction to the next LLM

Do not ask what the next step is.  
It is already defined:

> Create and validate Case 17 focused on uncertain or delayed emergency alternative water supply, then compare its governed behavior with Case 16 and Case 15.

That is the correct immediate next action.
