# Project Log

## Project
**Name:** Agro Decision Orchestrator  
**Short name:** Agro-DO  
**Working subtitle:** Advanced decision support for greenhouse irrigation, climate, and fertigation systems

## Update policy
1. `docs/project_log.md`
2. `README.md`
3. `docs/lessons_learned.md` when applicable
4. `docs/handoff/current_handoff.md`
5. Git commit and GitHub push

## Chronological entries

### [LOG-017]
**Date:** 2026-04-11  
**Type:** milestone  
**Title:** High-risk backup-available policy escalation implemented and validated

**What happened**  
The governed generative orchestrator was updated with a stronger service-policy rule for high-risk cases where a backup path is explicitly available. In those situations, the system is no longer allowed to remain in soft-response modes such as `inspect`, `continue_with_monitoring`, or `no_action`. The policy now escalates the recommendation to `switch_to_backup` and keeps human review mandatory.

**Why this was needed**  
The previous governed validation proved that structural guardrails alone were not enough. The system could still produce a recommendation that was technically valid but too passive for a high-severity operational scenario. The product therefore needed a stricter business-policy layer, not just output-shape validation.

**Why it happened at this moment**  
This was the right next step because the architecture had already proven that the generative path worked and that basic governance worked. Once that foundation was validated, the next highest-value improvement was to shape product behavior under operationally sensitive conditions.

**What this enables next**  
This moves Agro-DO from structural governance into explicit service-policy governance. It also creates a pattern for expanding policy hardening to additional realistic cases instead of allowing product strictness to depend on only one scenario.

**Files affected**
- `src/agro_do/decision_orchestrator/llm_orchestrator.py`

**Project manager comment / voice note**
- Since the previous major milestone, the project has moved from having a governed generative recommendation path to having a more explicit and operationally stricter recommendation policy. The first important development in this phase was the recognition that structural guardrails alone were not enough. Even though the generative orchestrator was already functioning and governed, the previous validation showed that in a high-severity case with an available backup path, the model could still return a relatively soft recommendation such as inspect. This was not treated as a technical failure, but as a product-policy issue that needed to be resolved explicitly.

### [LOG-018]
**Date:** 2026-04-11  
**Type:** test-result  
**Title:** Policy-hardened generative recommendation validated successfully

**What happened**  
The updated policy was validated successfully using the same main irrigation pump degradation case. The resulting recommendation remained high priority, required human review, kept high confidence, and now returned `switch_to_backup` instead of the previous softer `inspect` outcome.

**Why this was needed**  
It was not enough to encode the new rule in code. The project needed evidence that the rule actually changes the outcome of the governed generative path in practice.

**Why it happened at this moment**  
This validation was the immediate follow-up to the policy hardening implementation and was necessary before documenting the rule as part of the product behavior.

**What this enables next**  
It confirms that Agro-DO now contains a real product-policy escalation rule and makes it sensible to extend similar logic to additional realistic scenarios.

**Files affected**
- runtime validation only

**Project manager comment / voice note**
- The updated behavior was then validated again using the same main pump degradation case. This validation was successful and showed a clear policy shift in the output. The resulting recommendation remained high priority, still required human review, and kept high confidence, but the action type changed from inspect to switch_to_backup. The action summary was also aligned with the stronger operational response. This demonstrates that the new policy guardrail is not only present in the code, but actually changes the recommendation outcome in practice.
