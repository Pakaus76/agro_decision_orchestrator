# Current Handoff — Agro Decision Orchestrator

## 1. Purpose of this handoff

This file is intended to let another LLM continue the work without losing architectural continuity, product intent, repository discipline, or execution style.

The assistant that receives this handoff must understand that this project is being built from scratch in Visual Studio Code with the user acting as project manager and executor, while the assistant provides structured technical guidance.

The project is not a thesis artifact. It is a product-oriented agricultural decision-support prototype intended to evolve toward a realistic operator-facing platform.

---

## 2. Project ambition

The target product is a modular agricultural decision-support platform for protected horticulture environments.

Its purpose is to transform greenhouse operational context into prioritized, explainable, and actionable recommendations related to:
- irrigation,
- fertigation,
- climate control,
- actuator and sensor reliability,
- equipment health,
- intervention prioritization.

The long-term ambition is to build a system that could evolve toward:
- SaaS-style productization,
- operator-facing dashboards,
- configurable scenario execution,
- historical run traceability,
- richer governed reasoning,
- future predictive or AI extensions.

---

## 3. Non-negotiable operating rules

The following rules are already fixed and must be preserved:

1. The user executes locally in **Visual Studio Code**.  
   The assistant acts as the user's technical assistant.

2. The assistant must guide the work **step by step**:
   - one objective at a time,
   - one step at a time,
   - exact shell or PowerShell command first,
   - then exact text to paste when needed,
   - expected output must always be stated,
   - do not move forward until the current step is validated.

3. All project files must be written in **English**:
   - `.md`,
   - `.py`,
   - `.csv`,
   - configuration files,
   - comments,
   - identifiers,
   - variable names,
   - parameters.

4. The conversation with the user remains in **Spanish**.

5. The repository must live in **GitHub** and be kept synchronized through normal version-control discipline.

6. Three core documentation files must always be kept synchronized:
   - `docs/project_log.md`
   - `README.md`
   - `docs/handoff/current_handoff.md`

7. A fourth knowledge-preservation file must also exist:
   - `docs/lessons_learned.md`

8. Update order for meaningful milestones:
   1. `docs/project_log.md`
   2. `README.md`
   3. `docs/lessons_learned.md` when applicable
   4. `docs/handoff/current_handoff.md`
   5. Git commit and GitHub push

9. If reusable knowledge emerges, `docs/lessons_learned.md` must be updated and then reflected in the handoff.

10. Before a major log update, the user must have the opportunity to add:
   - a project-manager comment,
   - a note,
   - or a voice-note transcript.

11. The root `README.md` must always remain useful and current.  
    It must explain:
   - what the project is,
   - why it exists,
   - how it is structured,
   - where key files live,
   - how to use current capabilities,
   - how to interpret outputs,
   - and it must contain an up-to-date repository tree.

12. Markdown files are preferably delivered to the user as attached files when practical, because long inline markdown is inconvenient in the chat UI.

---

## 4. Current architectural direction

The product is organized around three explicit planes:

### 4.1. Digital Plantation
A structured representation of the greenhouse environment, including:
- greenhouse structure,
- sectors,
- assets,
- sensors,
- actuators,
- crop context,
- external weather,
- incidents,
- operational constraints.

### 4.2. Decision Orchestrator
A reasoning layer that consumes a normalized agricultural decision case and produces:
- priority,
- recommended action,
- rationale,
- confidence,
- alternatives,
- human-review requirement,
- traceability.

### 4.3. Bridge
A thin and explicit layer that:
- reads cases from the digital plantation,
- normalizes them into a stable decision-case contract,
- invokes one or more decision policies,
- persists outputs,
- supports future comparisons and reporting.

The bridge must not silently introduce business logic or semantic changes.

---

## 5. Canonical reference environment

The initial MVP must start with one realistic but manageable environment:

- tomato greenhouse,
- substrate cultivation,
- 3 sectors,
- drip irrigation,
- fertigation,
- automatic ventilation,
- circulation fans,
- shading screen,
- basic irrigation and climate sensing.

This is the canonical baseline and should guide the first domain models, blueprints, and cases.

---

## 6. Current repository design

Planned repository structure:

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

## 7. Work completed so far

### Completed
- Project vision defined as product-oriented rather than thesis-oriented.
- Canonical reference environment selected.
- Local project folder created.
- Local Git repository initialized.
- Branch normalized to `main`.
- Base repository structure created.
- Empty structural directories preserved with `.gitkeep` files where needed.
- Documentation discipline fixed.
- Project log created.
- README created.
- Lessons-learned registry adopted and created.
- Current handoff created.
- `.gitignore` configured.
- `pyproject.toml` configured.
- Base Python package skeleton created.

### In progress
- Repository bootstrap is complete and ready to be committed.
- Core documentation is being synchronized with the latest milestone closure.

### Not started yet
- Stable domain contracts.
- First greenhouse blueprint.
- First commit.
- GitHub remote creation and push.

---

## 8. Immediate next objective

The correct immediate objective is:

**Finish the bootstrap documentation and repository skeleton, then define the first stable domain contracts and the first greenhouse blueprint.**

This means the next correct sequence is:

1. finish synchronizing `docs/project_log.md`,
2. finish synchronizing `README.md`,
3. update `docs/lessons_learned.md` when a reusable lesson applies,
4. finish synchronizing `docs/handoff/current_handoff.md`,
5. create the first commit,
6. create the GitHub repository and push,
7. define the first stable domain contracts,
8. create the first greenhouse blueprint.

Only after that should richer application logic be created.

---

## 9. Planned implementation path

### Phase 1 — Repository bootstrap
Create:
- repository structure,
- core docs,
- base package,
- Git discipline.

### Phase 2 — Domain contracts
Define:
- greenhouse,
- sector,
- asset,
- sensor,
- actuator,
- crop profile,
- decision case,
- recommendation.

### Phase 3 — Digital plantation MVP
Create:
- first greenhouse blueprint,
- first structured input files,
- initial sample cases.

### Phase 4 — Deterministic decision orchestrator MVP
Implement:
- transparent baseline policy,
- explainable rule-based outputs.

### Phase 5 — Bridge MVP
Implement:
- case loading,
- normalization,
- policy invocation,
- output persistence.

### Phase 6 — UI MVP
Implement:
- scenario selection,
- run execution,
- recommendation view,
- history page.

### Phase 7 — Expert elicitation support
Create:
- interview packs,
- transcript distillation templates,
- knowledge extraction workflows.

### Phase 8 — Richer decision logic
Add:
- more context-sensitive conditions,
- governed escalation and review behavior.

### Phase 9 — Optional predictive or AI layer
Only after the deterministic product foundation is stable.

---

## 10. Product and knowledge discipline

This assistant handoff must always remain coordinated with:
- `docs/project_log.md`,
- `README.md`,
- `docs/lessons_learned.md`.

The handoff must preserve:
- project ambition,
- plan and subphases,
- progress versus plan,
- decisions taken,
- pending decisions,
- test outcomes,
- reusable lessons,
- project-manager comments and voice-note transcripts when available.

---

## 11. Known user preferences that affect execution

- The user prefers practical execution over abstract discussion.
- The user wants exact commands and expected outputs.
- The user does not want large undocumented jumps.
- When new files are created, shell or PowerShell commands should be provided.
- For technical work, files and structured content must remain in English.
- Markdown files are better delivered as attached files than pasted inline in the chat UI.
- The assistant must behave as an execution partner, not as a detached advisor.

---

## 12. Pending decisions

The following decisions still need to be made later:
- final backend dependency set beyond the current bootstrap baseline,
- initial FastAPI structure timing,
- initial frontend stack timing,
- persistence choice for early MVP (`JSON`/`CSV` only vs `SQLite`),
- naming details for first blueprint files,
- shape of the first decision-case schema,
- shape of the first recommendation schema.

These decisions should be taken only when the project reaches the corresponding step.

---

## 13. Current checkpoint summary

At this checkpoint, the project has:
- a clear product vision,
- a clear greenhouse baseline,
- a strict documentation workflow,
- a handoff discipline,
- a lessons-learned discipline,
- and a stepwise execution method.

The next assistant must not skip ahead into AI layers, frontend overdesign, or abstract agricultural overmodeling.

The next correct move is still:
**complete bootstrap documentation and repository skeleton first.**

---

## 14. Latest milestone note

The initial repository bootstrap has been completed successfully.

Project manager comment recorded for this milestone:
- "We are starting the project now that the repository structure has been created."
