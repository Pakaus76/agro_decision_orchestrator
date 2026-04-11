# Current Handoff — Agro Decision Orchestrator

## 1. Purpose of this handoff

This document is intended to let another LLM continue the Agro Decision Orchestrator project without losing context, ambition, decisions, progress state, or working method.

It should be kept synchronized with:
1. `docs/project_log.md`
2. `README.md`
3. `docs/lessons_learned.md`

This file is not meant to replace those documents. It should synthesize them and preserve the execution context needed for continuity.

---

## 2. Non-negotiable operating rules

1. The assistant acts as the project assistant. The user executes commands locally in Visual Studio Code.
2. All repository files must be written in English.
3. Code comments, markdown documentation, CSV headers, structured texts, variable names, and identifiers must remain in English.
4. Conversation with the user remains in Spanish.
5. The repository must stay synchronized in this order:
   1. `docs/project_log.md`
   2. `README.md`
   3. `docs/lessons_learned.md` when applicable
   4. `docs/handoff/current_handoff.md`
   5. Git commit and GitHub push
6. Before a major log update, the project manager must have the opportunity to add a comment or voice-note transcript.
7. The root `README.md` must always explain the project clearly enough for an external visitor to understand purpose, structure, usage direction, and result interpretation.
8. The `README.md` must include an updated repository tree that matches the real tracked structure.
9. The handoff file must remain detailed enough for another LLM to continue the work without losing ambition, plan, decisions, progress state, or user preferences.
10. For repository markdown files that the user needs to copy easily, attached file delivery is preferred when practical.
11. Chronological traceability must be explanatory, not telegraphic: major milestones must document what was done, why it mattered, why it was done then, and what it unlocks next.

---

## 3. Product vision

The target product is a modular agricultural decision-support platform that combines:

1. **Digital Plantation**  
   A structured digital representation of the greenhouse environment, including sectors, assets, sensors, actuators, crop context, external weather, incidents, and operational constraints.

2. **Decision Orchestrator**  
   A reasoning layer that receives a normalized agricultural decision case and returns a prioritized, explainable, and actionable recommendation.

3. **Bridge**  
   A thin and explicit integration layer that reads cases from the digital plantation, normalizes them into a stable contract, invokes one or more decision policies, persists outputs, and supports comparisons or reporting.

The system is intended to help greenhouse owners, greenhouse managers, technicians, and agronomic advisors make better decisions regarding irrigation, fertigation, humidity control, temperature control, ventilation, shading, water system health, actuator reliability, sensor trustworthiness, and operational prioritization.

---

## 4. Canonical starting environment

The initial reference environment has already been fixed and should not be broadened prematurely.

**Canonical scenario:**
- tomato greenhouse,
- substrate cultivation,
- 3 sectors,
- drip irrigation,
- fertigation,
- automatic ventilation,
- circulation fans,
- shading screen,
- basic irrigation and climate sensing.

This scope is deliberately narrow enough to stay controllable and rich enough to support realistic product behavior.

---

## 5. Intended MVP

The first meaningful product milestone is a working local prototype where the user can:

- open the project in Visual Studio Code,
- run the backend locally,
- load a predefined greenhouse scenario,
- choose a fault case from a UI,
- execute the agricultural decision orchestrator,
- inspect a recommendation card that shows:
  - priority,
  - action,
  - rationale,
  - involved assets,
  - suggested next checks,
- save the run.

This MVP is more important than speculative future sophistication.

---

## 6. Repository structure currently in place

The repository has already been bootstrapped with this tracked structure:

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

The repository is already published on GitHub and tracks `origin/main`.

**GitHub repository:**  
`https://github.com/Pakaus76/agro_decision_orchestrator`

---

## 7. Technology stack currently fixed

### Backend
- Python
- `pydantic` as current base dependency
- `FastAPI` and `uvicorn` prepared as optional API dependencies in `pyproject.toml`

### Quality / development tooling
- `pytest`
- `ruff`
- `mypy`

### Packaging structure
- `src/` layout
- Python target version: `3.11`

The frontend stack has not yet been implemented, but the working direction remains React / Next.js with TypeScript once the backend contracts are stable enough.

---

## 8. What has already been completed

### Completed milestone A — Repository bootstrap
Completed:
- project root created,
- local Git repository initialized,
- branch renamed to `main`,
- modular folder structure created,
- `.gitkeep` placeholders added where needed,
- `.gitignore` created,
- `pyproject.toml` created,
- initial `README.md` created,
- initial `docs/project_log.md` created,
- initial `docs/lessons_learned.md` created,
- initial `docs/handoff/current_handoff.md` created,
- first commit completed.

### Completed milestone B — GitHub publication
Completed:
- remote repository created on GitHub,
- local `origin` connected,
- `main` pushed successfully,
- local branch tracking `origin/main` confirmed.

### Completed milestone C — Initial domain foundation
Completed:
- `src/agro_do/domain/models.py` created with the first stable domain contracts,
- `src/agro_do/domain/__init__.py` updated to export the domain models cleanly,
- imports validated successfully through `PYTHONPATH=src`,
- first greenhouse blueprint created at `inputs/greenhouse_blueprints/reference_tomato_greenhouse.json`,
- blueprint validated successfully as JSON.

This is the first moment when the project has both:
- a stable abstract vocabulary of domain entities, and
- a concrete operational environment built with that vocabulary.

### Cleanup already handled
A local assistant-generated archive file was accidentally staged during the initial commit workflow. This was corrected before the first push by removing it from version control history and adding the bundle names to `.gitignore`.

---

## 9. Current project status

The project is still in **early product-foundation stage**, but it has moved beyond pure bootstrap.

The documentation layer is in place, the repository is published remotely, the first domain contracts exist, and the first greenhouse blueprint has been validated successfully.

The current highest-priority next objective is:

1. define the first decision-case contract,
2. create the first sample decision cases,
3. begin the first loader or validation path from blueprint data into decision-ready input structures,
4. only then move toward the first deterministic decision-orchestrator behavior.

---

## 10. Immediate next technical objective

The next assistant should start with:

### Objective
Define the initial decision-case foundation that will sit between the blueprint and the future deterministic orchestration logic.

### Expected next artifacts
- first decision-case model or schema,
- first recommendation model or schema if needed to keep outputs explicit,
- first sample cases under `inputs/sample_cases/`,
- possibly the first simple loader or validation script that proves blueprint and case data can be consumed coherently.

### Rationale
The domain and blueprint now exist, but the project still lacks the explicit structure of a “decision-ready case.” That structure must exist before meaningful orchestration logic, comparisons, or UI forms can be built.

The assistant must not jump ahead to LLM logic, predictive models, or frontend implementation before these foundations exist.

---

## 11. Product and modeling guidance to preserve

### Product mindset
Always think first in terms of:
- user value,
- workflows,
- configurable inputs,
- understandable outputs,
- explainability for non-technical operators.

Avoid drifting into research-first or benchmark-first framing.

### Modeling scope discipline
Do not broaden to “all agriculture.” Keep the first implementation anchored to one greenhouse reference environment.

### Bridge discipline
The bridge must remain thin. It should translate, invoke, persist, and report. It must not become the hidden center of business logic.

### Deterministic-first discipline
The first decision layer should be explainable and deterministic. Richer or AI-based layers are deferred until the product foundation is stable.

---

## 12. Interview and expert elicitation direction

This has not yet been implemented, but it is already a core design requirement.

When the project reaches that phase, expert knowledge should be elicited through concrete operational storytelling, not abstract modeling questions.

Preferred prompts later include:
- what happened last time this failed,
- what they check first,
- what cannot wait,
- which alarms waste time,
- when they trust intuition over the system.

This direction is already part of the intended product refinement strategy and should remain visible in future work.

---

## 13. Durable lessons already identified

The following lessons are already formalized in `docs/lessons_learned.md` and should remain active:

1. Deliver markdown documents as attached files when practical.
2. Preserve reusable knowledge in a dedicated lessons-learned file.
3. Do not commit auxiliary documentation bundles or similar archive artifacts unless intentionally part of the repository.
4. Treat chronological traceability as an explanatory narrative, not as a terse checklist.

---

## 14. Open decisions still pending

The following items are still pending and should be decided later, not prematurely:

- exact internal taxonomy for asset types,
- exact schema granularity for sensors versus logical measurements,
- persistence choice for early MVP (`JSON`/`CSV` only vs `SQLite`),
- shape of the first decision-case schema,
- shape of the first recommendation schema,
- exact timing for the first FastAPI scaffold,
- exact timing for the first frontend scaffold.

These are valid pending decisions, but none of them blocks starting the decision-case layer.

---

## 15. What the next assistant must avoid

1. Do not start with AI or prediction models.
2. Do not create UI first.
3. Do not overcomplicate the stack.
4. Do not expand the domain beyond the chosen greenhouse reference too early.
5. Do not write repository files in Spanish.
6. Do not break the documentation update order.
7. Do not advance multiple implementation steps without validating the current one with the user.

---

## 16. Working style expected by the user

The user strongly prefers a controlled stepwise execution style:

- one immediate objective at a time,
- one step at a time,
- completed / current / pending structure made explicit,
- exact shell or PowerShell command first,
- exact text to paste after the command,
- expected output stated clearly,
- no forward jumping before the current step is validated.

In addition, when the log is updated for a meaningful milestone, the narrative should be understandable to a poorly informed reader and should not assume hidden chat context.
