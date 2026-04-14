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

### [LESSON-012]
**Title:** Degraded-visibility scenarios are essential for testing recommendation prudence

A decision-support service can appear strong when it only handles physical-failure or climate-correction cases. Real reliability also depends on how it behaves when the main issue is uncertainty, incomplete visibility, or partially untrusted signals.

**Operational consequence**
- Include degraded-visibility cases in the case library early.
- Treat confidence behavior and escalation behavior as first-class policy concerns.
- Do not assume that policy hardening is complete until the service has been tested under uncertainty, not only under clearly observable failures.

### [LESSON-013]
**Title:** State-mismatch cases are essential for testing whether the service knows when to stop automation

A decision-support service can look reliable while it only recommends escalation or adjustment. A stronger maturity signal appears when it can also recognize that the safest action is to stop and verify because the digital state may no longer reflect physical reality.

**Operational consequence**
- Include state-mismatch cases in the case library, not only failure and visibility cases.
- Treat `stop_and_review` behavior as a first-class policy outcome, not only as an exception.
- Use these cases to test whether the service can distrust the control layer without assuming a full communication outage.

### [LESSON-014]
**Title:** Sensor-trust scenarios are essential for testing whether the service knows when data quality becomes the main risk

A decision-support service can appear mature while it still assumes that most available signals are basically trustworthy. A stronger maturity signal appears when it can recognize that the main danger is acting on misleading data rather than on a confirmed physical failure.

**Operational consequence**
- Include sensor-drift and flatline cases in the case library, not only actuator and communication cases.
- Treat data-trust behavior as a first-class policy concern.
- Use these cases to test whether the service can reduce confidence and escalate prudently even when the wider control infrastructure still appears available.

### [LESSON-015]
**Title:** Resource-continuity cases are useful for finding when the service becomes too abrupt instead of merely prudent

A decision-support service can recognize a serious risk correctly and still respond with an action that is stronger than ideal for the exact operational pattern. Resource-shortage scenarios are especially good at revealing whether the service knows the difference between “unsafe to continue” and “serious but still manageable through controlled mitigation.”

**Operational consequence**
- Include reserve-depletion and continuity-risk cases in the case library, not only failure and visibility cases.
- Treat continuity-management behavior as a distinct policy concern.
- Use these cases to refine whether the service should stop immediately, adjust operation, or escalate with continuity planning when resources are running low but service has not fully failed yet.


### [LESSON-016]
**Title:** Scarcity scenarios must distinguish between stop conditions and controlled mitigation conditions

A decision-support service becomes more credible when it can separate two situations that are both serious but not operationally identical: one in which continuity risk justifies a stop-oriented response, and another in which continuity can still be preserved through controlled mitigation such as rationing, prioritization, or temporary operational adjustment.

**Operational consequence**
- Do not treat all low-resource scenarios as equivalent to immediate interruption.
- Build paired cases inside the same risk family so that the service is tested on whether it can distinguish between abrupt-stop logic and graduated continuity-management logic.
- When flow and pressure remain stable, test whether scarcity can be managed through `adjust_operation` or escalation with continuity planning before assuming `stop_and_review` is the best response.

### [LESSON-017]
**Title:** Controlled scarcity mitigation is only credible while execution stability still exists

A decision-support service should not evaluate scarcity only by reserve level. It must also consider whether the delivery system remains stable enough for the proposed mitigation to be executed reliably. Low reserves with stable hydraulic behavior can justify controlled mitigation, but low reserves combined with unstable flow or deteriorating pressure can legitimately shift the response back toward interruption-oriented logic.

**Operational consequence**
- Do not model scarcity policy only around reserve percentage.
- Pair resource-continuity cases with execution-feasibility signals such as flow stability and pressure behavior.
- Treat hydraulic deterioration as a first-class reason to move from `adjust_operation` back toward `stop_and_review`.

### [LESSON-018]
**Title:** The current scarcity policy boundary appears earlier and more conservative than expected

A decision-support service may appear to have a rich internal policy boundary, but paired transition cases can show that the effective threshold is actually simpler and more conservative. In Agro-DO, once hydraulic behavior stops being clearly stable, the system already tends to move to `stop_and_review`, even before degradation becomes fully severe.

**Operational consequence**
- Do not assume that a conceptual middle zone exists just because it was designed into the case family.
- Test the boundary with multiple gradual transition cases before concluding that the system differentiates finely.
- Treat the current threshold as conservative: stable execution supports `adjust_operation`, while even mild hydraulic degradation may already be enough to trigger `stop_and_review`.

### [LESSON-019]
**Title:** Very mild hydraulic degradation can still remain inside the controlled-mitigation zone

A decision-support service may appear overly conservative after a borderline transition case, but a softer early-warning case can reveal that a narrow permissive band still exists. In Agro-DO, low-water continuity pressure combined with very mild hydraulic softening can still justify `adjust_operation` when flow and pressure remain largely functional and degradation does not yet imply meaningful instability.

**Operational consequence**
- Do not conclude too early that any visible degradation automatically triggers interruption-oriented logic.
- Separate borderline degradation from genuinely mild early-warning softening when designing scarcity cases.
- Use additional threshold-probing cases to locate the exact switching point between `adjust_operation` and `stop_and_review`.

### [LESSON-020]
**Title:** The scarcity-family switching threshold is narrow and flips quickly after the early-warning pattern

A decision-support service can have a real permissive band without that band being broad. In Agro-DO, once hydraulic degradation becomes slightly stronger than the very mild early-warning condition, the policy already flips to `stop_and_review`. This means the threshold exists, but it lies very close to the soft edge of degradation.

**Operational consequence**
- Do not describe the scarcity policy as broadly tolerant just because Case 10 remained in `adjust_operation`.
- Treat the current mitigation band as narrow and close to the stable/softening edge.
- Use one final confirmatory threshold case before declaring the boundary fully characterized.

### [LESSON-021]
**Title:** A policy threshold can be considered sufficiently characterized once a confirmatory near-threshold case reproduces the same side of the flip

A decision-support service does not need endless micro-variations once a threshold has been probed from both sides and then confirmed by an intermediate or near-threshold case. In Agro-DO, Case 10, Case 11, and Case 12 together show that the scarcity-family switching point is narrow and stable enough for the current stage of development.

**Operational consequence**
- Stop iterating a micro-family once the threshold has been probed from both sides and confirmed.
- Treat the current scarcity-plus-hydraulics threshold as sufficiently characterized for now.
- Move effort to a new policy family where the service can demonstrate broader decision value instead of diminishing returns from further threshold sampling.

### [LESSON-022]
**Title:** The README must preserve its full structural role, including the project tree

`README.md` is not only a presentation file. In this project it acts as a live operational entry point and must preserve the structural sections that make the repository understandable at a glance. This includes keeping the current README structure and explicitly maintaining the project tree section whenever the repository structure changes.

**Operational consequence**
- Do not simplify or overwrite `README.md` with shorter summary versions that remove structural sections.
- Preserve the current README structure unless the project manager explicitly requests a redesign.
- Always keep the project tree section present and updated when folders or major structural elements change.
- Treat removal of the tree or loss of README structure as a documentation regression, not as a harmless edit.

### [LESSON-023]
**Title:** Constrained continuity should be tested as an allocation problem, not only as a stop-versus-continue problem

A decision-support service shows broader operational value when it can reason about how to preserve partial continuity under constrained resources instead of collapsing immediately into global interruption logic. In Agro-DO, sector prioritization under water constraint revealed that selective continuity can be both operationally and economically preferable when hydraulic execution remains viable.

**Operational consequence**
- Add case families where not all sectors have equal priority or equal tolerance to restriction.
- Test whether the service can recommend differentiated allocation under constraint instead of defaulting too quickly to global stop logic.
- Treat prioritization-oriented `adjust_operation` outcomes as a key maturity signal for the product.

### [LESSON-024]
**Title:** Never degrade a previously validated deliverable when preparing an update

When a file already contains a stronger, richer, or more useful version of a section, any later update must start from that validated baseline and preserve or improve it. It is not acceptable to replace a richer result with a reduced shortcut version just because it is faster to generate.

**Operational consequence**
- Always compare the new proposed output with the strongest prior validated version of the same deliverable.
- Never replace a richer section, structure, tree, summary, or specification with a poorer version.
- Updates must preserve quality floor and preferably improve it; they must not degrade it.
- If a full-file replacement is requested, the replacement must carry forward everything that remains valuable from the previous version unless the project manager explicitly requests removal.

### [LESSON-025]
**Title:** Prioritization can remain viable even when continuity collapses for medium-priority sectors

A decision-support service can show strong operational maturity when it does not jump too quickly from broad selective continuity to global stop logic. In Agro-DO, tighter water constraints still allowed a prioritization-oriented response, but only by protecting the highest-priority sector and fully sacrificing lower-priority continuity.

**Operational consequence**
- Test prioritization families beyond the first selective-allocation success case.
- Distinguish between “broad prioritization still viable” and “only top-priority continuity remains viable.”
- Treat one-sector protection under severe constraint as a distinct policy mode, not merely as a weaker version of the earlier allocation case.

### [LESSON-026]
**Title:** A prioritization family is sufficiently characterized once it covers broad allocation, top-priority-only allocation, and full collapse

A decision-support service does not need endless variations once a constrained-allocation family has been mapped across its main policy modes. In Agro-DO, the prioritization family now covers:
- broader selective continuity,
- top-priority-sector-only continuity,
- and full interruption when even that last continuity option becomes too fragile.

**Operational consequence**
- Treat the current prioritization family as sufficiently characterized for the current stage.
- Stop sampling more micro-variations inside the same allocation pattern once the collapse boundary has been observed.
- Move to a new family where Agro-DO must reason about recovery alternatives, backup paths, or post-collapse continuity options.

### [LESSON-027]
**Title:** External recovery paths should be treated as a distinct decision family, not as a minor variant of internal collapse

A decision-support service shows broader operational intelligence when it can distinguish between internal collapse with no way out and internal collapse with a credible backup or recovery path. In Agro-DO, confirmed emergency external water supply changed the recommendation from interruption-oriented logic to backup-oriented recovery logic.

**Operational consequence**
- Add recovery-oriented case families after internal collapse families are mapped.
- Do not treat confirmed backup supply as a small detail inside a collapse case; it can change the policy mode entirely.
- Treat `switch_to_backup` outcomes as a first-class maturity signal when recovery depends on credible external support.

### [LESSON-028]
**Title:** Temporary result files must never be left in the repository root after documentation is complete

Intermediate JSON outputs, validation dumps, and execution result files are useful only while they add immediate traceability during active work. Once the relevant outcome has already been captured in the permanent project documents and the corresponding commit has been completed, those temporary files stop adding value and become repository noise.

**Operational consequence**
- Do not save temporary JSON result files in the repository root.
- Only keep intermediate result files when they provide real ongoing value.
- When temporary results must be preserved, store them in a coherent location under `outputs/reports/`, not in the repository root.
- After the result has been documented in `README.md`, `docs/project_log.md`, `docs/lessons_learned.md`, or `docs/handoff/current_handoff.md`, delete the temporary file unless the project manager explicitly requests that it be retained.
- Do not invent a new storage location from one case to the next; keep the same repository rule consistently.

