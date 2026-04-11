# Current Handoff

## 1. Project purpose

This repository is building **Agro Decision Orchestrator (Agro-DO)**, a modular, product-oriented decision-support system for protected horticulture environments.

The target is not a thesis artifact and not a benchmark-only repository. The target is a real service-oriented product foundation that could later evolve into a deployable and monetizable offering.

## 2. Non-negotiable working rules

1. The assistant guides; the user executes locally in Visual Studio Code.
2. All repository files must be written in English.
3. Conversations with the user remain in Spanish.
4. Documentation update order:
   - `docs/project_log.md`
   - `README.md`
   - `docs/lessons_learned.md` when applicable
   - `docs/handoff/current_handoff.md`
   - Git commit and GitHub push
5. Do not use ZIP bundles as normal delivery artifacts.
6. The project log must explain what happened, why it mattered, why it happened then, and what it enables next.
7. Do not drift into thesis-style A/B/C/D/E/F product variants.

## 3. Repository status

Remote repository:
- `https://github.com/Pakaus76/agro_decision_orchestrator.git`

Current state already achieved:
- repository bootstrapped and published to GitHub
- domain contracts for the environment created
- normalized decision-case contract created
- normalized recommendation contract created
- reference greenhouse blueprint created and validated
- first sample case created and validated
- minimal bridge loader created and validated
- product-direction correction recorded to prevent version-ladder drift

## 4. Important design correction already made

A drift toward a thesis-style file such as `condition_a.py` was detected when the first orchestration logic was about to be implemented.

This drift was corrected immediately.

Interpretation for future assistants:
- do not build the product as visible internal variants or benchmark conditions
- do not name orchestration modules using A/B/C-style labels
- do not describe the architecture as a ladder of versions

Correct framing:
- Agro-DO is one real product
- internal steps are only controlled construction steps
- orchestration modules should be named as service components, for example:
  - `orchestrator.py`
  - `policy_engine.py`
  - `recommendation_service.py`

## 5. Correct next objective

Create the first real orchestrator module in `src/agro_do/decision_orchestrator/orchestrator.py`.

This module should:
1. receive the validated minimal execution payload
2. apply service-oriented deterministic logic
3. use the normalized recommendation output contract
4. remain explainable and governed
5. be designed as the first real core of the product, not as an experimental variant
