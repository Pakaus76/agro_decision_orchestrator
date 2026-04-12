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

    serialized_payload = json.dumps(_serialize_payload(payload), indent=2, ensure_ascii=False)

    return (
        "Analyze the following validated greenhouse decision payload and generate "
        "the best operational recommendation.\n\n"
        "Important constraints:\n"
        "- Keep the recommendation grounded in the provided data.\n"
        "- Prefer safe operational behavior under uncertainty.\n"
        "- Require human review when the action has meaningful operational risk.\n"
        "- Keep action_summary and rationale short but clear.\n"
        "- next_checks must be a list of short actionable items.\n"
        "- decision_trace must be a list of short reasoning steps.\n\n"
        f"Payload:\n{serialized_payload}"
    )


def _parse_recommendation_response(
    raw_response: dict[str, Any],
    payload: MinimalExecutionPayload,
) -> Recommendation:
    """Validate and normalize the LLM response into the Recommendation contract."""

    return Recommendation(
        recommendation_id=f"rec_{payload.decision_case.case_id}",
        case_id=payload.decision_case.case_id,
        priority=RecommendationPriority(raw_response["priority"]),
        action_type=RecommendedActionType(raw_response["action_type"]),
        action_summary=str(raw_response["action_summary"]),
        rationale=str(raw_response["rationale"]),
        confidence=ConfidenceLevel(raw_response["confidence"]),
        human_review_required=bool(raw_response["human_review_required"]),
        implicated_asset_ids=payload.decision_case.affected_asset_ids,
        next_checks=[str(item) for item in raw_response.get("next_checks", [])],
        decision_trace=[str(item) for item in raw_response.get("decision_trace", [])],
    )


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
            "decision_trace": updated_trace,
            "rationale": updated_rationale,
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