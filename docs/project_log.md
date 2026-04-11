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
The operating rules for the project were explicitly defined before implementation work started. This created a common way of working for repository discipline, documentation order, language conventions, and LLM handoff continuity.

**Why this was needed**
Without clear rules from the beginning, the project could quickly become inconsistent, difficult to follow, and hard to transfer to another assistant later.

**Why it was the right moment**
This had to be done before coding in order to prevent structural disorder from appearing in the first place.

**What this enables next**
It makes it possible to bootstrap the repository in a controlled way and to maintain consistent documentation from the first commit.

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
The project root folder was created and a local Git repository was initialized successfully. This marked the transition from planning to actual implementation.

**Why this was needed**
A product cannot be developed seriously without a controlled repository, versioning, and a stable local workspace.

**Why it was the right moment**
The operating rules were already defined, so the next sensible move was to create the technical environment where the project would live.

**What this enables next**
It allows the project structure, documentation, and source code to evolve under version control from the start.

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
The project scope was fixed around a product-oriented agricultural decision-support system rather than a thesis-style benchmark artifact. This protected the implementation from drifting toward a research-first mindset.

**Why this was needed**
The previous industrial repository had a research orientation, so the new project needed an explicit reset to keep the focus on operator value, workflows, configuration, and explainability.

**Why it was the right moment**
The scope had to be fixed before the first structural files and domain models were created. Otherwise, the repository could have been shaped around the wrong purpose.

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
The project needed a realistic but still manageable operational world. Modeling “all agriculture” too early would have made the MVP vague and unbuildable.

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
Markdown files should be delivered as attached files whenever practical, and a dedicated lessons-learned registry should be maintained for reusable project knowledge.

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
- "Since the previous documented milestone, we moved from repository setup into the first real product foundation. We defined the initial domain contracts in Python so that the project now has a stable vocabulary for the main entities of the system, such as greenhouses, sectors, assets, sensors, actuators, and crop profiles. This was important because the product could not evolve consistently if each future component used its own interpretation of the domain. After that, we exposed these models through the domain package and verified that they could be imported correctly. This confirmed that the project structure and package organization were working as intended before adding more complexity."

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
- "Since the previous documented milestone, we moved from repository setup into the first real product foundation. We defined the initial domain contracts in Python so that the project now has a stable vocabulary for the main entities of the system, such as greenhouses, sectors, assets, sensors, actuators, and crop profiles. This was important because the product could not evolve consistently if each future component used its own interpretation of the domain. After that, we exposed these models through the domain package and verified that they could be imported correctly. This confirmed that the project structure and package organization were working as intended before adding more complexity. We then created the first reference greenhouse blueprint as a concrete JSON representation of the MVP environment: a tomato greenhouse in substrate with three sectors, irrigation, fertigation, climate assets, sensors, and actuators. This was a key step because the project now has not only abstract models, but also a first operational environment that can later support decision cases, orchestration logic, testing, and user-facing views. Finally, we validated that the blueprint loads correctly as JSON and that its main sections are present and consistent. At this point, the project has moved beyond repository bootstrap and already contains the first meaningful domain foundation for the product."

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
