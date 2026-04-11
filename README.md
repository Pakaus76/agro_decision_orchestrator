# Agro Decision Orchestrator

**Agro-DO** is a modular decision-support product prototype for protected horticulture environments, starting with a realistic greenhouse reference scenario.

The system is designed to help greenhouse owners, managers, technicians, and agronomic advisors make better operational decisions related to irrigation, fertigation, climate control, equipment health, sensor trustworthiness, and intervention prioritization.

This project is intentionally product-oriented. It is not being developed as a thesis-only artifact or as a benchmark-first repository. The goal is to build a modular software foundation that can evolve into a real operator-facing platform and later into a service that can be deployed and monetized.

Repository: `https://github.com/Pakaus76/agro_decision_orchestrator.git`

## Working product vision

Agro-DO combines three explicit planes:

1. **Digital Plantation**
2. **Decision Orchestrator**
3. **Bridge**

The product must be built as **one real service-oriented Agro-DO**, not as a sequence of A/B/C/D/E/F-style product versions.

## Initial reference environment

- Crop: tomato
- Cultivation mode: substrate
- Greenhouse sectors: 3
- Irrigation: drip irrigation
- Nutrition: fertigation
- Climate control: automatic ventilation, circulation fans, shading screen
- Sensing: basic irrigation and climate sensing

## What already exists

- Core domain contracts for environment modeling
- Decision-case contract
- Recommendation contract
- Reference greenhouse blueprint
- First sample case
- Minimal bridge loading path with validated execution payload

## Important product-direction clarification

The project must **not** evolve as a thesis-style sequence of product versions such as A/B/C/D/E/F.

Correct approach:
- build one real Agro-DO product
- use implementation stages only as controlled construction steps
- name modules as service components, not as experimental conditions

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
│       ├── digital_plantation/
│       ├── domain/
│       │   ├── __init__.py
│       │   ├── decision_case.py
│       │   ├── models.py
│       │   └── recommendation.py
│       ├── persistence/
│       ├── reporting/
│       ├── ui_contracts/
│       └── utils/
├── tests/
│   ├── fixtures/
│   ├── integration/
│   └── unit/
├── .gitignore
├── pyproject.toml
└── README.md
```

## Documentation workflow

Update order for each major milestone:
1. `docs/project_log.md`
2. `README.md`
3. `docs/lessons_learned.md` when applicable
4. `docs/handoff/current_handoff.md`
5. Git commit and GitHub push

## Current status

Current repository stage:
- repository initialized and published
- environment contracts created and validated
- decision-case contract created and validated
- recommendation contract created and exported
- reference greenhouse blueprint created and validated
- first sample case created and validated
- minimal bridge loader created and validated
- product-direction correction recorded to avoid thesis-style versioning drift

Immediate next objective:
- create the first real orchestrator module in `src/agro_do/decision_orchestrator/orchestrator.py`
- keep the implementation oriented to one real service, not to internal product variants
