"""Decision-case contracts for the Agro Decision Orchestrator."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from .models import CropPhase


class CaseSource(str, Enum):
    """Indicates how a decision case was created."""

    SIMULATED = "simulated"
    MANUAL = "manual"
    IMPORTED = "imported"
    LIVE_SYSTEM = "live_system"


class SeverityLevel(str, Enum):
    """Simple severity hint used before orchestration logic is applied."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class VisibilityLevel(str, Enum):
    """Represents how much trustworthy visibility is available for the case."""

    FULL = "full"
    PARTIAL = "partial"
    LIMITED = "limited"
    BLIND = "blind"


class ObservedSignal(BaseModel):
    """Represents one relevant observed signal attached to the decision case."""

    signal_id: str = Field(..., description="Unique signal identifier inside the case.")
    metric_name: str = Field(..., description="Human-readable name of the metric.")
    sensor_id: Optional[str] = Field(
        default=None,
        description="Related sensor identifier when available.",
    )
    value: str = Field(
        ...,
        description="Observed value represented as text for flexibility in the MVP.",
    )
    unit: Optional[str] = Field(
        default=None,
        description="Measurement unit when applicable.",
    )
    interpretation: Optional[str] = Field(
        default=None,
        description="Short interpretation of why the signal matters.",
    )
    is_out_of_expected_range: bool = Field(
        default=False,
        description="Whether the signal is outside the expected operating range.",
    )
    is_trusted: bool = Field(
        default=True,
        description="Whether the signal is currently considered trustworthy.",
    )


class ContextNote(BaseModel):
    """Represents contextual information that may influence the decision."""

    category: str = Field(
        ...,
        description="Context category, for example operational, agronomic, or business.",
    )
    note: str = Field(..., description="Context note content.")
    impact: Optional[str] = Field(
        default=None,
        description="Short description of how this context may affect the decision.",
    )


class DecisionCase(BaseModel):
    """Represents a normalized agricultural case to be evaluated by the orchestrator."""

    case_id: str = Field(..., description="Unique decision-case identifier.")
    title: str = Field(..., description="Short human-readable case title.")
    summary: str = Field(..., description="Short summary of the decision situation.")
    greenhouse_id: str = Field(..., description="Related greenhouse identifier.")
    sector_id: Optional[str] = Field(
        default=None,
        description="Related sector identifier when the case is sector-specific.",
    )
    crop_phase: Optional[CropPhase] = Field(
        default=None,
        description="Crop phase relevant to the case when known.",
    )
    source: CaseSource = Field(..., description="Origin of the decision case.")
    suspected_issue: str = Field(
        ...,
        description="Short description of the suspected issue or anomaly.",
    )
    severity_hint: SeverityLevel = Field(
        ...,
        description="Initial severity hint before orchestration logic is applied.",
    )
    visibility_level: VisibilityLevel = Field(
        default=VisibilityLevel.FULL,
        description="How much trustworthy visibility is available for the case.",
    )
    affected_asset_ids: list[str] = Field(
        default_factory=list,
        description="Identifiers of assets believed to be involved in the case.",
    )
    related_sensor_ids: list[str] = Field(
        default_factory=list,
        description="Identifiers of sensors directly related to the case.",
    )
    related_actuator_ids: list[str] = Field(
        default_factory=list,
        description="Identifiers of actuators directly related to the case.",
    )
    symptoms: list[str] = Field(
        default_factory=list,
        description="Observed symptoms expressed in operational language.",
    )
    observed_signals: list[ObservedSignal] = Field(
        default_factory=list,
        description="Signals that support the case description.",
    )
    operational_context: list[ContextNote] = Field(
        default_factory=list,
        description="Operational constraints or relevant operational context.",
    )
    agronomic_context: list[ContextNote] = Field(
        default_factory=list,
        description="Agronomic context that may change the decision logic.",
    )
    business_context: list[ContextNote] = Field(
        default_factory=list,
        description="Business or service context that may affect prioritization.",
    )
    recommended_review_by_human: bool = Field(
        default=False,
        description="Whether the case already suggests human review before action.",
    )
    notes: Optional[str] = Field(
        default=None,
        description="Optional free-text note for additional context.",
    )