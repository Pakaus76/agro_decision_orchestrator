# Project Log

## Project
**Name:** Agro Decision Orchestrator  
**Short name:** Agro-DO  
**Working subtitle:** Advanced decision support for greenhouse irrigation, climate, and fertigation systems

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
**Title:** Generative orchestration path connected to OpenAI

**What happened**  
The project gained an OpenAI integration layer, local environment-based configuration, a deterministic fallback orchestrator, and a generative orchestrator capable of building prompts from the validated payload and normalizing OpenAI output into the shared recommendation contract.

**Why this was needed**  
Generative AI is a mandatory part of the target architecture, so the project needed to move beyond static preparation and actually connect the service to a real model provider.

**Why it happened at this moment**  
The foundational layers were already in place: environment, case, bridge payload, and recommendation contract.

**What this enables next**  
It allows real local execution of generative recommendations and creates the basis for future policy hardening.

**Files affected**
- `src/agro_do/decision_orchestrator/orchestrator.py`
- `src/agro_do/decision_orchestrator/llm_orchestrator.py`
- `src/agro_do/integrations/openai_client.py`
- `.env.example`
- `pyproject.toml`

**Project manager comment / voice note**
- Since the repository bootstrap phase, the project has evolved from a structured concept into the first working foundation of a real generative decision-support service for greenhouse operations.

### [LOG-014]
**Date:** 2026-04-11  
**Type:** test-result  
**Title:** Real local generative recommendation successfully executed

**What happened**  
The full local flow succeeded using the real OpenAI API configuration. The system loaded the greenhouse blueprint, loaded the decision case, built the validated execution payload, called OpenAI, and returned a usable recommendation.

**Why this was needed**  
Architectural preparation alone was not enough. The project needed proof that the generative path worked in practice in the real local environment.

**Why it happened at this moment**  
This could only happen after the integration layer, environment variables, and generative orchestrator were already implemented.

**What this enables next**  
It proves that Agro-DO can already behave as a real generative service prototype and makes it worthwhile to invest in guardrails rather than more plumbing.

**Files affected**
- runtime validation only

**Project manager comment / voice note**
- The generative layer is no longer only planned or prepared. It already works in practice in the local environment.

### [LOG-015]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** Governed generative orchestrator validated

**What happened**  
The generative orchestrator was rewritten with explicit guardrails and validated successfully through a new real local execution. The governed version now enforces minimum structural quality, constrains recommendation quality, reduces confidence under poor visibility or untrusted signals, forces human review for risky actions, and falls back to the deterministic path when the generative result is invalid or unsafe.

**Why this was needed**  
A generative recommendation path is valuable only if it is also trustworthy. After proving that OpenAI integration worked, the next necessary step was to prevent weak or incoherent outputs from being accepted too easily.

**Why it happened at this moment**  
This was the right next step because the architecture had already proven that it could generate real recommendations. The next priority was therefore product reliability, not more structural expansion.

**What this enables next**  
It shifts the project from a merely working generative prototype toward a governed decision-support service and reveals the next policy question the product must settle.

**Files affected**
- `src/agro_do/decision_orchestrator/llm_orchestrator.py`

**Project manager comment / voice note**
- Since the previous major milestone, the project has moved from having a first working generative path to having a more governed and product-aligned generative service architecture.

### [LOG-016]
**Date:** 2026-04-11  
**Type:** decision  
**Title:** Product-policy hardening identified as the next critical step

**What happened**  
The latest governed generative test produced a coherent result, but it also exposed an important product-policy question: when severity is high and a backup path is available, should the product allow an inspect-first recommendation, or should policy force a stronger operational response?

**Why this was needed**  
This question must be recognized explicitly, because it is not a technical bug. It is a service-policy decision that affects how strict the product should be in high-risk situations.

**Why it happened at this moment**  
The question only became visible after the generative path was both functional and governed enough to produce credible recommendations.

**What this enables next**  
It gives the project a clear next focus: policy hardening and stronger high-risk guardrails rather than architectural redesign.

**Files affected**
- future orchestration policy work
- future documentation updates

**Project manager comment / voice note**
- The current architecture is already viable. The next phase should deepen product reliability and policy strictness rather than reopen foundational design.
