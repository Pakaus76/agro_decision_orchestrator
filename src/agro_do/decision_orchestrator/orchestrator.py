"""Core orchestration logic for the Agro Decision Orchestrator service."""

from __future__ import annotations

from agro_do.bridge.loader import MinimalExecutionPayload
from agro_do.domain import (
    ConfidenceLevel,
    RecommendedActionType,
    Recommendation,
    RecommendationPriority,
    SeverityLevel,
    VisibilityLevel,
)


def _map_severity_to_priority(severity: SeverityLevel) -> RecommendationPriority:
    """Map the case severity hint to the baseline recommendation priority."""

    mapping = {
        SeverityLevel.LOW: RecommendationPriority.LOW,
        SeverityLevel.MEDIUM: RecommendationPriority.MEDIUM,
        SeverityLevel.HIGH: RecommendationPriority.HIGH,
        SeverityLevel.CRITICAL: RecommendationPriority.CRITICAL,
    }
    return mapping[severity]


def _detect_backup_option(payload: MinimalExecutionPayload) -> bool:
    """Detect whether the operational context explicitly mentions an available backup."""

    for context_note in payload.decision_case.operational_context:
        combined_text = f"{context_note.note} {context_note.impact or ''}".lower()
        if "backup" in combined_text and "available" in combined_text:
            return True
    return False


def _count_untrusted_signals(payload: MinimalExecutionPayload) -> int:
    """Count how many observed signals are currently marked as untrusted."""

    return sum(
        1 for signal in payload.decision_case.observed_signals if not signal.is_trusted
    )


def _count_out_of_range_signals(payload: MinimalExecutionPayload) -> int:
    """Count how many observed signals are outside the expected range."""

    return sum(
        1
        for signal in payload.decision_case.observed_signals
        if signal.is_out_of_expected_range
    )


def _adjust_priority_for_visibility(
    initial_priority: RecommendationPriority,
    visibility_level: VisibilityLevel,
) -> RecommendationPriority:
    """Escalate priority when visibility is poor and operational uncertainty is high."""

    if visibility_level in {VisibilityLevel.LIMITED, VisibilityLevel.BLIND}:
        if initial_priority == RecommendationPriority.LOW:
            return RecommendationPriority.MEDIUM
        if initial_priority == RecommendationPriority.MEDIUM:
            return RecommendationPriority.HIGH
    return initial_priority


def _select_action_type(
    priority: RecommendationPriority,
    has_backup_option: bool,
    visibility_level: VisibilityLevel,
) -> RecommendedActionType:
    """Select the main action type for the recommendation."""

    if visibility_level == VisibilityLevel.BLIND:
        return RecommendedActionType.ESCALATE_TO_HUMAN

    if priority == RecommendationPriority.CRITICAL:
        if has_backup_option:
            return RecommendedActionType.SWITCH_TO_BACKUP
        return RecommendedActionType.STOP_AND_REVIEW

    if priority == RecommendationPriority.HIGH:
        if has_backup_option:
            return RecommendedActionType.SWITCH_TO_BACKUP
        return RecommendedActionType.ESCALATE_TO_HUMAN

    if priority == RecommendationPriority.MEDIUM:
        return RecommendedActionType.INSPECT

    return RecommendedActionType.CONTINUE_WITH_MONITORING


def _build_action_summary(
    action_type: RecommendedActionType,
    has_backup_option: bool,
) -> str:
    """Build a concise human-readable action summary."""

    if action_type == RecommendedActionType.SWITCH_TO_BACKUP and has_backup_option:
        return "Inspect the main irrigation path and prepare a controlled switch to the backup pump."
    if action_type == RecommendedActionType.STOP_AND_REVIEW:
        return "Stop the affected operation and perform immediate human review."
    if action_type == RecommendedActionType.ESCALATE_TO_HUMAN:
        return "Escalate the case to human review and inspect the irrigation system immediately."
    if action_type == RecommendedActionType.INSPECT:
        return "Inspect the affected assets and confirm the source of the irrigation anomaly."
    return "Continue operation with close monitoring while confirming whether the anomaly persists."


def _build_confidence(
    payload: MinimalExecutionPayload,
    visibility_level: VisibilityLevel,
    untrusted_signals: int,
) -> ConfidenceLevel:
    """Estimate qualitative confidence for the recommendation."""

    if visibility_level in {VisibilityLevel.LIMITED, VisibilityLevel.BLIND}:
        return ConfidenceLevel.LOW

    if untrusted_signals > 0:
        return ConfidenceLevel.MEDIUM

    if len(payload.decision_case.observed_signals) >= 2:
        return ConfidenceLevel.HIGH

    return ConfidenceLevel.MEDIUM


def _build_next_checks(
    payload: MinimalExecutionPayload,
    has_backup_option: bool,
) -> list[str]:
    """Build the ordered next checks for the operator."""

    next_checks = [
        "Confirm whether the abnormal pressure and flow readings are persistent.",
        "Inspect the main irrigation pump for degradation symptoms or instability.",
        "Verify filter condition before confirming pump failure as the primary cause.",
    ]

    if has_backup_option:
        next_checks.append(
            "Prepare the backup pump as a fallback path if instability continues."
        )

    if payload.decision_case.visibility_level in {
        VisibilityLevel.LIMITED,
        VisibilityLevel.BLIND,
    }:
        next_checks.append(
            "Confirm which telemetry and actuator feedback channels are currently trustworthy."
        )

    return next_checks


def _build_decision_trace(
    payload: MinimalExecutionPayload,
    initial_priority: RecommendationPriority,
    final_priority: RecommendationPriority,
    action_type: RecommendedActionType,
    has_backup_option: bool,
    untrusted_signals: int,
    out_of_range_signals: int,
) -> list[str]:
    """Build a compact reasoning trace for explainability."""

    trace = [
        f"Severity hint received from case: {payload.decision_case.severity_hint.value}.",
        f"Initial priority mapped from severity: {initial_priority.value}.",
        f"Observed out-of-range signals: {out_of_range_signals}.",
        f"Untrusted observed signals: {untrusted_signals}.",
        f"Visibility level considered: {payload.decision_case.visibility_level.value}.",
    ]

    if final_priority != initial_priority:
        trace.append(
            f"Priority adjusted due to uncertainty and visibility constraints: {final_priority.value}."
        )
    else:
        trace.append("No priority escalation was required after context evaluation.")

    if has_backup_option:
        trace.append("Operational context confirms an available backup option.")
    else:
        trace.append("No available backup option was confirmed in the operational context.")

    trace.append(f"Selected action type: {action_type.value}.")

    return trace


def _build_rationale(
    payload: MinimalExecutionPayload,
    final_priority: RecommendationPriority,
    has_backup_option: bool,
    out_of_range_signals: int,
) -> str:
    """Build a concise rationale for the recommendation."""

    backup_text = (
        "A fallback backup path is available."
        if has_backup_option
        else "No explicit backup path was confirmed."
    )

    return (
        "The recommendation is based on the decision-case severity, the consistency of the "
        "observed irrigation signals, and the operational context of the greenhouse. "
        f"The case contains {out_of_range_signals} out-of-range signal(s), and the final "
        f"priority was set to {final_priority.value}. {backup_text}"
    )


def generate_recommendation(payload: MinimalExecutionPayload) -> Recommendation:
    """Generate a deterministic recommendation for a validated execution payload."""

    decision_case = payload.decision_case

    initial_priority = _map_severity_to_priority(decision_case.severity_hint)
    final_priority = _adjust_priority_for_visibility(
        initial_priority=initial_priority,
        visibility_level=decision_case.visibility_level,
    )

    has_backup_option = _detect_backup_option(payload)
    untrusted_signals = _count_untrusted_signals(payload)
    out_of_range_signals = _count_out_of_range_signals(payload)

    action_type = _select_action_type(
        priority=final_priority,
        has_backup_option=has_backup_option,
        visibility_level=decision_case.visibility_level,
    )

    confidence = _build_confidence(
        payload=payload,
        visibility_level=decision_case.visibility_level,
        untrusted_signals=untrusted_signals,
    )

    human_review_required = decision_case.recommended_review_by_human or (
        action_type
        in {
            RecommendedActionType.SWITCH_TO_BACKUP,
            RecommendedActionType.ESCALATE_TO_HUMAN,
            RecommendedActionType.STOP_AND_REVIEW,
        }
    )

    action_summary = _build_action_summary(
        action_type=action_type,
        has_backup_option=has_backup_option,
    )

    next_checks = _build_next_checks(
        payload=payload,
        has_backup_option=has_backup_option,
    )

    decision_trace = _build_decision_trace(
        payload=payload,
        initial_priority=initial_priority,
        final_priority=final_priority,
        action_type=action_type,
        has_backup_option=has_backup_option,
        untrusted_signals=untrusted_signals,
        out_of_range_signals=out_of_range_signals,
    )

    rationale = _build_rationale(
        payload=payload,
        final_priority=final_priority,
        has_backup_option=has_backup_option,
        out_of_range_signals=out_of_range_signals,
    )

    return Recommendation(
        recommendation_id=f"rec_{decision_case.case_id}",
        case_id=decision_case.case_id,
        priority=final_priority,
        action_type=action_type,
        action_summary=action_summary,
        rationale=rationale,
        confidence=confidence,
        human_review_required=human_review_required,
        implicated_asset_ids=decision_case.affected_asset_ids,
        next_checks=next_checks,
        decision_trace=decision_trace,
    )