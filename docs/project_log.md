# Project Log

## Project
**Name:** Agro Decision Orchestrator  
**Short name:** Agro-DO  
**Working subtitle:** Advanced decision support for greenhouse irrigation, climate, and fertigation systems

## Purpose of this log
This file records major project milestones, key decisions, relevant test outcomes, and project-manager comments in chronological order.

It is not intended to capture every micro-step. It should be updated when:
- a meaningful objective is completed,
- a relevant architectural or product decision is made,
- a test produces a result worth preserving,
- the project manager adds a comment or voice note transcript that should remain traceable.

This log must explain not only **what** was done, but also **why** it was needed, **why it was done at that moment**, and **what it enables next**. The goal is to make the chronology understandable even to a reader with very limited technical background.

## Update policy
When a major update is needed, the update sequence must always be:
1. `docs/project_log.md`
2. `README.md`
3. `docs/lessons_learned.md` when applicable
4. `docs/handoff/current_handoff.md`
5. Git commit and GitHub push

## Entry template

### [ENTRY-ID]
**Date:** YYYY-MM-DD  
**Type:** milestone | decision | test-result | project-manager-note  
**Title:** Short descriptive title

**Summary**  
Short explanation of what happened and why it matters.

**Why this was needed**
Explain the problem or risk that made this step necessary.

**Why it was the right moment**
Explain why this step belonged to that specific point in the plan.

**What this enables next**
Explain what future work becomes possible because of this step.

**Files affected**
- File 1
- File 2

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

**Why this was needed**
The project required a stable working method before code creation began, including language discipline, documentation order, Git discipline, and role separation between assistant and project manager.

**Why it was the right moment**
These rules had to be fixed before the first real implementation steps, otherwise the repository would have grown without a consistent operating standard.

**What this enables next**
It establishes a controlled environment for all future technical work, documentation updates, and handoffs.

**Files affected**
- `README.md`
- `docs/project_log.md`
- `docs/handoff/current_handoff.md`

**Project manager comment / voice note**
- None recorded.

### [LOG-002]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** Local repository bootstrap started

**Summary**  
The project root folder was created and a local Git repository was initialized successfully.

**Why this was needed**
The project had to exist as a real codebase, not just as a concept discussed in chat.

**Why it was the right moment**
This was the unavoidable first execution step once the working rules were defined.

**What this enables next**
It opens the path for real file creation, version control, and progressive product construction.

**Files affected**
- repository root
- `.git/`

**Project manager comment / voice note**
- None recorded.

### [LOG-003]
**Date:** 2026-04-11  
**Type:** decision  
**Title:** Initial product scope fixed

**Summary**  
The project scope was fixed around a product-oriented agricultural decision-support system rather than a thesis-style benchmark artifact.

**Why this was needed**
Without an early scope decision, the project risked inheriting the wrong mindset from the previous repository and drifting into research-first behavior.

**Why it was the right moment**
This decision had to be made before architecture, contracts, and documentation started to harden.

**What this enables next**
It keeps architecture, documentation, and implementation choices aligned with a future product rather than with a paper-oriented artifact.

**Files affected**
- `README.md`
- `docs/handoff/current_handoff.md`

**Project manager comment / voice note**
- None recorded.

### [LOG-004]
**Date:** 2026-04-11  
**Type:** decision  
**Title:** Canonical reference environment selected

**Summary**  
The canonical starting environment was defined as a tomato greenhouse in substrate with three sectors, drip irrigation, fertigation, automatic ventilation, circulation fans, shading screen, and basic climate and irrigation sensing.

**Why this was needed**
The project needed a realistic but still manageable operational world. Modeling all agriculture too early would have made the MVP vague and unbuildable.

**Why it was the right moment**
This decision had to be taken before domain contracts and blueprints were created, because those files depend on a specific environment.

**What this enables next**
It provides a concrete target for the domain models, the first blueprint, the first decision cases, and the future UI.

**Files affected**
- `README.md`
- `docs/handoff/current_handoff.md`

**Project manager comment / voice note**
- None recorded.

### [LOG-005]
**Date:** 2026-04-11  
**Type:** decision  
**Title:** Markdown delivery and lessons learned registry adopted

**Summary**  
Markdown files should be delivered as separate attached files whenever practical, and a dedicated lessons-learned registry should be maintained for reusable project knowledge.

**Why this was needed**
Long markdown content is hard to copy and manage directly from the chat interface. At the same time, some instructions are too important to leave only in transient conversation memory.

**Why it was the right moment**
The documentation system was being created at that stage, so this was the right point to include a formal place for reusable operational knowledge.

**What this enables next**
It improves usability in the chat workflow and ensures that future assistants inherit stable working rules.

**Files affected**
- `docs/lessons_learned.md`
- `README.md`
- `docs/handoff/current_handoff.md`

**Project manager comment / voice note**
- None recorded.

### [LOG-006]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** Repository bootstrap completed and published to GitHub

**Summary**  
The repository structure, core documentation, `.gitignore`, `pyproject.toml`, package skeleton, and GitHub publication were completed successfully. The project now exists as a real, versioned, remotely published codebase.

**Why this was needed**
The project needed to move beyond planning and become a real repository with traceable history, shared structure, and remote backup.

**Why it was the right moment**
This was the natural closing point of the bootstrap phase, after the local structure and initial documentation had been prepared.

**What this enables next**
It unlocks real implementation work on domain models, blueprints, tests, and future product logic with proper version control and remote continuity.

**Files affected**
- `.gitignore`
- `pyproject.toml`
- `README.md`
- `docs/project_log.md`
- `docs/lessons_learned.md`
- `docs/handoff/current_handoff.md`

**Project manager comment / voice note**
- "We are starting the project now that the repository structure has been created."

### [LOG-007]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** Initial domain contracts created and validated

**Summary**  
The file `src/agro_do/domain/models.py` was created to define the first stable vocabulary of the product domain, and `src/agro_do/domain/__init__.py` was updated to export the new models cleanly. The imports were then validated successfully. This means the project now has a reusable and consistent language for the main entities it will manipulate.

**Why this was needed**
Before the project could create realistic scenarios, decision cases, bridge logic, or UI forms, it needed a stable definition of what a greenhouse, sector, asset, sensor, actuator, and crop profile actually are. Without these contracts, each future component could interpret the domain differently and create inconsistency across the product.

**Why it was the right moment**
This step belonged immediately after repository bootstrap because it creates the semantic foundation of the system. Building sample cases or orchestration logic before defining the domain would have meant constructing behavior on top of ambiguity.

**What this enables next**
It allows the project to build blueprints, loaders, decision-case schemas, and future recommendation logic on a shared and validated foundation.

**Files affected**
- `src/agro_do/domain/models.py`
- `src/agro_do/domain/__init__.py`

**Project manager comment / voice note**
- A first semantic base was established so future components would not invent their own interpretation of the greenhouse domain.

### [LOG-008]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** First reference greenhouse blueprint created and validated

**Summary**  
The file `inputs/greenhouse_blueprints/reference_tomato_greenhouse.json` was created as the first concrete operational environment of the product and then validated successfully as real JSON. The blueprint includes one greenhouse, three sectors, one crop profile, twenty assets, fourteen sensors, and eleven actuators.

**Why this was needed**
The domain models define the vocabulary of the system, but the product also needed a first concrete world built with that vocabulary. Without a blueprint, the project would still be talking about abstract entities rather than a real greenhouse that future logic can use.

**Why it was the right moment**
This step came immediately after the domain contracts because the blueprint depends on the entities already defined there. It would have been premature before the contracts existed and too late if the team had already started cases, rules, or UI without a concrete environment.

**What this enables next**
It enables the next layers of the product: decision-case design, blueprint loading and validation, deterministic decision logic, tests, and future user-facing scenario selection.

**Files affected**
- `inputs/greenhouse_blueprints/reference_tomato_greenhouse.json`

**Project manager comment / voice note**
- The project now had not only a vocabulary, but also a first operational world built with that vocabulary.

### [LOG-009]
**Date:** 2026-04-11  
**Type:** decision  
**Title:** Chronological traceability standard strengthened and formalized

**Summary**  
The documentation discipline was strengthened so that major log entries must explain not only what was created, but also why it matters, why it was created at that specific moment, and what it unlocks next. A new comprehensive lesson learned was also added to preserve this rule for future assistants.

**Why this was needed**
A purely technical or telegraphic log is not enough for long projects with multiple assistants, iterative decisions, and future handoffs. The project manager explicitly required a level of clarity that makes the chronological narrative understandable even to a non-expert reader.

**Why it was the right moment**
This correction was made immediately after the first real implementation artifacts were created, before the project accumulated more history under a weaker documentation standard.

**What this enables next**
It improves project continuity, auditability, onboarding for future assistants, and the usefulness of the log as a real project narrative rather than as a sparse technical checklist.

**Files affected**
- `docs/project_log.md`
- `docs/lessons_learned.md`
- `README.md`
- `docs/handoff/current_handoff.md`

**Project manager comment / voice note**
- None recorded.

### [LOG-010]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** Decision-case contract and first sample case created

**Summary**  
The file `src/agro_do/domain/decision_case.py` was created to define how the product represents a concrete situation that requires a decision. After that, the first sample case, `inputs/sample_cases/case_main_pump_degradation.json`, was created and validated. At this point, the project can describe not only what exists in the greenhouse, but also what is happening when something may require action.

**Why this was needed**
The project already knew how to describe the greenhouse environment, but it still had no standard way to describe a decision situation. Without this contract, future rules, bridge logic, and UI execution paths would have no stable input format for operational cases.

**Why it was the right moment**
This step belonged immediately after the blueprint milestone because the project needed a real case format before it could start connecting environment data to future decision logic.

**What this enables next**
It enables loader development, cross-validation between case and environment, deterministic recommendation logic, and future UI execution flows based on real decision situations instead of abstract placeholders.

**Files affected**
- `src/agro_do/domain/decision_case.py`
- `src/agro_do/domain/__init__.py`
- `inputs/sample_cases/case_main_pump_degradation.json`

**Project manager comment / voice note**
- Since the previous milestone, the repository moved from describing the greenhouse world to describing a real problem inside that world. The project now has a standard way to express an operational situation, plus a first realistic case based on main pump degradation.

### [LOG-011]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** First bridge-side loading path created and validated

**Summary**  
The file `src/agro_do/bridge/loader.py` was created to load the greenhouse blueprint and the decision case, validate both, check that their references are consistent, and build a first `MinimalExecutionPayload`. The loader was executed successfully against the reference blueprint and the main-pump sample case.

**Why this was needed**
Until this point, the project had the right pieces but they were still separate: the environment, the case schema, and the sample case. The product needed an explicit path that could connect those pieces and prove that they work together as one coherent system.

**Why it was the right moment**
This step came immediately after the first sample case because the next architectural question was no longer what the pieces look like, but whether they can already interact in a controlled way.

**What this enables next**
It enables deterministic orchestration logic, richer validation tests, execution scripts, and later UI-triggered runs that operate on a validated payload instead of on loosely connected JSON files.

**Files affected**
- `src/agro_do/bridge/loader.py`

**Project manager comment / voice note**
- Since the previous milestone, the project has moved from having separate data structures to having its first working execution path. First, we created the decision-case contract so the product could describe not only what exists in the greenhouse but also what is happening when a decision is needed. Then we created a realistic main irrigation pump degradation case to test whether that schema was useful in practice. Finally, we built the first minimal loader in the bridge layer. This loader reads the greenhouse blueprint, reads the decision case, validates both, verifies that their references match, and produces a minimal execution payload. What has been demonstrated is that the project no longer contains only static definitions or isolated example files. It already has a first functional path in which the environment description, the case description, and the bridge logic work together in a basic but real way.
