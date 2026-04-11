"""Recommendation contracts for the Agro Decision Orchestrator."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class RecommendationPriority(str, Enum):
    """Priority levels used by the deterministic recommendation layer."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ConfidenceLevel(str, Enum):
    """Qualitative confidence levels for recommendation outputs."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class RecommendedActionType(str, Enum):
    """High-level action categories for deterministic recommendations."""

    INSPECT = "inspect"
    SWITCH_TO_BACKUP = "switch_to_backup"
    CONTINUE_WITH_MONITORING = "continue_with_monitoring"
    ADJUST_OPERATION = "adjust_operation"
    ESCALATE_TO_HUMAN = "escalate_to_human"
    STOP_AND_REVIEW = "stop_and_review"
    NO_ACTION = "no_action"


class Recommendation(BaseModel):
    """Represents a normalized recommendation produced by the orchestrator."""

    recommendation_id: str = Field(..., description="Unique recommendation identifier.")
    case_id: str = Field(..., description="Related decision-case identifier.")
    priority: RecommendationPriority = Field(
        ...,
        description="Operational priority assigned to the recommendation.",
    )
    action_type: RecommendedActionType = Field(
        ...,
        description="High-level recommended action category.",
    )
    action_summary: str = Field(
        ...,
        description="Short human-readable summary of the recommended action.",
    )
    rationale: str = Field(
        ...,
        description="Short explanation of why this recommendation was produced.",
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Qualitative confidence level of the recommendation.",
    )
    human_review_required: bool = Field(
        default=False,
        description="Whether human review is required before or during execution.",
    )
    implicated_asset_ids: list[str] = Field(
        default_factory=list,
        description="Assets directly implicated in the recommendation.",
    )
    next_checks: list[str] = Field(
        default_factory=list,
        description="Ordered checks or actions suggested to the operator.",
    )
    decision_trace: list[str] = Field(
        default_factory=list,
        description="Short trace of the main reasoning steps behind the recommendation.",
    )