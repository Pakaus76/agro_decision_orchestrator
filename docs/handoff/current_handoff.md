# Current Handoff — Agro Decision Orchestrator

## Core identity
Agro-DO is one real service-oriented product for greenhouse decision support.

Important:
- generative AI is mandatory in the target product architecture,
- deterministic orchestration exists only as fallback and resilience,
- do not reintroduce A/B/C/F-style framing.

## What has already been proven
- domain contracts validated
- blueprint validated
- decision cases validated
- bridge payload validated
- real local generative execution succeeded with OpenAI
- governed generative execution succeeded
- explicit high-risk backup-available policy escalation succeeded
- a second case confirmed that the service can differentiate between problem families
- a third case confirmed that the service behaves more cautiously under limited visibility and partially untrusted signals
- a fourth case confirmed that the service can stop automation and require physical verification when digital state may not match physical reality

Observed current validated patterns:
- pump degradation case → `high` + `switch_to_backup`
- high humidity disease-risk case → `high` + `adjust_operation`
- communication loss partial-blindness case → `high` + `escalate_to_human` + `medium` confidence
- manual override mismatch case → `high` + `stop_and_review` + `medium` confidence

All four required human review and remained operationally coherent.

## Main conclusions
1. The project has crossed from static modeling into real service behavior.
2. Generative AI is already functioning in practice.
3. The key challenge is no longer plumbing, but policy hardening.
4. Agro-DO now includes explicit product-policy escalation and differentiated behavior across multiple case families.
5. The service is already beginning to align recommendation style not only with severity, but also with the operational nature of the problem, fallback availability, the degree of uncertainty, and the trustworthiness of the digital control state.
6. The next work should keep broadening the case library and only then continue tightening policy where needed.

## Correct next objective
Add at least one more realistic case and continue policy hardening through broader scenario coverage.

More concretely:
- add another operationally meaningful case,
- validate it through the bridge and the governed generative path,
- inspect whether current policy remains coherent,
- refine `llm_orchestrator.py` only where case evidence justifies it.

## Anti-overwrite safeguard for cumulative memory files
`docs/project_log.md` and `docs/lessons_learned.md` must always be treated as cumulative memory files.

Required controls:
1. inspect the current file before updating it,
2. identify the last visible `LOG-*` and `LESSON-*` entries,
3. verify that prior entries remain present,
4. treat any drastically shorter replacement as likely wrong,
5. explicitly state whether a file instruction means:
   - replace the full file,
   - append to the current file,
   - or insert into a specific section.
