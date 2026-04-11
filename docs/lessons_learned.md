# Lessons Learned

## Purpose
This file stores reusable lessons, execution preferences, workflow corrections, and operating knowledge that should influence future interactions in this project.

It is not intended to duplicate the project log. It should capture lessons that are expected to remain useful over time and should be applied again later.

## Usage rules
- Add a new entry only when the project manager explicitly asks to preserve a lesson or when a lesson is clearly reusable and confirmed.
- Keep entries concise, operational, and reusable.
- When this file is updated, the lesson must also be reflected in `docs/handoff/current_handoff.md`.
- If a lesson changes the way the assistant should work, it should also be considered in future steps immediately.

## Entry template

### [LESSON-ID]
**Date:** YYYY-MM-DD  
**Category:** workflow | documentation | architecture | testing | communication | product  
**Title:** Short descriptive title

**Lesson**  
Describe the reusable lesson clearly.

**Implication for future work**
- Action 1
- Action 2

**Source**
- Brief note on how the lesson emerged.

---

## Lessons

### [LESSON-001]
**Date:** 2026-04-11  
**Category:** documentation  
**Title:** Deliver markdown files as attachments when practical

**Lesson**  
Long markdown content is easier for the project manager to handle when it is delivered as attached files instead of being pasted inline in the chat.

**Implication for future work**
- Prefer attached `.md` files for substantial markdown deliverables.
- Keep inline chat content focused on commands, expected outputs, and coordination.

**Source**
- Explicit instruction from the project manager during repository bootstrap.

### [LESSON-002]
**Date:** 2026-04-11  
**Category:** workflow  
**Title:** Preserve reusable knowledge in a dedicated lessons-learned file

**Lesson**  
Reusable project knowledge should not rely only on conversation memory or the project log. It must be preserved in a dedicated `docs/lessons_learned.md` file and propagated to the handoff document.

**Implication for future work**
- When the project manager flags a reusable lesson, record it in `docs/lessons_learned.md`.
- Reflect the lesson in `docs/handoff/current_handoff.md` so a future LLM inherits it immediately.

**Source**
- Explicit instruction from the project manager during repository bootstrap.

### [LESSON-003]
**Date:** 2026-04-11  
**Category:** documentation  
**Title:** Do not version auxiliary documentation bundles

**Lesson**  
Archive bundles created only to simplify chat delivery, such as temporary `.zip` documentation packs, should not be committed to the repository unless they are explicitly intended to be part of the product assets.

**Implication for future work**
- Keep temporary documentation bundles ignored in `.gitignore`.
- Prefer committing source documents rather than derived delivery bundles.

**Source**
- Correction applied before the first GitHub push.

### [LESSON-004]
**Date:** 2026-04-11  
**Category:** documentation  
**Title:** Treat chronological traceability as an explanatory narrative, not as a terse checklist

**Lesson**  
Project traceability must be preserved through an explicit chronological narrative that explains each major step in plain terms. The log must not merely state that a file or module was created. For every relevant milestone, the documentation should explain what was created, why it was necessary, why it was done at that exact point in the plan, how it fits in the architecture, and what it enables next. The goal is for even a poorly informed reader to understand the meaning of the work without reconstructing hidden context from the chat history.

**Implication for future work**
- Write project-log entries as explanatory milestone narratives, not as sparse technical notes.
- When documenting a new structural artifact such as a Python module, schema, blueprint, or test result, explicitly explain its role in the product architecture and in the project sequence.
- Synchronize the same narrative logic across `docs/project_log.md`, `README.md`, and `docs/handoff/current_handoff.md`, adapting the detail to the purpose of each document.
- Before updating the log for a major milestone, preserve any project-manager comment or voice-note transcript so the chronological record reflects both execution and managerial intent.
- Use the lessons-learned file to preserve durable documentation rules that future assistants must inherit from the start.

**Source**
- Explicit instruction from the project manager after the first domain and blueprint artifacts were created.
