# Agro Decision Orchestrator

**Agro-DO** is a modular decision-support product prototype for protected horticulture environments, starting with a realistic greenhouse reference scenario.

The system is designed to help greenhouse owners, managers, technicians, and agronomic advisors make better operational decisions related to irrigation, fertigation, climate control, equipment health, sensor trustworthiness, and intervention prioritization.

This repository is product-oriented. It is not being developed as a thesis-only artifact or as a benchmark-first repository. The goal is to build a modular software foundation that can evolve into a real operator-facing service.

## Current product direction

Agro-DO is being built as **one real service-oriented product**.

This means:
- generative AI is a **mandatory part** of the target architecture,
- deterministic orchestration exists as a **fallback and resilience layer**,
- internal implementation steps are used to build the service in an orderly way,
- but those steps are **not** treated as competing product versions.

## Current service flow

1. Load the greenhouse blueprint.
2. Load a normalized decision case.
3. Validate references and build a minimal execution payload.
4. Generate a recommendation through either:
   - the deterministic fallback orchestrator, or
   - the generative orchestrator backed by OpenAI.
5. Normalize the result into the shared recommendation contract.
6. Apply explicit structural guardrails to the generative output.
7. Apply policy hardening rules for high-risk cases.
8. Fall back to deterministic orchestration if the generative path is unavailable or invalid.

## Current proven capability

The repository has already demonstrated that Agro-DO can:
- load a structured greenhouse environment,
- load realistic operational decision cases,
- validate consistency between environment and case,
- construct a stable execution payload,
- call OpenAI from the local environment,
- generate a structured recommendation,
- govern the generative result through explicit guardrails and fallback behavior,
- apply stricter policy for high-risk cases with an available backup path,
- distinguish between different problem families,
- and respond more cautiously when operational visibility is degraded and signal trust is limited.

## Currently validated case families

### 1. Irrigation failure with backup available
Validated case:
- `inputs/sample_cases/case_main_pump_degradation.json`

Observed governed behavior after policy hardening:
- high priority,
- switch_to_backup,
- human review required,
- high confidence.

### 2. Climate and disease risk without a clear backup path
Validated case:
- `inputs/sample_cases/case_high_humidity_disease_risk.json`

Observed governed behavior:
- high priority,
- adjust_operation,
- human review required,
- high confidence.

### 3. Communication loss with limited trusted visibility
Validated case:
- `inputs/sample_cases/case_communication_loss_partial_blindness.json`

Observed governed behavior:
- high priority,
- escalate_to_human,
- human review required,
- medium confidence.

This confirms that the product can distinguish between:
- a severe problem with continuity fallback,
- a severe problem that requires operational correction,
- and a severe problem where the safest response is to escalate because trusted visibility is degraded.

## Current product conclusion

Agro-DO is no longer only a generative recommendation prototype. It now behaves as a governed service that can distinguish at least three operational patterns:

- **irrigation failure + backup available** → continuity-oriented escalation
- **climate/disease risk + no backup path** → operational adjustment response
- **communication loss + limited trusted visibility** → cautious escalation to human review

This is a meaningful maturity step because it shows that the service is aligning recommendation behavior not only with severity, but also with the operational nature of the problem and with the level of uncertainty in the available information.

## Current open product question

The next important question is not whether policy hardening is needed, but how broadly it should be extended across additional realistic scenarios.

The highest-value next step is:
- add more realistic cases,
- test whether current policy remains coherent across those cases,
- and only then continue tightening guardrails where the service still behaves too softly or too confidently.

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
│   │   ├── case_main_pump_degradation.json
│   │   ├── case_high_humidity_disease_risk.json
│   │   └── case_communication_loss_partial_blindness.json
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

## Main design principles

- **Product-first mindset**
- **Generative core with governed behavior**
- **Deterministic fallback**
- **Explicit service policy**
- **Modular architecture**
- **Explicit contracts**
- **Traceable evolution**

## Current implementation phases

### Phase 1 — Repository bootstrap
Completed.

### Phase 2 — Domain contracts
Completed.

### Phase 3 — Digital plantation MVP
Completed.

### Phase 4 — Decision-case modeling
Completed for three realistic case families.

### Phase 5 — Bridge MVP
Completed.

### Phase 6 — Generative orchestration base
Completed.

### Phase 7 — Policy hardening
In progress and already validated on multiple case families, including degraded-visibility scenarios.

### Phase 8 — Service entry path
Pending.

### Phase 9 — UI MVP
Pending.

## Documentation workflow

Update order for each major milestone:
1. `docs/project_log.md`
2. `README.md`
3. `docs/lessons_learned.md` when applicable
4. `docs/handoff/current_handoff.md`
5. Git commit and GitHub push

For cumulative memory files:
- `docs/project_log.md` and `docs/lessons_learned.md` must be treated as append-only by default,
- never replaced by shortened summaries,
- and always checked for continuity before commit.

## Current status

Current repository stage:
- domain layer implemented,
- reference greenhouse blueprint implemented,
- three realistic sample cases implemented,
- bridge loading path implemented,
- recommendation contract implemented,
- deterministic fallback orchestrator implemented,
- OpenAI integration implemented,
- governed generative orchestrator validated locally,
- first explicit policy-hardening rule implemented and validated,
- three case families now confirm differentiated governed behavior.

Immediate next objective:
- continue broadening policy hardening through additional realistic cases,
- especially to verify that current confidence and escalation behavior generalize beyond the first three validated patterns.

## Language and documentation conventions

- All repository files must be written in **English**.
- Code comments and internal documentation must be written in **English**.
- Variable names, parameters, and identifiers must be written in **English**.
- Conversations with the project manager may remain in **Spanish**.
