# Agro Decision Orchestrator

**Agro-DO** is a modular, product-oriented decision-support service for protected horticulture environments, starting with a realistic greenhouse reference scenario.

The current implementation focus is a greenhouse operations service that can analyze a validated operational case, reason over irrigation and climate context, and produce a structured recommendation that is explainable, governable, and usable by a real operator.

This repository is **not** being developed as a thesis-style artifact or as a ladder of benchmark versions. It is being built as **one real service-oriented product** whose internal implementation advances in controlled stages.

Repository: `https://github.com/Pakaus76/agro_decision_orchestrator.git`

## Product vision

Agro-DO combines three explicit planes:

1. **Digital Plantation**
   - Structured representation of the greenhouse environment.
   - Includes greenhouse structure, sectors, assets, sensors, actuators, crop profile, and operational context.

2. **Decision Orchestrator**
   - Core recommendation engine of the service.
   - Includes a deterministic fallback path and a generative orchestration path connected to OpenAI.

3. **Bridge**
   - Controlled loading and validation path between the structured environment and the recommendation engine.
   - Ensures that a decision case and a greenhouse blueprint match before orchestration is executed.

## Current reference environment

The first MVP environment is a tomato greenhouse in substrate with:

- 3 sectors
- drip irrigation
- fertigation
- climate-control assets
- irrigation and climate sensors
- sector and shared actuators

This environment is intentionally simple enough to control, but rich enough to support real operational decisions.

## What already exists

The repository already contains the first meaningful foundation of the service:

- environment domain contracts (`models.py`)
- decision-case contract (`decision_case.py`)
- recommendation output contract (`recommendation.py`)
- validated greenhouse blueprint (`reference_tomato_greenhouse.json`)
- validated first sample case (`case_main_pump_degradation.json`)
- bridge loader with consistency checks (`loader.py`)
- deterministic orchestrator (`orchestrator.py`) used as a governed fallback layer
- OpenAI client adapter (`openai_client.py`)
- generative orchestrator (`llm_orchestrator.py`)
- first successful local execution of the generative path using a real OpenAI API key in the user's local environment

## Important architectural decisions

### 1. Agro-DO is one product, not a ladder of product versions

This project must not inherit the A/B/C/D/E/F framing of the previous scientific repository.

Correct interpretation:
- one real Agro-DO product
- one service-oriented architecture
- internal implementation stages only as construction steps
- no visible experimental version ladder in product naming or framing

### 2. Generative AI is mandatory in the target architecture

Generative AI is not optional in the destination of the product.

The service is being built toward a governed generative architecture. The deterministic orchestration layer remains important, but only as:
- a fallback path
- a control layer
- a robustness mechanism

It is not the intended endpoint of the product.

### 3. Documentation and chronology are part of the product discipline

The repository must remain chronologically traceable. Major implementation steps must be recorded not only in terms of what changed, but also why the step mattered, why it happened at that moment, and what it enables next.

## Current repository structure

```text
agro_decision_orchestrator/
├── app/
│   ├── backend/
│   └── frontend/
├── docs/
│   ├── architecture/
│   ├── experiments/
│   ├── handoff/
│   │   └── current_handoff.md
│   ├── interviews/
│   ├── product/
│   ├── lessons_learned.md
│   └── project_log.md
├── inputs/
│   ├── greenhouse_blueprints/
│   │   └── reference_tomato_greenhouse.json
│   ├── sample_cases/
│   │   └── case_main_pump_degradation.json
│   └── scenarios/
├── outputs/
│   ├── exports/
│   ├── reports/
│   └── runs/
├── scripts/
├── src/
│   └── agro_do/
│       ├── bridge/
│       │   └── loader.py
│       ├── decision_orchestrator/
│       │   ├── __init__.py
│       │   ├── llm_orchestrator.py
│       │   └── orchestrator.py
│       ├── digital_plantation/
│       ├── domain/
│       │   ├── __init__.py
│       │   ├── decision_case.py
│       │   ├── models.py
│       │   └── recommendation.py
│       ├── integrations/
│       │   ├── __init__.py
│       │   └── openai_client.py
│       ├── persistence/
│       ├── reporting/
│       ├── ui_contracts/
│       └── utils/
├── tests/
│   ├── fixtures/
│   ├── integration/
│   └── unit/
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

## Current service status

The repository has already crossed the line between static modeling and functional service behavior.

What has been demonstrated so far:

1. the system can load and validate a greenhouse environment
2. the system can load and validate a normalized decision case
3. the bridge can build a validated execution payload
4. the deterministic path can generate a structured recommendation
5. the generative path can call OpenAI in the local environment and return a structured recommendation using the shared recommendation contract

This means Agro-DO is no longer only a well-structured repository. It is already the first working backbone of a real generative decision-support service.

## Documentation workflow

The update order for each major milestone must remain:

1. `docs/project_log.md`
2. `README.md`
3. `docs/lessons_learned.md` when applicable
4. `docs/handoff/current_handoff.md`
5. Git commit and GitHub push

## Current strategic conclusion

The project foundations are already sufficient. The correct next steps are no longer foundational redesign. The correct next steps are product deepening, especially:

- strengthen generative guardrails
- expand the case library
- improve service entry paths
- prepare future API and UI execution on top of the existing governed generative core
