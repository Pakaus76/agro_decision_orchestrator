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
6. Apply explicit guardrails to the generative output.
7. Apply policy hardening rules for high-risk cases.
8. Fall back to deterministic orchestration if the generative path is unavailable or invalid.

## Current proven capability

The repository has already demonstrated that Agro-DO can:
- load a structured greenhouse environment,
- load a realistic operational decision case,
- validate consistency between both,
- construct a stable execution payload,
- call OpenAI from the local environment,
- generate a structured recommendation,
- govern the generative result through explicit guardrails and fallback behavior,
- and harden policy for specific high-risk operational patterns.

## Current open product question

A first explicit policy rule has already been implemented and validated:
- when a case is **high** or **critical**
- and an available **backup path** exists,
- the product must not remain in soft-response modes such as:
  - `inspect`,
  - `continue_with_monitoring`,
  - `no_action`.

The current implementation escalates such cases to a stronger response, currently `switch_to_backup`.

The next open question is how broadly and consistently similar policy rules should be extended across additional realistic scenarios.

## Current status

Current repository stage:
- domain layer implemented,
- reference greenhouse blueprint implemented,
- first sample case implemented,
- bridge loading path implemented,
- recommendation contract implemented,
- deterministic fallback orchestrator implemented,
- OpenAI integration implemented,
- governed generative orchestrator validated locally,
- first explicit policy-hardening rule implemented and validated.

Immediate next objective:
- broaden policy hardening with at least one additional realistic case,
- so product strictness does not depend on a single scenario.
