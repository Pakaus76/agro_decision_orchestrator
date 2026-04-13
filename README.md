# Agro Decision Orchestrator

**Agro-DO** is a modular decision-support product prototype for protected horticulture environments, starting with a realistic greenhouse reference scenario.

The system is designed to help greenhouse owners, managers, technicians, and agronomic advisors make better operational decisions related to irrigation, fertigation, climate control, equipment health, sensor trustworthiness, and intervention prioritization.

This repository is product-oriented. It is not being developed as a thesis-only artifact or as a benchmark-first repository. The goal is to build a modular software foundation that can evolve into a real operator-facing service.

---

## Current product direction

Agro-DO is being built as **one real service-oriented product**.

This means:

- generative AI is a **mandatory part** of the target architecture,
- deterministic orchestration exists as a **fallback and resilience layer**,
- internal implementation steps are used to build the service in an orderly way,
- but those steps are **not** treated as competing product versions.

---

## Working product vision

Agro-DO combines five explicit planes:

1. **Digital Plantation**
   - A structured digital representation of the greenhouse environment.
   - Includes greenhouse structure, sectors, assets, sensors, actuators, crop context, external weather, incidents, and operational constraints.

2. **Decision Case Layer**
   - A normalized representation of an operational situation that requires a decision.
   - Includes suspected issue, severity, visibility, affected assets, observed signals, and contextual notes.

3. **Bridge**
   - A thin integration layer that reads cases from the digital plantation, validates them against the environment, and builds a stable execution payload.
   - The bridge must remain explicit and must not hide business logic.

4. **Decision Orchestrator**
   - A service layer that produces structured recommendations.
   - Includes a deterministic fallback path and a governed generative path.

5. **Integrations**
   - External adapters such as the OpenAI client.
   - These adapters allow Agro-DO to use real generative AI while keeping the integration isolated from the core domain layer.

---

## Initial reference environment

The first canonical scenario for the MVP is:

- **Crop:** tomato
- **Cultivation mode:** substrate
- **Greenhouse sectors:** 3
- **Irrigation:** drip irrigation
- **Nutrition:** fertigation
- **Climate control:** automatic ventilation, circulation fans, shading screen
- **Sensing:** basic irrigation and climate sensing

This reference environment is simple enough for controlled implementation and rich enough to support realistic operational decisions.

---

## Current service flow

The current implemented flow is:

1. Load the greenhouse blueprint.
2. Load a normalized decision case.
3. Validate references and build a minimal execution payload.
4. Generate a recommendation through either:
   - the deterministic fallback orchestrator, or
   - the generative orchestrator backed by OpenAI.
5. Normalize the result into the shared recommendation contract.
6. Apply explicit guardrails to the generative output.
7. Fall back to deterministic orchestration if the generative path is unavailable or invalid.

This means the project already supports a real end-to-end decision path.

---

## Current proven capability

The repository has already demonstrated that Agro-DO can:

- load a structured greenhouse environment,
- load a realistic operational decision case,
- validate consistency between both,
- construct a stable execution payload,
- call OpenAI from the local environment,
- generate a structured recommendation,
- and govern the generative result through explicit guardrails and fallback behavior.

This is the current strongest validated capability of the project.

---

## Current open product question

The latest governed generative validation exposed an important product-policy question:

- when a case has **high severity** and a **backup path is available**,
- should the product be allowed to recommend an **inspect-first** action,
- or should policy force a stronger response such as:
  - `switch_to_backup`,
  - `adjust_operation`,
  - or `escalate_to_human`?

This is now a service-policy decision, not a technical architecture problem.

---

## MVP objective

The first meaningful milestone remains a working local prototype where the user can:

- open the project in Visual Studio Code,
- run the backend or service logic locally,
- load a predefined greenhouse scenario,
- choose one fault case,
- execute the Agro-DO recommendation flow,
- inspect a recommendation showing:
  - priority,
  - action,
  - rationale,
  - confidence,
  - review requirement,
  - next checks,
  - traceability,
- and save or expose the run later through a service entrypoint.

---

## Planned repository structure

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

---

## Main design principles

- **Product-first mindset**
- **Generative core with governed behavior**
- **Deterministic fallback**
- **Modular architecture**
- **Explicit contracts**
- **Traceable evolution**

---

## Current implementation phases

### Phase 1 — Repository bootstrap
Completed.

### Phase 2 — Domain contracts
Completed.

### Phase 3 — Digital plantation MVP
Completed for the first reference greenhouse blueprint.

### Phase 4 — Decision-case modeling
Completed for the first realistic sample case.

### Phase 5 — Bridge MVP
Completed for the minimal validated loading path.

### Phase 6 — Generative orchestration base
Completed for:
- OpenAI integration,
- deterministic fallback path,
- generative orchestrator,
- guarded generative validation.

### Phase 7 — Policy hardening
Current focus.
The next work should strengthen orchestration policy and guardrails for high-risk scenarios.

### Phase 8 — Service entry path
Pending.

### Phase 9 — UI MVP
Pending.

---

## Documentation workflow

The documentation set must remain synchronized throughout the project.

Update order for each major milestone:
1. `docs/project_log.md`
2. `README.md`
3. `docs/lessons_learned.md` when applicable
4. `docs/handoff/current_handoff.md`
5. Git commit and GitHub push

---

## Current status

Current repository stage:
- local repository initialized,
- published on GitHub,
- domain layer implemented,
- reference greenhouse blueprint implemented,
- first sample case implemented,
- bridge loading path implemented,
- recommendation contract implemented,
- deterministic fallback orchestrator implemented,
- OpenAI integration implemented,
- governed generative orchestrator validated locally.

Immediate next objective:
- strengthen explicit policy guardrails for high-risk cases,
- especially where severity is high and a backup path is available.

---

## Language and documentation conventions

- All repository files must be written in **English**.
- Code comments and internal documentation must be written in **English**.
- Variable names, parameters, and identifiers must be written in **English**.
- Conversations with the project manager may remain in **Spanish**.
