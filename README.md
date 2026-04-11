# Agro Decision Orchestrator

**Agro-DO** is a modular decision-support product prototype for protected horticulture environments, starting with a realistic greenhouse reference scenario.

The system is designed to help greenhouse owners, managers, technicians, and agronomic advisors make better operational decisions related to irrigation, fertigation, climate control, equipment health, sensor trustworthiness, and intervention prioritization.

This project is intentionally product-oriented. It is not being developed as a thesis-only artifact or as a benchmark-first repository. The goal is to build a modular software foundation that can evolve into a real operator-facing platform.

---

## Working product vision

Agro-DO combines three explicit planes:

1. **Digital Plantation**
   - A structured digital representation of the greenhouse environment.
   - Includes greenhouse structure, sectors, assets, sensors, actuators, crop context, external weather, incidents, and operational constraints.

2. **Decision Orchestrator**
   - A reasoning layer that receives a normalized agricultural decision case and returns prioritized, explainable, and actionable recommendations.
   - Outputs include priority, recommended action, rationale, confidence, alternatives, review requirements, and traceability.

3. **Bridge**
   - A thin integration layer that reads cases from the digital plantation, normalizes them into a stable contract, invokes one or more decision policies, persists outputs, and supports comparisons and reporting.
   - The bridge must remain explicit and must not hide business logic.

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

## MVP objective

The first meaningful milestone is a working local prototype where the user can:

- open the project in Visual Studio Code,
- run the backend locally,
- load a predefined greenhouse scenario,
- choose one fault case from a user interface,
- execute the agricultural decision orchestrator,
- inspect a recommendation card showing:
  - priority,
  - action,
  - rationale,
  - involved assets,
  - suggested next checks,
- save the run for later inspection.

---

## Target users

### 1. Greenhouse owner / business owner
Needs:
- simple visibility,
- prioritized risks,
- confidence in the recommendation,
- reduced crop and downtime risk.

### 2. Greenhouse operations manager
Needs:
- sector-specific diagnosis,
- actionable priorities,
- traceable recommendations,
- alarm triage support.

### 3. Technician / irrigation or maintenance specialist
Needs:
- root-cause hints,
- asset-focused diagnostics,
- guidance on what to inspect first,
- clear review markers.

### 4. Agronomist / crop advisor
Needs:
- crop-context explanation,
- environmental risk interpretation,
- evidence before intervention.

---

## Repository structure

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
│   └── scenarios/
├── outputs/
│   ├── exports/
│   ├── reports/
│   └── runs/
├── scripts/
├── src/
│   └── agro_do/
│       ├── bridge/
│       ├── decision_orchestrator/
│       ├── digital_plantation/
│       ├── domain/
│       │   ├── __init__.py
│       │   └── models.py
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

---

## Main design principles

- **Product-first mindset**
  - Focus on user value, workflows, explainability, and operational usefulness.

- **Modular architecture**
  - No monolithic script.
  - Clear boundaries between domain, simulation, orchestration, persistence, reporting, and UI contracts.

- **Explicit contracts**
  - Stable schemas for domain objects, decision cases, and recommendation outputs.

- **Deterministic foundation first**
  - The system starts with simple and governed deterministic logic before any predictive or LLM-based extension.

- **Thin bridge**
  - The bridge translates, invokes, persists, and reports.
  - It must not silently change the meaning of the case.

- **Traceable evolution**
  - Major decisions, milestones, and relevant test outcomes are recorded in the project log, distilled into lessons learned when reusable, and reflected in the handoff file.

---

## Initial implementation phases

### Phase 1 — Repository bootstrap
Create the repository structure, core documentation, and base Python package.

### Phase 2 — Domain contracts
Define the first stable models:
- greenhouse,
- sector,
- asset,
- sensor,
- actuator,
- crop profile,
- decision case,
- recommendation.

### Phase 3 — Digital plantation MVP
Build the first greenhouse blueprint and the first structured input files.

### Phase 4 — Deterministic decision orchestrator MVP
Implement an explainable baseline policy.

### Phase 5 — Bridge MVP
Load a digital plantation case, build the normalized decision case, run the baseline policy, and persist the output.

### Phase 6 — UI MVP
Create the first operator-facing pages:
- scenario selection,
- run execution,
- recommendation view,
- run history.

### Phase 7 — Expert elicitation support
Create interview templates and transcript distillation workflows for future refinement.

### Phase 8 — Richer decision logic
Add more context-sensitive and governed conditions.

### Phase 9 — Optional predictive or AI layer
Only after the deterministic product foundation is stable.

---

## Documentation workflow

The documentation set must remain synchronized throughout the project.

Update order for each major milestone:
1. `docs/project_log.md`
2. `README.md`
3. `docs/lessons_learned.md` when applicable
4. `docs/handoff/current_handoff.md`
5. Git commit and GitHub push

The project log must explain not only what was created, but also why it was needed, why it was created at that specific moment, and what it enables next. The intention is to make the evolution of the project understandable even to a reader with very limited prior context.

---

## Current status

Current repository stage:
- local repository initialized,
- base folder structure created,
- project governance rules established,
- project log started,
- lessons learned file established,
- initial bootstrap committed,
- repository published to GitHub on `main`,
- first stable domain contracts created in `src/agro_do/domain/models.py`,
- domain exports validated through `src/agro_do/domain/__init__.py`,
- first greenhouse blueprint created in `inputs/greenhouse_blueprints/reference_tomato_greenhouse.json`,
- blueprint JSON validated successfully.

Immediate next objective:
- define the first decision-case contract,
- create the first sample decision cases,
- start the first loader or validation path from blueprint data to decision-ready inputs.

---

## How to use this repository

At the current stage, this repository is still under controlled foundation building.

The intended future usage flow is:

1. Load or configure a greenhouse scenario.
2. Build or select an agricultural decision case.
3. Run a decision policy through the backend.
4. Inspect the recommendation in a structured view.
5. Save the result and compare it with previous runs.

Usage instructions will be expanded as executable components are added.

---

## Project log, lessons learned, and handoff

- The chronological project log is maintained in `docs/project_log.md`.
- Reusable operating knowledge is maintained in `docs/lessons_learned.md`.
- The current assistant handoff document is maintained in `docs/handoff/current_handoff.md`.

Together, these documents preserve:
- the ambition of the project,
- the plan and milestones,
- completed work,
- pending decisions,
- reusable lessons,
- important manager comments and voice-note transcripts when provided.

---

## Language and documentation conventions

- All repository files must be written in **English**.
- Code comments and internal documentation must be written in **English**.
- Variable names, parameters, and identifiers must be written in **English**.
- Conversations with the project manager may remain in **Spanish**.

---

## Status disclaimer

This repository is in early product-foundation stage.
The architecture is intentionally being built from the ground up in a controlled and traceable way to support future growth without forcing premature complexity.
