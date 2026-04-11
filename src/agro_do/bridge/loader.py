"""Minimal loading path for greenhouse blueprints and decision cases."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from agro_do.domain import (
    Actuator,
    Asset,
    CropProfile,
    DecisionCase,
    Greenhouse,
    Sector,
    Sensor,
)


class LoadedBlueprint(BaseModel):
    """Structured representation of a greenhouse blueprint loaded from JSON."""

    greenhouse: Greenhouse = Field(..., description="Top-level greenhouse definition.")
    sectors: list[Sector] = Field(
        default_factory=list,
        description="Operational sectors defined in the blueprint.",
    )
    crop_profile: CropProfile = Field(
        ...,
        description="Crop profile associated with the greenhouse blueprint.",
    )
    assets: list[Asset] = Field(
        default_factory=list,
        description="Assets available in the greenhouse environment.",
    )
    sensors: list[Sensor] = Field(
        default_factory=list,
        description="Sensors available in the greenhouse environment.",
    )
    actuators: list[Actuator] = Field(
        default_factory=list,
        description="Actuators available in the greenhouse environment.",
    )


class MinimalExecutionPayload(BaseModel):
    """Minimal validated payload ready for future orchestration logic."""

    greenhouse: Greenhouse = Field(..., description="Greenhouse context.")
    sectors: list[Sector] = Field(
        default_factory=list,
        description="Sector context relevant to the execution.",
    )
    crop_profile: CropProfile = Field(..., description="Crop profile context.")
    decision_case: DecisionCase = Field(..., description="Normalized decision case.")


def _load_json_dict(file_path: Path) -> dict[str, Any]:
    """Read a JSON file and return its parsed dictionary content."""

    return json.loads(file_path.read_text(encoding="utf-8"))


def load_greenhouse_blueprint(file_path: str | Path) -> LoadedBlueprint:
    """Load and validate a greenhouse blueprint from a JSON file."""

    file_path = Path(file_path)
    raw_data = _load_json_dict(file_path)

    return LoadedBlueprint(
        greenhouse=Greenhouse.model_validate(raw_data["greenhouse"]),
        sectors=[Sector.model_validate(item) for item in raw_data["sectors"]],
        crop_profile=CropProfile.model_validate(raw_data["crop_profile"]),
        assets=[Asset.model_validate(item) for item in raw_data["assets"]],
        sensors=[Sensor.model_validate(item) for item in raw_data["sensors"]],
        actuators=[Actuator.model_validate(item) for item in raw_data["actuators"]],
    )


def load_decision_case(file_path: str | Path) -> DecisionCase:
    """Load and validate a decision case from a JSON file."""

    file_path = Path(file_path)
    raw_data = _load_json_dict(file_path)
    return DecisionCase.model_validate(raw_data)


def build_minimal_execution_payload(
    blueprint: LoadedBlueprint,
    decision_case: DecisionCase,
) -> MinimalExecutionPayload:
    """Validate blueprint-case consistency and build a minimal execution payload."""

    if decision_case.greenhouse_id != blueprint.greenhouse.greenhouse_id:
        raise ValueError(
            "Decision case greenhouse_id does not match the loaded greenhouse blueprint."
        )

    valid_sector_ids = {sector.sector_id for sector in blueprint.sectors}
    valid_asset_ids = {asset.asset_id for asset in blueprint.assets}
    valid_sensor_ids = {sensor.sensor_id for sensor in blueprint.sensors}
    valid_actuator_ids = {actuator.actuator_id for actuator in blueprint.actuators}

    if decision_case.sector_id is not None and decision_case.sector_id not in valid_sector_ids:
        raise ValueError(
            "Decision case sector_id does not exist in the loaded greenhouse blueprint."
        )

    missing_asset_ids = sorted(set(decision_case.affected_asset_ids) - valid_asset_ids)
    missing_sensor_ids = sorted(set(decision_case.related_sensor_ids) - valid_sensor_ids)
    missing_actuator_ids = sorted(set(decision_case.related_actuator_ids) - valid_actuator_ids)

    if missing_asset_ids:
        raise ValueError(
            f"Decision case references unknown asset IDs: {missing_asset_ids}"
        )

    if missing_sensor_ids:
        raise ValueError(
            f"Decision case references unknown sensor IDs: {missing_sensor_ids}"
        )

    if missing_actuator_ids:
        raise ValueError(
            f"Decision case references unknown actuator IDs: {missing_actuator_ids}"
        )

    return MinimalExecutionPayload(
        greenhouse=blueprint.greenhouse,
        sectors=blueprint.sectors,
        crop_profile=blueprint.crop_profile,
        decision_case=decision_case,
    )