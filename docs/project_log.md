# Project Log

## Project
**Name:** Agro Decision Orchestrator  
**Short name:** Agro-DO  
**Working subtitle:** Advanced decision support for greenhouse irrigation, climate, and fertigation systems

## Purpose of this log
This file records major project milestones, important decisions, relevant test results, and project-manager comments in chronological order.

The log must explain:
- what was done,
- why it mattered,
- why that step happened at that moment,
- what it enables next.

## Update policy
1. `docs/project_log.md`
2. `README.md`
3. `docs/lessons_learned.md` when applicable
4. `docs/handoff/current_handoff.md`
5. Git commit and GitHub push

## Chronological entries

### [LOG-013]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** Real orchestrator module implemented as the first service-level decision engine

**What was done**  
The repository added `src/agro_do/decision_orchestrator/orchestrator.py` as the first real recommendation engine of Agro-DO. This module takes a validated execution payload and produces a normalized recommendation using the shared output contract.

**Why this was needed**  
Up to that point, the project could already model the greenhouse, model a decision case, validate their consistency, and build a payload. What was still missing was the first module capable of turning that validated input into an operational recommendation. Without this step, the project would still describe situations but not respond to them.

**Why this happened now**  
This became the correct next step once the environment contract, decision-case contract, recommendation contract, sample case, and bridge loader were all already validated. At that moment the architecture was ready for a real decision engine instead of more structural preparation.

**What this enables next**
- service-level recommendation generation
- fallback behavior for future generative integration
- clearer operator-facing output design
- future persistence, API, and UI execution around a real recommendation path

**Files affected**
- `src/agro_do/decision_orchestrator/orchestrator.py`

**Project manager comment / voice note**
- None recorded.

### [LOG-014]
**Date:** 2026-04-11  
**Type:** decision  
**Title:** Generative AI confirmed as mandatory in the target product architecture

**What was done**  
The project explicitly clarified that Agro-DO must include generative AI as part of its target architecture. The deterministic orchestration path was kept, but only as a fallback and robustness mechanism rather than as the destination of the product.

**Why this was needed**  
A temporary ambiguity appeared after the first deterministic recommendation flow was implemented. That ambiguity risked creating the false impression that the current deterministic orchestrator might itself be the intended product endpoint. This had to be corrected immediately because the user had already defined that the final service must behave like the most advanced governed generative logic of the previous repository.

**Why this happened now**  
The clarification became necessary exactly when the architecture reached the point where both a deterministic path and a future generative path were conceptually possible. That made it the correct moment to lock the product direction and avoid future drift.

**What this enables next**
- OpenAI integration as a core architectural component
- governed generative orchestration instead of optional add-on behavior
- correct framing of the deterministic layer as fallback only
- stronger alignment between implementation choices and commercial product ambition

**Files affected**
- `README.md`
- `docs/project_log.md`
- `docs/lessons_learned.md`
- `docs/handoff/current_handoff.md`

**Project manager comment / voice note**
- The target Agro-DO service must use generative AI. The deterministic path remains important only as a governed fallback and safety mechanism.

### [LOG-015]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** OpenAI integration layer and generative orchestrator implemented

**What was done**  
The repository added a dedicated integration layer for OpenAI in `src/agro_do/integrations/openai_client.py`, updated local configuration through `.env.example`, added the `openai` dependency to `pyproject.toml`, and implemented `src/agro_do/decision_orchestrator/llm_orchestrator.py`. The decision orchestrator package was also updated to export both the deterministic and generative entry points.

**Why this was needed**  
Once the project direction was clarified, the product required a real technical path for generative reasoning. It was no longer enough to say that Agro-DO would eventually use generative AI. The codebase needed a real adapter to OpenAI, a real generative orchestration layer, and a controlled fallback path so that the service could behave coherently under both normal and failure conditions.

**Why this happened now**  
This happened now because the project had already completed all necessary preconditions: normalized inputs, validated execution payloads, and normalized recommendation outputs. That meant the architecture was finally stable enough to integrate OpenAI without turning the system into an uncontrolled prompt experiment.

**What this enables next**
- real generative recommendation generation
- governed JSON outputs from the LLM layer
- deterministic fallback for robustness
- future guardrails, policy checks, and richer case handling

**Files affected**
- `src/agro_do/integrations/__init__.py`
- `src/agro_do/integrations/openai_client.py`
- `src/agro_do/decision_orchestrator/llm_orchestrator.py`
- `src/agro_do/decision_orchestrator/__init__.py`
- `.env.example`
- `pyproject.toml`

**Project manager comment / voice note**
- None recorded.

### [LOG-016]
**Date:** 2026-04-11  
**Type:** test-result  
**Title:** End-to-end OpenAI-backed recommendation path validated locally

**What was done**  
The full generative path was executed successfully in the local environment using the user's real `.env` configuration. The system loaded the reference greenhouse blueprint, loaded the main pump degradation case, built the validated execution payload, called OpenAI through the generative orchestrator, and returned a structured recommendation.

**Why this was needed**  
This was the first real proof that the product had moved beyond architectural preparation and into functioning generative service behavior. Until this test, the generative path existed in code but had not yet been proven to work end to end in the actual local environment.

**Why this happened now**  
This test was correctly executed immediately after the OpenAI adapter, configuration, and generative orchestrator were in place. Waiting longer would have delayed the most important architectural confirmation of the current phase.

**What this enables next**
- hardening guardrails around generative outputs
- expanding the case library
- designing service entry points around a real generative core
- preparing persistence, API, and UI layers on top of a validated generative path

**Files affected**
- no new source file was required for the validation itself; the result validates the current implementation path

**Project manager comment / voice note**
- Since the repository bootstrap phase, the project has evolved from a structured concept into the first working foundation of a real generative decision-support service for greenhouse operations. The initial work focused on building a reliable architectural base: stable domain contracts were created for the greenhouse environment, the decision case, and the recommendation output. This established a shared language for the system, ensuring that future components would not rely on inconsistent or improvised representations of assets, sectors, sensors, actuators, crop context, cases, or recommendations.
- A realistic reference greenhouse blueprint was then defined for the MVP. This blueprint describes a tomato greenhouse in substrate with three sectors, irrigation, fertigation, climate-related assets, sensors, and actuators. This step transformed the project from an abstract design into a concrete operational environment that the system can load, validate, and reason about. In parallel, the first realistic decision case was created around main irrigation pump degradation, allowing the project to represent not only the greenhouse itself, but also a meaningful operational problem that requires action.
- The next major milestone was the creation of the bridge loading path. This loader reads the greenhouse blueprint, reads the decision case, validates both through the domain contracts, checks cross-reference consistency, and builds a minimal execution payload. This was an important turning point because it demonstrated that the architecture was no longer a collection of isolated files and models. It had become a first controlled pipeline capable of connecting environment, case, and execution context in a coherent way.
- A recommendation contract was then introduced to formally define what the system must produce as output. This was an important architectural decision because it forced the project to define the structure of a recommendation before expanding the service logic. Priority, action type, rationale, confidence, human review requirement, next checks, implicated assets, and decision trace were all standardized, which means the service output is now stable and suitable for future API, UI, persistence, and audit needs.
- At that point, an explicit product-direction correction was made. It was decided that Agro-DO must not inherit the experimental A/B/C/F versioning logic of the previous scientific repository. Instead, Agro-DO is being built as one real service-oriented product whose internal implementation may advance in stages, but without turning those stages into competing product variants. This was a critical decision because it aligned the project with its true commercial ambition and prevented the architecture from drifting into a thesis-style mindset.
- With that direction clarified, the first real orchestration logic was implemented. A deterministic orchestrator was created as an internal safety layer capable of generating structured recommendations from validated payloads. This was never treated as the final product, but as a governed fallback and a control baseline needed for service robustness. Its existence ensured that the future generative layer would be integrated on top of a stable and inspectable decision path rather than on top of uncontrolled behavior.
- The project then advanced into the generative phase. An OpenAI integration layer was created, local environment-based configuration was prepared, and a generative orchestrator was implemented to build prompts from validated payloads, request JSON responses from OpenAI, normalize them into the recommendation contract, and fall back to the deterministic path when necessary. This was a decisive step because it introduced the real mechanism through which Agro-DO can behave as a generative decision-support service instead of only as a deterministic rules engine.
- The most important validation achieved so far is that the full generative path has already worked successfully in the local environment. The system was able to load the greenhouse blueprint, load the decision case, construct the execution payload, call OpenAI using the configured API key, and return a usable recommendation with priority, action type, confidence, next checks, and decision trace. The result was operationally coherent for the tested case: the system identified the situation as high priority, recommended switching to the backup pump, required human review, and generated a concise action summary aligned with the greenhouse context. This confirms that the generative layer is not only architecturally present, but already functioning in practice.
- The main conclusions at this stage are clear. First, the project has successfully moved beyond static modeling and now behaves as an actual decision-support service prototype. Second, the architecture has proven viable because domain contracts, blueprint loading, case loading, validation, deterministic fallback, and generative reasoning are already connected into one coherent flow. Third, the product direction has been clarified and protected: Agro-DO is a single service-oriented product with a governed generative core, not an experimental sequence of product versions. Fourth, the deterministic layer remains valuable, but only as a fallback and control mechanism within the service, not as the product endpoint.
- The key decisions taken during this phase are also now established. The project will continue to evolve as a commercially oriented product. Generative AI is a mandatory part of the target architecture, not an optional add-on. The deterministic orchestration path will remain for resilience and fallback. Chronological traceability across project log, README, lessons learned, and handoff remains mandatory. All major implementation steps must continue to be explained not only in terms of what was built, but also why it was needed, why it was built at that moment, and what it enables next.
- At the current point, Agro-DO already has the first meaningful foundation of a real service: a structured agricultural environment, normalized operational cases, validated payload construction, deterministic fallback, and a working generative orchestration path connected to OpenAI. The next logical steps are no longer foundational redesign, but product deepening: strengthen guardrails, expand the case library, and move progressively toward a more complete service entry path that can later support API and UI execution in a robust way.
