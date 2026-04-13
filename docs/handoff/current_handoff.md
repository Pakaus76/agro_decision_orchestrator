# Current Handoff — Agro Decision Orchestrator

## Core identity
Agro-DO is one real service-oriented product for greenhouse decision support.

Important:
- generative AI is mandatory in the target product architecture,
- deterministic orchestration exists only as fallback and resilience,
- do not reintroduce A/B/C/F-style framing.

## Current implemented architecture
- `src/agro_do/domain/models.py`
- `src/agro_do/domain/decision_case.py`
- `src/agro_do/domain/recommendation.py`
- `inputs/greenhouse_blueprints/reference_tomato_greenhouse.json`
- `inputs/sample_cases/case_main_pump_degradation.json`
- `src/agro_do/bridge/loader.py`
- `src/agro_do/decision_orchestrator/orchestrator.py`
- `src/agro_do/decision_orchestrator/llm_orchestrator.py`
- `src/agro_do/integrations/openai_client.py`
- `.env.example`
- `pyproject.toml`

## What has already been proven
- domain contracts validated
- blueprint validated
- decision case validated
- bridge payload validated
- real local generative execution succeeded with OpenAI
- governed generative execution also succeeded
- explicit high-risk backup-available policy escalation also succeeded

Observed latest policy-hardened output on the pump case:
- priority: `high`
- action type: `switch_to_backup`
- human review required: `True`
- confidence: `high`
- next checks: `6`
- decision trace: `8`
- action summary: "Switch irrigation to backup pump to restore stable flow and pressure."

## Main conclusions
1. The project has crossed from static modeling into real service behavior.
2. Generative AI is already functioning in practice.
3. The key challenge is no longer plumbing, but policy hardening.
4. Agro-DO now includes at least one explicit product-policy escalation rule that changes recommendation behavior in practice.
5. The next work should broaden policy hardening with more realistic cases rather than return to foundational redesign.

## Correct next objective
Add at least one additional realistic case and use it to continue policy hardening.

More concretely:
- create a second operationally meaningful sample case,
- validate it through the same bridge and generative path,
- identify whether current policy is sufficient,
- then refine `llm_orchestrator.py` further if needed.

## Important process rule
Whenever text is given for a file, instructions must explicitly state whether the user should replace the whole file or append to the current content.

### Anti-overwrite safeguard for cumulative memory files

A previous documentation incident proved that `docs/project_log.md` and `docs/lessons_learned.md` must never be treated as disposable summary files. They are cumulative project-memory artifacts and must preserve the full historical continuity of the repository.

Therefore, every future assistant must apply these controls before updating the four core markdown files:

1. `docs/project_log.md` and `docs/lessons_learned.md` are cumulative by default.
   - Append or edit locally in a targeted way.
   - Do not regenerate them as shortened replacements unless the project manager explicitly orders a full restructuring.

2. Inspect the current file before updating it.
   - Identify the last visible `LOG-*` entry.
   - Identify the last visible `LESSON-*` entry.
   - Verify that earlier entries are still present.

3. Apply an anti-truncation check.
   - If the proposed new file is much shorter than the current one, treat that as a likely error.
   - If numbering continuity is broken, correct it before any commit.

4. Every file-edit instruction must explicitly state one of these modes:
   - replace the full file content,
   - append this block to the current file,
   - insert this block in a specific section.

5. No documentation milestone may be committed until cumulative memory integrity has been checked.

This safeguard is mandatory because the loss of accumulated documentation would seriously damage traceability, continuity, and handoff quality.

