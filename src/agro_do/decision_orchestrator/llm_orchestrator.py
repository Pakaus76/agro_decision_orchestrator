"""Generative orchestration layer for the Agro Decision Orchestrator."""

from __future__ import annotations

import json
from typing import Any

from agro_do.bridge.loader import MinimalExecutionPayload
from agro_do.decision_orchestrator.orchestrator import generate_recommendation
from agro_do.domain import (
    ConfidenceLevel,
    RecommendedActionType,
    Recommendation,
    RecommendationPriority,
)
from agro_do.integrations.openai_client import (
    OpenAIConfigurationError,
    request_json_response,
)

_PRIORITY_ORDER = {
    RecommendationPriority.LOW: 1,
    RecommendationPriority.MEDIUM: 2,
    RecommendationPriority.HIGH: 3,
    RecommendationPriority.CRITICAL: 4,
}

_RISKY_ACTION_TYPES = {
    RecommendedActionType.SWITCH_TO_BACKUP,
    RecommendedActionType.ESCALATE_TO_HUMAN,
    RecommendedActionType.STOP_AND_REVIEW,
}


def _build_system_prompt() -> str:
    """Build the system prompt for the generative orchestrator."""

    return (
        "You are the generative reasoning layer of Agro Decision Orchestrator, a "
        "decision-support service for greenhouse operations. "
        "Your task is to analyze a validated agricultural decision payload and return "
        "one JSON object only. "
        "The response must be operational, concise, and grounded in the provided case. "
        "Do not invent assets, sensors, or context that are not present in the payload. "
        "You must choose one priority from: low, medium, high, critical. "
        "You must choose one action_type from: inspect, switch_to_backup, "
        "continue_with_monitoring, adjust_operation, escalate_to_human, "
        "stop_and_review, no_action. "
        "You must choose one confidence from: low, medium, high. "
        "If the action has meaningful operational risk, human_review_required must be true. "
        "Do not return fewer than 2 next_checks or more than 6. "
        "Do not return fewer than 3 decision_trace items or more than 8. "
        "Do not return a lower recommendation priority than the severity implied by the case. "
        "If the case is high or critical and an available backup path exists, do not keep the "
        "recommendation in a soft state such as inspect, continue_with_monitoring, or no_action. "
        "Return JSON with exactly these keys: "
        "priority, action_type, action_summary, rationale, confidence, "
        "human_review_required, next_checks, decision_trace."
    )


def _serialize_payload(payload: MinimalExecutionPayload) -> dict[str, Any]:
    """Convert the validated payload into a prompt-friendly serializable dictionary."""

    return {
        "greenhouse": payload.greenhouse.model_dump(mode="json"),
        "sectors": [sector.model_dump(mode="json") for sector in payload.sectors],
        "crop_profile": payload.crop_profile.model_dump(mode="json"),
        "decision_case": payload.decision_case.model_dump(mode="json"),
    }


def _build_user_prompt(payload: MinimalExecutionPayload) -> str:
    """Build the user prompt containing the normalized payload."""

    serialized_payload = json.dumps(
        _serialize_payload(payload),
        indent=2,
        ensure_ascii=False,
    )

    return (
        "Analyze the following validated greenhouse decision payload and generate "
        "the best operational recommendation.\n\n"
        "Important constraints:\n"
        "- Keep the recommendation grounded in the provided data.\n"
        "- Prefer safe operational behavior under uncertainty.\n"
        "- Require human review when the action has meaningful operational risk.\n"
        "- Keep action_summary and rationale short but clear.\n"
        "- next_checks must be a list of short actionable items.\n"
        "- decision_trace must be a list of short reasoning steps.\n"
        "- Never lower recommendation priority below what the case severity justifies.\n"
        "- If severity is high or critical and backup is available, do not stay in inspect-only mode.\n\n"
        f"Payload:\n{serialized_payload}"
    )


def _normalize_text_list(
    raw_value: Any,
    *,
    field_name: str,
    min_items: int,
    max_items: int,
) -> list[str]:
    """Normalize and validate a text list returned by the LLM."""

    if not isinstance(raw_value, list):
        raise ValueError(f"{field_name} must be a list.")

    normalized_items = [str(item).strip() for item in raw_value if str(item).strip()]

    if len(normalized_items) < min_items:
        raise ValueError(
            f"{field_name} must contain at least {min_items} non-empty item(s)."
        )

    return normalized_items[:max_items]


def _minimum_allowed_priority(
    payload: MinimalExecutionPayload,
) -> RecommendationPriority:
    """Return the minimum allowed priority based on the incoming decision case."""

    severity_value = payload.decision_case.severity_hint.value
    return RecommendationPriority(severity_value)


def _is_priority_lower_than_case(
    candidate: RecommendationPriority,
    minimum_allowed: RecommendationPriority,
) -> bool:
    """Return whether a recommendation priority is lower than the minimum allowed level."""

    return _PRIORITY_ORDER[candidate] < _PRIORITY_ORDER[minimum_allowed]


def _detect_backup_option(payload: MinimalExecutionPayload) -> bool:
    """Detect whether the operational context explicitly mentions an available backup."""

    for context_note in payload.decision_case.operational_context:
        combined_text = f"{context_note.note} {context_note.impact or ''}".lower()
        if "backup" in combined_text and "available" in combined_text:
            return True
    return False


def _enforce_high_severity_backup_policy(
    recommendation: Recommendation,
    payload: MinimalExecutionPayload,
) -> tuple[Recommendation, list[str]]:
    """Enforce stricter policy for high-risk cases with an available backup path."""

    guardrail_notes: list[str] = []
    has_backup_option = _detect_backup_option(payload)

    if not has_backup_option:
        return recommendation, guardrail_notes

    if recommendation.priority not in {
        RecommendationPriority.HIGH,
        RecommendationPriority.CRITICAL,
    }:
        return recommendation, guardrail_notes

    if recommendation.action_type in {
        RecommendedActionType.INSPECT,
        RecommendedActionType.CONTINUE_WITH_MONITORING,
        RecommendedActionType.NO_ACTION,
    }:
        updated_next_checks = list(recommendation.next_checks)

        enforced_check = (
            "Prepare and execute a controlled switch to the backup pump if operating conditions allow."
        )

        if enforced_check not in updated_next_checks:
            updated_next_checks.insert(0, enforced_check)

        updated_trace = list(recommendation.decision_trace)
        updated_trace.append(
            "Policy escalation applied: high-severity case with available backup cannot remain in a soft-response mode."
        )

        updated_rationale = (
            f"{recommendation.rationale} Policy escalation was applied because the case is "
            "high-severity and an available backup path exists."
        )

        recommendation = recommendation.model_copy(
            update={
                "action_type": RecommendedActionType.SWITCH_TO_BACKUP,
                "action_summary": (
                    "Initiate a controlled switch to the backup pump and inspect the primary irrigation path."
                ),
                "human_review_required": True,
                "next_checks": updated_next_checks[:6],
                "decision_trace": updated_trace[:8],
                "rationale": updated_rationale[:600],
            }
        )

        guardrail_notes.append(
            "Action was escalated to switch_to_backup due to high-severity risk with backup availability."
        )

    return recommendation, guardrail_notes


def _apply_guardrails(
    recommendation: Recommendation,
    payload: MinimalExecutionPayload,
) -> Recommendation:
    """Apply deterministic guardrails to the LLM recommendation."""

    updates: dict[str, Any] = {}
    guardrail_notes: list[str] = []

    minimum_allowed_priority = _minimum_allowed_priority(payload)
    final_priority = recommendation.priority

    if _is_priority_lower_than_case(final_priority, minimum_allowed_priority):
        raise ValueError(
            "LLM recommendation priority is lower than the minimum level justified by the case."
        )

    human_review_required = recommendation.human_review_required
    if payload.decision_case.recommended_review_by_human:
        human_review_required = True
        guardrail_notes.append(
            "Human review remained mandatory because the decision case explicitly required it."
        )

    if recommendation.action_type in _RISKY_ACTION_TYPES and not human_review_required:
        human_review_required = True
        guardrail_notes.append(
            "Human review was forced because the selected action has meaningful operational risk."
        )

    if human_review_required != recommendation.human_review_required:
        updates["human_review_required"] = human_review_required

    final_confidence = recommendation.confidence
    visibility_level = payload.decision_case.visibility_level.value
    untrusted_signals = sum(
        1 for signal in payload.decision_case.observed_signals if not signal.is_trusted
    )

    if visibility_level == "blind" and final_confidence != ConfidenceLevel.LOW:
        final_confidence = ConfidenceLevel.LOW
        guardrail_notes.append(
            "Confidence was reduced to low because the case visibility level is blind."
        )
    elif visibility_level == "limited" and final_confidence == ConfidenceLevel.HIGH:
        final_confidence = ConfidenceLevel.MEDIUM
        guardrail_notes.append(
            "Confidence was reduced because the case visibility level is limited."
        )
    elif untrusted_signals > 0 and final_confidence == ConfidenceLevel.HIGH:
        final_confidence = ConfidenceLevel.MEDIUM
        guardrail_notes.append(
            "Confidence was reduced because at least one observed signal is not trusted."
        )

    if final_confidence != recommendation.confidence:
        updates["confidence"] = final_confidence

    action_summary = recommendation.action_summary.strip()
    rationale = recommendation.rationale.strip()

    if not action_summary:
        raise ValueError("LLM recommendation returned an empty action_summary.")
    if not rationale:
        raise ValueError("LLM recommendation returned an empty rationale.")

    if len(action_summary) > 220:
        action_summary = action_summary[:220].rstrip()
        updates["action_summary"] = action_summary
        guardrail_notes.append("Action summary was trimmed to keep it concise.")

    if len(rationale) > 600:
        rationale = rationale[:600].rstrip()
        updates["rationale"] = rationale
        guardrail_notes.append("Rationale was trimmed to keep it concise.")

    next_checks = recommendation.next_checks[:6]
    if len(next_checks) < 2:
        raise ValueError("LLM recommendation returned too few next_checks items.")
    if next_checks != recommendation.next_checks:
        updates["next_checks"] = next_checks
        guardrail_notes.append("Extra next_checks items were trimmed.")

    decision_trace = recommendation.decision_trace[:8]
    if len(decision_trace) < 3:
        raise ValueError("LLM recommendation returned too few decision_trace items.")
    if decision_trace != recommendation.decision_trace:
        updates["decision_trace"] = decision_trace
        guardrail_notes.append("Extra decision_trace items were trimmed.")

    if guardrail_notes:
        updated_trace = list(updates.get("decision_trace", recommendation.decision_trace))
        updated_trace.extend(guardrail_notes)
        updates["decision_trace"] = updated_trace[:8]

    if updates:
        recommendation = recommendation.model_copy(update=updates)

    recommendation, policy_notes = _enforce_high_severity_backup_policy(
        recommendation=recommendation,
        payload=payload,
    )

    if policy_notes:
        updated_trace = list(recommendation.decision_trace)
        updated_trace.extend(policy_notes)

        recommendation = recommendation.model_copy(
            update={
                "decision_trace": updated_trace[:8],
            }
        )

    return recommendation


def _parse_recommendation_response(
    raw_response: dict[str, Any],
    payload: MinimalExecutionPayload,
) -> Recommendation:
    """Validate and normalize the LLM response into the Recommendation contract."""

    recommendation = Recommendation(
        recommendation_id=f"rec_{payload.decision_case.case_id}",
        case_id=payload.decision_case.case_id,
        priority=RecommendationPriority(str(raw_response["priority"]).strip()),
        action_type=RecommendedActionType(str(raw_response["action_type"]).strip()),
        action_summary=str(raw_response["action_summary"]).strip(),
        rationale=str(raw_response["rationale"]).strip(),
        confidence=ConfidenceLevel(str(raw_response["confidence"]).strip()),
        human_review_required=bool(raw_response["human_review_required"]),
        implicated_asset_ids=payload.decision_case.affected_asset_ids,
        next_checks=_normalize_text_list(
            raw_response.get("next_checks", []),
            field_name="next_checks",
            min_items=2,
            max_items=6,
        ),
        decision_trace=_normalize_text_list(
            raw_response.get("decision_trace", []),
            field_name="decision_trace",
            min_items=3,
            max_items=8,
        ),
    )

    return _apply_guardrails(recommendation, payload)


def _append_fallback_trace(
    recommendation: Recommendation,
    reason: str,
) -> Recommendation:
    """Return a copy of the recommendation with explicit fallback trace information."""

    updated_trace = list(recommendation.decision_trace)
    updated_trace.append(f"Fallback to deterministic orchestrator triggered: {reason}")

    updated_rationale = (
        f"{recommendation.rationale} Deterministic fallback was used because {reason}."
    )

    return recommendation.model_copy(
        update={
            "decision_trace": updated_trace[:8],
            "rationale": updated_rationale[:600],
        }
    )


def generate_llm_recommendation(
    payload: MinimalExecutionPayload,
    *,
    allow_fallback: bool = True,
) -> Recommendation:
    """Generate a recommendation using OpenAI, with deterministic fallback when enabled."""

    system_prompt = _build_system_prompt()
    user_prompt = _build_user_prompt(payload)

    try:
        raw_response = request_json_response(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=0.2,
        )
        return _parse_recommendation_response(raw_response, payload)

    except OpenAIConfigurationError as exc:
        if not allow_fallback:
            raise
        fallback = generate_recommendation(payload)
        return _append_fallback_trace(fallback, str(exc))

    except Exception as exc:
        if not allow_fallback:
            raise
        fallback = generate_recommendation(payload)
        return _append_fallback_trace(fallback, f"LLM generation failed: {exc}")