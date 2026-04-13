# Current Handoff — Agro Decision Orchestrator

## Core identity
Agro-DO is one real service-oriented product for greenhouse decision support.

Important:
- generative AI is mandatory in the target product architecture,
- deterministic orchestration exists only as fallback and resilience,
- do not reintroduce A/B/C/F-style framing.

## Current implemented architecture
- `src/agro_do/domain/models.py`
- `src/agro_do/domain/decision_case.py`
- `src/agro_do/domain/recommendation.py`
- `inputs/greenhouse_blueprints/reference_tomato_greenhouse.json`
- `inputs/sample_cases/case_main_pump_degradation.json`
- `src/agro_do/bridge/loader.py`
- `src/agro_do/decision_orchestrator/orchestrator.py`
- `src/agro_do/decision_orchestrator/llm_orchestrator.py`
- `src/agro_do/integrations/openai_client.py`
- `.env.example`
- `pyproject.toml`

## What has already been proven
- domain contracts validated
- blueprint validated
- decision case validated
- bridge payload validated
- real local generative execution succeeded with OpenAI
- governed generative execution also succeeded

Observed governed output on the pump case:
- priority: `high`
- action type: `inspect`
- human review required: `True`
- confidence: `high`
- next checks: `6`
- decision trace: `8`

## Main conclusions
1. The project has crossed from static modeling into real service behavior.
2. Generative AI is already functioning in practice.
3. The key challenge is no longer plumbing, but policy hardening.
4. The next live design question is how strict the service should be when severity is high and a backup path is available.

## Correct next objective
Policy hardening for high-risk scenarios.

More concretely:
- strengthen guardrails in `llm_orchestrator.py`,
- especially for high-severity + backup-available cases,
- retest on the current case,
- then add more realistic cases.
