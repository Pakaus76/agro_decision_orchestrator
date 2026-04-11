# Project Log

## Project
**Name:** Agro Decision Orchestrator  
**Short name:** Agro-DO  
**Working subtitle:** Advanced decision support for greenhouse irrigation, climate, and fertigation systems

## Purpose of this log
This file records major project milestones, key decisions, relevant test outcomes, and project-manager comments in chronological order.

It must explain not only what was done, but also why it mattered, why that step was taken at that moment, and what it enables next.

## Update policy
1. `docs/project_log.md`
2. `README.md`
3. `docs/lessons_learned.md` when applicable
4. `docs/handoff/current_handoff.md`
5. Git commit and GitHub push

## Chronological entries

### [LOG-011]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** Recommendation output contract added

**What was done**  
The repository added the recommendation output contract in `recommendation.py` and integrated it into the domain package exports.

**Why this was needed**  
Before writing real orchestration logic, the project needed to define what a recommendation should look like. Without a stable output contract, early logic would likely return improvised and inconsistent structures.

**Why this happened now**  
This was the correct next step after validating the bridge loader because the next architectural need was to define the orchestrator output before implementing the orchestrator itself.

**What this enables next**
- controlled recommendation generation
- consistent persistence and UI rendering
- real orchestrator implementation

**Files affected**
- `src/agro_do/domain/recommendation.py`
- `src/agro_do/domain/__init__.py`

**Project manager comment / voice note**
- None recorded.

### [LOG-012]
**Date:** 2026-04-11  
**Type:** decision  
**Title:** Product direction corrected away from thesis-style versioning

**What was done**  
A naming and architectural correction was made after detecting a drift toward a thesis-style sequence of internal conditions or versions. The file `condition_a.py` was explicitly rejected as part of the product direction and removed from the implementation path. The project reaffirmed that Agro-DO must be built as one real service-oriented product, not as a visible ladder of A/B/C/F-style variants.

**Why this was needed**  
This correction was important because the previous industrial thesis repository created a strong conceptual habit around progressive benchmark conditions. That habit does not fit the purpose of this product. If left uncorrected, it would gradually distort naming, architecture, documentation, and future UI/API behavior.

**Why this happened now**  
The drift was detected exactly when the first orchestrator implementation was about to begin. That made it the correct moment to correct the direction, before a wrong naming scheme and wrong product framing could spread through the codebase and the documentation.

**What this enables next**
- creation of a real `orchestrator.py`
- service-oriented internal architecture
- cleaner product identity and future monetizable positioning

**Files affected**
- `src/agro_do/decision_orchestrator/condition_a.py` (discarded)
- `README.md`
- `docs/project_log.md`
- `docs/lessons_learned.md`
- `docs/handoff/current_handoff.md`

**Project manager comment / voice note**
- The project must not evolve as a scientific sequence of versions A, B, C, D, E, or F. The objective is to build directly the real Agro-DO service that we would eventually want to exploit commercially. Internal steps may still exist, but only as controlled construction steps, not as product variants.
