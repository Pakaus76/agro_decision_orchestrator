# Project Log

## Project
**Name:** Agro Decision Orchestrator  
**Short name:** Agro-DO  
**Working subtitle:** Advanced decision support for greenhouse irrigation, climate, and fertigation systems

## Purpose of this log
This file records major project milestones, key decisions, relevant test outcomes, and project-manager comments in chronological order.

It is not intended to capture every micro-step.  
It should be updated when:
- a meaningful objective is completed,
- a relevant architectural or product decision is made,
- a test produces a result worth preserving,
- the project manager adds a comment or voice note transcript that should remain traceable.

## Update policy
When a major update is needed, the update sequence must always be:
1. `docs/project_log.md`
2. `README.md`
3. `docs/handoff/current_handoff.md`
4. Git commit and GitHub push

When a lesson learned must be preserved for future work, `docs/lessons_learned.md` should also be updated and then reflected in the handoff document.

## Entry template

### [ENTRY-ID]
**Date:** YYYY-MM-DD  
**Type:** milestone | decision | test-result | project-manager-note  
**Title:** Short descriptive title

**Summary**  
Brief description of what was achieved, decided, or observed.

**Details**
- Scope:
- Files affected:
- Expected impact:
- Follow-up needed:

**Project manager comment / voice note**
- None recorded.

---

## Chronological entries

### [LOG-001]
**Date:** 2026-04-11  
**Type:** decision  
**Title:** Project operating rules established

**Summary**  
The operating rules for the project were explicitly defined before implementation work started.

**Details**
- Scope: project governance, documentation workflow, repository discipline, language conventions
- Files affected: pending initial creation of core documentation files
- Expected impact: improved continuity, traceability, maintainability, and smoother handoff between LLM assistants
- Follow-up needed: reflect these rules in README and handoff

**Project manager comment / voice note**
- None recorded.

### [LOG-002]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** Local repository bootstrap started

**Summary**  
The project root folder was created and a local Git repository was initialized successfully.

**Details**
- Scope: local bootstrap
- Files affected: repository root and `.git/`
- Expected impact: the project can now evolve under version control from the start
- Follow-up needed: create initial documentation set and base Python package structure

**Project manager comment / voice note**
- None recorded.

### [LOG-003]
**Date:** 2026-04-11  
**Type:** decision  
**Title:** Initial product scope fixed

**Summary**  
The project scope was fixed around a product-oriented agricultural decision-support system rather than a thesis-style benchmark artifact.

**Details**
- Scope: product vision and architectural direction
- Files affected: to be reflected in README and handoff
- Expected impact: keeps implementation focused on user value, workflows, explainability, and modular product design
- Follow-up needed: define the initial greenhouse reference blueprint and core domain contracts

**Project manager comment / voice note**
- None recorded.

### [LOG-004]
**Date:** 2026-04-11  
**Type:** decision  
**Title:** Canonical reference environment selected

**Summary**  
The canonical starting environment was defined as a tomato greenhouse in substrate with three sectors, drip irrigation, fertigation, automatic ventilation, circulation fans, shading screen, and basic climate and irrigation sensing.

**Details**
- Scope: domain baseline
- Files affected: future blueprint files and domain models
- Expected impact: provides a realistic but manageable starting point for the MVP
- Follow-up needed: encode this reference environment as the first greenhouse blueprint

**Project manager comment / voice note**
- None recorded.

### [LOG-005]
**Date:** 2026-04-11  
**Type:** decision  
**Title:** Markdown delivery and lessons learned registry adopted

**Summary**  
Markdown files should be delivered as attached files whenever practical, and a dedicated lessons-learned registry should be maintained for reusable project knowledge.

**Details**
- Scope: assistant workflow, documentation handling, cross-LLM continuity
- Files affected: `docs/lessons_learned.md`, `README.md`, `docs/handoff/current_handoff.md`
- Expected impact: easier document handling in the chat interface and better preservation of reusable operating knowledge
- Follow-up needed: include the lessons-learned file in the repository structure and handoff discipline

**Project manager comment / voice note**
- None recorded.

### [LOG-006]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** Initial repository bootstrap completed

**Summary**  
The initial repository bootstrap was completed successfully, including the base folder structure, core documentation scaffold, package skeleton preservation, branch normalization to `main`, and baseline project configuration.

**Details**
- Scope: repository bootstrap, documentation baseline, packaging baseline, version-control normalization
- Files affected: `README.md`, `docs/project_log.md`, `docs/lessons_learned.md`, `docs/handoff/current_handoff.md`, `.gitignore`, `pyproject.toml`, `src/`, `app/`, `inputs/`, `outputs/`, `scripts/`, `tests/`
- Expected impact: the project can now move from setup into stable domain-contract and greenhouse-blueprint work without redoing foundational repository decisions
- Follow-up needed: create the first stable domain contracts and the first greenhouse reference blueprint

**Project manager comment / voice note**
- We are starting the project now that the repository structure has been created.

