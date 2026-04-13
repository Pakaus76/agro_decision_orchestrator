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

### [LESSON-005]
**Date:** 2026-04-11  
**Category:** workflow  
**Title:** Do not generate auxiliary ZIP packages for this project

**Lesson**  
Auxiliary ZIP packages used only for convenience in chat delivery are not useful in this project and should not be generated anymore.

**Implication for future work**
- Deliver only the necessary files separately.
- Avoid creating ZIP bundles unless the project manager explicitly asks for one.

**Source**
- Explicit correction from the project manager after repeated ZIP delivery.

### [LESSON-006]
**Date:** 2026-04-11  
**Category:** communication  
**Title:** Make manager summaries cumulative without repeating the same wording

**Lesson**  
Project-manager summaries must reflect what genuinely changed since the previous milestone and should also connect that change with the accumulated state of the project. They should not recycle the same introductory formula every time. The goal is to help a reader understand both the local step and the broader progression without feeling that the summary is mechanically repeated.

**Implication for future work**
- When writing a new manager summary, mention the new outcome first and then relate it to the already completed foundations.
- Avoid repeating the same opening structure across consecutive milestones.
- Use summaries to show progression, not only isolated activity.

**Source**
- Explicit correction from the project manager after repeated milestone summaries.

### [LESSON-007]
**Title:** Cumulative memory files must never be replaced by shortened summaries

`docs/project_log.md` and `docs/lessons_learned.md` are cumulative memory files, not rolling summaries. If they are replaced by shorter versions, the project loses historical continuity and handoff value.

**Operational consequence**
- Treat both files as append-only historical records unless the project manager explicitly requests restructuring.
- Before updating either file, verify that older entries are still present.
- If a proposed update is dramatically shorter than the current file, assume it is wrong until proven otherwise.

### [LESSON-008]
**Title:** Every file-edit instruction must specify replace vs append

Ambiguity about whether content should replace a file or be appended can create avoidable mistakes during step-by-step repository work.

**Operational consequence**
- Every time text is provided for a file, the instruction must explicitly say one of these:
  - replace the full file content,
  - append this content to the current file,
  - insert this block in a specific section.

### [LESSON-009]
**Title:** Cumulative project-memory files require anti-overwrite controls before every documentation update

A critical documentation failure occurred when `docs/project_log.md` and `docs/lessons_learned.md` were unintentionally replaced with shortened versions that no longer preserved the full accumulated history of the project. Although Git allowed recovery from the last complete version, the incident showed that these files cannot be handled like ordinary summary documents.

These files are not convenience summaries. They are cumulative memory artifacts and must preserve the full historical continuity of the project. If they are overwritten by shorter generated versions, the project loses traceability, decision continuity, and handoff reliability.

**Operational consequence**
Before any future update of the four core markdown files, the following control must be applied:

1. Treat `docs/project_log.md` and `docs/lessons_learned.md` as cumulative files by default.
   - They must be appended to or edited locally in a targeted way.
   - They must never be regenerated as short replacement summaries unless the project manager explicitly requests a full restructuring.

2. Verify the current file state before proposing any new content.
   - Identify the last visible `LOG-*` entry in `docs/project_log.md`.
   - Identify the last visible `LESSON-*` entry in `docs/lessons_learned.md`.
   - Confirm that older entries are still present.

3. Apply an anti-truncation sanity check before replacing or saving content.
   - If a proposed new version of `docs/project_log.md` or `docs/lessons_learned.md` is significantly shorter than the current file, assume it is wrong until proven otherwise.
   - If numbering continuity breaks, stop and correct it before proceeding.

4. Always state the edit mode explicitly when giving file instructions.
   - Replace the full file content, or
   - Append this block to the end of the current file, or
   - Insert this block in a specific section.
   Ambiguity is not acceptable.

5. Do not close a documentation milestone until the memory files are checked.
   - Confirm `LOG-*` continuity.
   - Confirm `LESSON-*` continuity.
   - Confirm that no prior historical entries were removed unintentionally.

This safeguard is mandatory for all future assistants and must also be reflected in the handoff so that no later LLM repeats the same mistake.

### [LESSON-010]
**Title:** Policy hardening must be tested against more than one case family

A policy rule that looks correct on one severe case can still be overfitted if it is not validated against a second case with a different operational pattern.

**Operational consequence**
- After hardening a policy rule on one case, validate it against at least one additional realistic case from a different problem family.
- Do not assume that a stricter rule is good just because it improved one scenario.
- Prefer expanding the case library before tightening policy further.

### [LESSON-011]
**Title:** Cumulative memory files require explicit anti-overwrite checks

`docs/project_log.md` and `docs/lessons_learned.md` are not rolling summaries. They are cumulative memory artifacts and must preserve historical continuity.

**Operational consequence**
- Before updating either file, verify the last visible entry and numbering continuity.
- If a proposed new version is much shorter than the current one, assume it is wrong until proven otherwise.
- Never replace these files with shortened generated summaries unless the project manager explicitly requests a full restructuring.

