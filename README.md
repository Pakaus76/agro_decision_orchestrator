# Agro Decision Orchestrator

Agro Decision Orchestrator (Agro-DO) is a product-oriented, governed decision-support service for greenhouse operations.

The project is designed as a real service concept for protected horticulture environments. It combines structured greenhouse context, normalized operational cases, a validated bridge payload, a deterministic fallback path, a generative orchestration layer using OpenAI, and explicit policy guardrails.

The current goal is not to build a scientific benchmark product made of competing versions. The goal is to build one credible governed service that can support operational decisions related to irrigation continuity, climate correction, equipment health, sensor trust, degraded visibility, and digital-physical state mismatch.

## Current status

The repository is working locally and is already connected to GitHub.

The following capabilities have already been validated:

- domain contracts
- greenhouse blueprint loading
- decision-case loading
- bridge payload generation
- local OpenAI integration
- governed generative recommendation execution

The project has already validated twelve realistic sample cases and has demonstrated differentiated behavior across multiple operational patterns.

### Latest validated result

The latest validated scenario is:

- `inputs/sample_cases/case_confirmatory_near_threshold_hydraulics.json`

This case was created to confirm whether the observed switching point inside the low-water scarcity family was stable.

The governed recommendation for this case produced:

- priority: `high`
- action type: `stop_and_review`
- human review required: `true`
- confidence: `high`

This is important because the closely related threshold cases produced:

- `case_early_warning_hydraulic_softening.json` -> `adjust_operation`
- `case_slight_hydraulic_degradation_threshold.json` -> `stop_and_review`
- `case_confirmatory_near_threshold_hydraulics.json` -> `stop_and_review`

The new comparison confirms that Agro-DO does have a narrow permissive band, but the switching threshold is stable enough to treat as a real boundary for the current stage of the project.

## Core architecture

<!-- PROJECT_TREE_START -->
## Project tree

The following tree shows the current directory structure of the repository.

```text
Listado de rutas de carpetas para el volumen OS
El numero de serie del volumen es 2814-033E
C:.
+---app
|   +---backend
|   \---frontend
+---docs
|   +---architecture
|   +---experiments
|   +---handoff
|   +---interviews
|   \---product
+---inputs
|   +---greenhouse_blueprints
|   +---sample_cases
|   \---scenarios
+---outputs
|   +---exports
|   +---reports
|   \---runs
+---scripts
+---src
|   \---agro_do
|       +---bridge
|       |   \---__pycache__
|       +---decision_orchestrator
|       |   \---__pycache__
|       +---digital_plantation
|       +---domain
|       |   \---__pycache__
|       +---integrations
|       |   \---__pycache__
|       +---persistence
|       +---reporting
|       +---ui_contracts
|       +---utils
|       \---__pycache__
\---tests
    +---fixtures
    +---integration
    \---unit

<!-- PROJECT_TREE_END -->

Agro-DO currently relies on the following structural layers:

- domain models
- decision case contract
- recommendation contract
- blueprint and case loader
- bridge payload builder
- deterministic orchestrator
- governed LLM orchestrator
- OpenAI integration layer

Main implemented modules:

- `src/agro_do/domain/models.py`
- `src/agro_do/domain/decision_case.py`
- `src/agro_do/domain/recommendation.py`
- `src/agro_do/bridge/loader.py`
- `src/agro_do/decision_orchestrator/orchestrator.py`
- `src/agro_do/decision_orchestrator/llm_orchestrator.py`
- `src/agro_do/integrations/openai_client.py`

## Reference inputs

### Greenhouse blueprint

- `inputs/greenhouse_blueprints/reference_tomato_greenhouse.json`

### Validated sample cases

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

## Validated behavioral coverage

The project has already demonstrated coherent governed behavior for at least these operational patterns:

- severe failure with backup available -> continuity-oriented response
- severe climate issue without a backup path -> operational adjustment
- degraded visibility -> cautious escalation with reduced confidence
- digital-physical state mismatch -> stop and review
- misleading sensor behavior -> escalation because data trust becomes the main risk
- low reserve and supply uncertainty -> stop-oriented continuity protection
- low reserve with still-manageable hydraulic conditions -> controlled mitigation through operational adjustment
- low reserve with deteriorating hydraulic stability -> return to stop-oriented logic
- low reserve with borderline hydraulic degradation -> stop-oriented logic remains active
- low reserve with very mild early-warning hydraulic softening -> controlled mitigation remains viable
- low reserve with slight threshold-near degradation -> stop-oriented logic resumes
- low reserve with confirmatory near-threshold hydraulics -> stop-oriented logic confirmed

This means Agro-DO is already behaving as a governed service with differentiated operational reasoning rather than as a generic alert generator, and it now reveals that the mitigation band inside the scarcity family is real but extremely narrow and sufficiently confirmed.

## Decision policy signal exposed by Case 10, Case 11, and Case 12

A major recent refinement question was whether the switching point inside the scarcity-plus-hydraulics family was real or just fragile.

That question is now sufficiently answered:

- Case 10 confirmed that very mild early-warning hydraulic softening can still remain inside the `adjust_operation` zone.
- Case 11 confirmed that a slightly stronger degradation pattern already moves to `stop_and_review`.
- Case 12 confirmed that the conservative side of that flip reproduces under a near-threshold confirmatory case.

This is a useful maturity signal because the service remains:

- high priority
- human reviewed
- operationally conservative

while also revealing that the current switching threshold is narrow, coherent, and stable enough for the present stage of development.

## Local execution notes

The repository is already configured for local OpenAI execution through a local `.env` file.

Important points:

- `.env` remains local and must not be committed
- `.env.example` exists in the repository
- OpenAI integration has already been tested successfully
- deterministic fallback remains part of the runtime behavior for resilience and inspection

## Minimal validation flow

A safe local validation flow for a new case is:

1. Create the case JSON in `inputs/sample_cases/`
2. Validate JSON syntax
3. Validate the case through the bridge
4. Execute the governed LLM recommendation
5. Compare the result against the closest existing case
6. Update documentation in the required order
7. Commit and push

## Documentation discipline

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

### Anti-overwrite safeguard

`docs/project_log.md` and `docs/lessons_learned.md` are cumulative memory files.

They must be treated as append-only by default.

Before editing either file:

- inspect the last visible `LOG-*` entry
- inspect the last visible `LESSON-*` entry
- verify that previous entries still exist
- assume that any much shorter replacement is wrong unless explicitly requested

### File-edit instruction rule

Whenever content is prepared for a repository file, the instruction must explicitly say one of these:

- replace the full file content
- append this block to the current file
- insert this block in a specific section

Ambiguous edit instructions are not acceptable.

## Immediate next focus

The scarcity-plus-hydraulics threshold family is now sufficiently characterized for the current stage of the project.

The next work should move to a new decision family where Agro-DO must reason about prioritization and trade-offs rather than only about hydraulic execution quality. A strong next candidate is a case family on sector prioritization under constrained continuity conditions.

In practical terms, the repository is now in a good position to stop iterating the same narrow threshold and start demonstrating broader operational decision value.

## Repository language rules

- conversation with the project manager: Spanish
- repository files: English
- code comments: English
- structured technical documentation inside files: English
