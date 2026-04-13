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
- respond more cautiously when operational visibility is degraded and signal trust is limited,
- stop automated behavior when the digital control state may not match physical reality,
- escalate for expert review when the core issue is misleading sensor behavior,
- and identify serious resource-continuity risk even before a full irrigation failure is confirmed.

## Currently validated case families

### 1. Irrigation failure with backup available
Validated case:
- `inputs/sample_cases/case_main_pump_degradation.json`

Observed governed behavior:
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

### 4. Manual override mismatch between digital state and physical reality
Validated case:
- `inputs/sample_cases/case_manual_override_mismatch.json`

Observed governed behavior:
- high priority,
- stop_and_review,
- human review required,
- medium confidence.

### 5. Sensor drift or flatline affecting decision trust
Validated case:
- `inputs/sample_cases/case_sensor_drift_flatline.json`

Observed governed behavior:
- high priority,
- escalate_to_human,
- human review required,
- medium confidence.

### 6. Low water reserve and uncertain supply continuity
Validated case:
- `inputs/sample_cases/case_low_tank_supply_uncertainty.json`

Observed governed behavior:
- high priority,
- stop_and_review,
- human review required,
- high confidence.

This confirms that the product can distinguish between:
- a severe problem with continuity fallback,
- a severe problem that requires operational correction,
- a severe problem where the safest response is human escalation under degraded visibility,
- a severe problem where automation should be halted until physical reality is verified,
- a severe problem where the main risk is acting on misleading sensor data,
- and a serious continuity threat caused by resource depletion before full mechanical failure occurs.

## Current product conclusion

Agro-DO is no longer only a generative recommendation prototype. It now behaves as a governed service that can distinguish at least six operational patterns:

- irrigation failure + backup available → continuity-oriented escalation
- climate/disease risk + no backup path → operational adjustment response
- communication loss + limited trusted visibility → cautious escalation to human review
- manual override mismatch → stop-and-review behavior with physical verification emphasis
- sensor drift / flatline → expert escalation focused on data trust
- low tank / uncertain supply continuity → strong interruption-oriented response to reserve risk

This is a meaningful maturity step because it shows that the service is aligning recommendation behavior not only with severity, but also with the operational nature of the problem, the quality of visibility, the trustworthiness of both digital state and sensor data, and the near-term continuity risk of essential resources.

## Current open product question

The next important question is not whether policy hardening is needed, but how precisely it should be tuned across additional realistic scenarios.

The low-tank case was especially useful because it showed both a strength and a refinement opportunity:
- the service correctly recognized serious continuity risk,
- but its current stop_and_review response may be stricter than ideal for a resource-shortage scenario that might benefit from more graduated continuity-management logic.

The highest-value next step is:
- add more realistic cases,
- test whether current policy remains coherent across those cases,
- and then refine guardrails where the service is still too soft, too confident, or too abrupt.

## Current status

Current repository stage:
- domain layer implemented,
- reference greenhouse blueprint implemented,
- six realistic sample cases implemented,
- bridge loading path implemented,
- recommendation contract implemented,
- deterministic fallback orchestrator implemented,
- OpenAI integration implemented,
- governed generative orchestrator validated locally,
- explicit policy-hardening rules implemented and validated,
- six case families now confirm differentiated governed behavior.

Immediate next objective:
- continue broadening policy hardening through additional realistic cases,
- especially to refine how the service should respond to continuity-risk scenarios that are serious but may still allow controlled mitigation instead of immediate stop behavior.
