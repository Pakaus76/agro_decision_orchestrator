# Current Handoff — Agro Decision Orchestrator

## 1. Purpose of this handoff

This handoff is intended for a future LLM assistant that may need to continue the Agro Decision Orchestrator project without losing architectural intent, project discipline, chronology, or product direction.

It summarizes:
- what the project is,
- what has already been built,
- how the project must be managed,
- what rules are already fixed,
- what the next correct objective is,
- and what must be avoided.

This document must remain coordinated with:
- `README.md`
- `docs/project_log.md`
- `docs/lessons_learned.md`

The update order is always:
1. `docs/project_log.md`
2. `README.md`
3. `docs/lessons_learned.md` when applicable
4. `docs/handoff/current_handoff.md`
5. Git commit and GitHub push

---

## 2. Core project identity

**Project name:** Agro Decision Orchestrator  
**Short name:** Agro-DO

Agro-DO is a **product-oriented**, modular software prototype for agricultural decision support in protected horticulture environments.

It is centered on three planes:

1. **Digital Plantation**  
   A structured representation of the greenhouse environment, including assets, sensors, actuators, sectors, crop context, external context, and operational constraints.

2. **Decision Orchestrator**  
   A reasoning layer that receives a normalized agricultural decision case and returns a prioritized, explainable, and actionable recommendation.

3. **Bridge**  
   A thin and explicit integration layer that reads environment and case data, validates them together, prepares stable execution payloads, and later will support orchestration, persistence, and reporting.

The system is intended to help greenhouse owners, greenhouse managers, technicians, and agronomic advisors make better decisions regarding irrigation, fertigation, humidity control, temperature control, ventilation, shading, water system health, actuator reliability, sensor trustworthiness, and operational prioritization.

---

## 3. Non-negotiable working rules

The following rules are already fixed and must be preserved:

- The assistant acts as the user's technical assistant; the user executes in Visual Studio Code.
- Repository files must be written in **English**.
- Code comments, markdown files, JSON content, and structured internal texts must be written in **English**.
- Variable names, parameter names, identifiers, and file contents must stay in **English**.
- Conversation with the project manager remains in **Spanish**.
- Markdown deliverables should be provided as separate files rather than relying on chat rendering.
- Do **not** generate auxiliary ZIP bundles for this project.
- The root `README.md` must remain updated and must include a project tree that matches the real repository structure.
- The project log must explain what was done, why it was needed, why it was done at that point, and what it enables next.
- Before major documentation updates, the project manager must be given the opportunity to add a comment or voice-note transcript.
- The handoff must always remain aligned with the project log, README, and lessons learned.

---

## 4. Canonical starting environment

The initial reference environment is fixed and should not be broadened prematurely.

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

The MVP should grow by connecting already validated foundations, not by introducing speculative complexity.

---

## 6. Repository structure currently in place

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

**GitHub repository:**  
`https://github.com/Pakaus76/agro_decision_orchestrator`

The repository already tracks `origin/main`.

---

## 7. Technology stack currently fixed

### Backend
- Python
- `pydantic` as the current base dependency
- `FastAPI` and `uvicorn` prepared as optional API dependencies in `pyproject.toml`

### Quality / development tooling
- `pytest`
- `ruff`
- `mypy`

### Packaging structure
- `src/` layout
- Python target version: `3.11`

The frontend stack has not yet been implemented, but the intended direction remains React / Next.js with TypeScript once backend contracts are stable enough.

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
- imports validated successfully,
- `inputs/greenhouse_blueprints/reference_tomato_greenhouse.json` created,
- blueprint validated successfully as JSON.

Meaning:
- the project no longer has only repository structure,
- it already has both an abstract domain vocabulary and a first concrete greenhouse environment built with that vocabulary.

### Completed milestone D — Decision-ready case foundation
Completed:
- `src/agro_do/domain/decision_case.py` created with the normalized decision-case contract,
- `src/agro_do/domain/__init__.py` updated to export the decision-case types,
- decision-case imports validated successfully,
- `inputs/sample_cases/case_main_pump_degradation.json` created,
- the sample case validated successfully as JSON.

Meaning:
- the project can now describe not only what exists in the greenhouse,
- but also what is happening when an operational situation requires a decision,
- and it already contains one realistic example of such a situation.

### Completed milestone E — First bridge-side loading path
Completed:
- `src/agro_do/bridge/loader.py` created,
- greenhouse blueprint loading implemented,
- decision-case loading implemented,
- blueprint and case cross-reference validation implemented,
- `MinimalExecutionPayload` contract implemented,
- loader executed successfully with the reference blueprint and the main-pump degradation case.

Meaning:
- the project no longer contains only isolated definitions and example files,
- it already has a first functional path where environment data, case data, and bridge validation operate together,
- and it can already produce a validated payload ready for future deterministic orchestration.

### Cleanup already handled
A local assistant-generated archive file was accidentally staged during early work. It was removed before push. The user later made it explicit that ZIP bundles are not useful for this project and must not be generated again.

---

## 9. Current project status

The project is still in **early product-foundation stage**, but it has clearly moved beyond pure bootstrap and beyond static domain modeling.

At this point, the repository already contains:
- synchronized core documentation,
- a published GitHub history,
- initial domain contracts,
- a validated greenhouse blueprint,
- a validated decision-case contract,
- a validated sample case,
- and a validated bridge-side loading path.

The project already connects four consistent layers:
1. a structured greenhouse environment,
2. a normalized decision-case schema,
3. a concrete operational case,
4. a validated minimal execution payload.

This is the first real proof that the architecture is beginning to behave like a system rather than like a set of disconnected files.

---

## 10. Immediate next technical objective

The next assistant should start with:

### Objective
Create the first deterministic decision-orchestration path that consumes the validated execution payload and returns a simple, explainable recommendation output.

### Expected next artifacts
Possible next artifacts include:
- a first recommendation contract under `src/agro_do/domain/` or `src/agro_do/decision_orchestrator/`,
- a baseline deterministic orchestration module under `src/agro_do/decision_orchestrator/`,
- a minimal script or callable path that loads the blueprint and case, builds the execution payload, runs the deterministic logic, and prints or persists a first structured recommendation.

### Rationale
The project already has:
- the environment,
- the case schema,
- the sample case,
- and the first validated bridge path.

The next logical step is no longer to add more foundational structure for its own sake, but to prove that a first recommendation can be produced in a deterministic and explainable way from the validated payload.

The assistant should **not** jump yet to AI logic, predictive models, or frontend implementation.

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
Do not broaden to all agriculture. Keep the first implementation anchored to one greenhouse reference environment.

### Bridge discipline
The bridge must remain thin. It should translate, validate, invoke, persist, and report. It must not become the hidden center of business logic.

### Deterministic-first discipline
The first decision layer should be explainable and deterministic. Richer or AI-based layers are deferred until the product foundation is stable.

---

## 12. Interview and expert elicitation direction

This has not yet been implemented, but it remains a core design requirement.

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

1. Deliver markdown files directly instead of relying on chat rendering.
2. Preserve reusable interaction rules in a dedicated lessons-learned file.
3. Do not commit auxiliary archive bundles unless they are intentional repository artifacts.
4. Treat chronological traceability as an explanatory narrative, not as a terse checklist.
5. Do not generate auxiliary ZIP packages for this project.
6. Make manager summaries cumulative without repeating the same wording.

---

## 14. Open decisions still pending

The following items are still pending and should be decided later, not prematurely:

- exact internal taxonomy depth for asset and signal types,
- persistence choice for early MVP (`JSON`/`CSV` only vs `SQLite`),
- shape of the first recommendation schema,
- exact output location for first execution results,
- exact timing for the first FastAPI scaffold,
- exact timing for the first frontend scaffold.

These are valid pending decisions, but none of them blocks starting deterministic orchestration.

---

## 15. What the next assistant must avoid

1. Do not start with AI or prediction models.
2. Do not broaden scope to multiple agricultural environments.
3. Do not jump into UI before the next deterministic execution path is stable enough to expose.
4. Do not let the bridge absorb hidden business logic.
5. Do not document milestones as sparse file lists only.
6. Do not generate ZIP bundles.
7. Do not repeat manager summaries mechanically; each new summary must reflect what truly changed in the project state.
