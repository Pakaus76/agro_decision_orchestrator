# Lessons Learned

## Purpose of this file
This file captures stable working rules and reusable project lessons that should influence future interactions, implementation steps, documentation discipline, and handoffs.

## Lessons

### [LESSON-004]
**Title:** Manager summaries must be cumulative without repeating the same wording

**Rule to preserve**  
Project-manager summaries must accumulate progress and explain the real delta of the current milestone. They should not mechanically repeat the same introduction or the same sequence of ideas at each update.

### [LESSON-005]
**Title:** Product projects must not inherit experimental version ladders from thesis repositories

**Context**  
During the first attempt to create orchestration logic, the project briefly drifted toward a thesis-style naming pattern such as `condition_a.py`, inherited from the previous industrial research repository.

**Rule to preserve**  
This agricultural project must be built as one real Agro-DO product. Internal implementation steps may exist, but they must not be framed, named, or documented as visible benchmark conditions or product variants such as A/B/C/D/E/F.

**Why this matters**
- protects the product identity
- avoids research-oriented drift
- keeps the architecture aligned with a future service that can be deployed and monetized

### [LESSON-006]
**Title:** Chronological traceability must explain intent, timing, and consequences

**Rule to preserve**  
Project chronology must never read like a terse technical checklist. Major milestones must explain what was built, why it mattered, why it was the correct step at that moment, and what the step enables next.

**Why this matters**
- makes the project understandable to non-specialists
- improves handoff quality between assistants
- keeps technical execution aligned with business intent

### [LESSON-007]
**Title:** In this product, generative AI is mandatory, not optional

**Context**  
A temporary ambiguity appeared after the deterministic orchestrator was validated, creating the risk of treating the deterministic path as a possible endpoint of the product.

**Rule to preserve**  
The target Agro-DO product must include a governed generative core. Deterministic logic remains valuable, but only as fallback, control, and resilience infrastructure.

**Why this matters**
- protects the actual product ambition
- prevents the service from drifting into a purely rules-based endpoint
- keeps architecture and business direction aligned from the start

### [LESSON-008]
**Title:** Deliver markdown files individually and do not use ZIP bundles

**Rule to preserve**  
When updated documentation files are delivered to the user, they must be provided individually. Auxiliary ZIP bundles should not be used in this project.

**Why this matters**
- reduces friction in the user's workflow
- avoids accidental versioning of irrelevant bundles
- keeps delivery aligned with the user's execution style in Visual Studio Code
