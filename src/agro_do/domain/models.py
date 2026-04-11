"""Core domain models for the Agro Decision Orchestrator."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class AssetCategory(str, Enum):
    """High-level asset categories used across the product domain."""

    IRRIGATION = "irrigation"
    FERTIGATION = "fertigation"
    CLIMATE = "climate"
    CONTROL = "control"
    POWER = "power"
    CROP = "crop"


class AssetRole(str, Enum):
    """Specific operational roles for assets inside the greenhouse domain."""

    PUMP = "pump"
    FILTER = "filter"
    VALVE = "valve"
    TANK = "tank"
    SENSOR = "sensor"
    DOSING_UNIT = "dosing_unit"
    MIXER = "mixer"
    FAN = "fan"
    WINDOW = "window"
    SHADING_SCREEN = "shading_screen"
    CONTROLLER = "controller"
    GATEWAY = "gateway"
    POWER_SUPPLY = "power_supply"
    CROP_ZONE = "crop_zone"
    OTHER = "other"


class SensorType(str, Enum):
    """Supported sensor types for the initial greenhouse MVP."""

    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    PRESSURE = "pressure"
    FLOW = "flow"
    LEVEL = "level"
    PH = "ph"
    EC = "ec"
    RADIATION = "radiation"
    WIND = "wind"
    VPD = "vpd"
    POWER = "power"
    COMMUNICATION_HEARTBEAT = "communication_heartbeat"
    OTHER = "other"


class ActuatorType(str, Enum):
    """Supported actuator types for the initial greenhouse MVP."""

    PUMP = "pump"
    VALVE = "valve"
    DOSING_UNIT = "dosing_unit"
    FAN = "fan"
    WINDOW = "window"
    SHADING_SCREEN = "shading_screen"
    MIXER = "mixer"
    OTHER = "other"


class CropPhase(str, Enum):
    """Simple crop phases for the initial product scope."""

    VEGETATIVE = "vegetative"
    FLOWERING = "flowering"
    FRUIT_SET = "fruit_set"
    PRODUCTION = "production"
    LATE_CYCLE = "late_cycle"


class Greenhouse(BaseModel):
    """Represents the top-level greenhouse entity."""

    greenhouse_id: str = Field(..., description="Unique greenhouse identifier.")
    name: str = Field(..., description="Human-readable greenhouse name.")
    location: str = Field(..., description="Site or farm location.")
    crop_type: str = Field(..., description="Main crop grown in the greenhouse.")
    cultivation_mode: str = Field(..., description="Cultivation mode, for example substrate.")
    sector_ids: list[str] = Field(
        default_factory=list,
        description="Identifiers of sectors belonging to this greenhouse.",
    )


class Sector(BaseModel):
    """Represents an operational greenhouse sector."""

    sector_id: str = Field(..., description="Unique sector identifier.")
    greenhouse_id: str = Field(..., description="Parent greenhouse identifier.")
    name: str = Field(..., description="Human-readable sector name.")
    crop_phase: CropPhase = Field(..., description="Current crop phase in the sector.")
    area_m2: float = Field(..., gt=0, description="Sector area in square meters.")
    irrigation_strategy: Optional[str] = Field(
        default=None,
        description="Short description of the irrigation strategy used in the sector.",
    )
    notes: Optional[str] = Field(
        default=None,
        description="Optional operational notes for the sector.",
    )


class Asset(BaseModel):
    """Represents a physical or logical asset used in the greenhouse."""

    asset_id: str = Field(..., description="Unique asset identifier.")
    greenhouse_id: str = Field(..., description="Parent greenhouse identifier.")
    sector_id: Optional[str] = Field(
        default=None,
        description="Sector identifier when the asset is sector-specific.",
    )
    name: str = Field(..., description="Human-readable asset name.")
    category: AssetCategory = Field(..., description="High-level asset category.")
    role: AssetRole = Field(..., description="Operational asset role.")
    manufacturer: Optional[str] = Field(
        default=None,
        description="Optional manufacturer name.",
    )
    model: Optional[str] = Field(
        default=None,
        description="Optional manufacturer model reference.",
    )
    is_critical: bool = Field(
        default=False,
        description="Whether the asset is considered operationally critical.",
    )
    is_redundant: bool = Field(
        default=False,
        description="Whether the asset has functional redundancy in the system.",
    )
    status: str = Field(
        default="unknown",
        description="Current known status of the asset.",
    )


class Sensor(BaseModel):
    """Represents a sensor attached to the greenhouse environment."""

    sensor_id: str = Field(..., description="Unique sensor identifier.")
    asset_id: str = Field(..., description="Related asset identifier.")
    greenhouse_id: str = Field(..., description="Parent greenhouse identifier.")
    sector_id: Optional[str] = Field(
        default=None,
        description="Sector identifier when the sensor is sector-specific.",
    )
    name: str = Field(..., description="Human-readable sensor name.")
    sensor_type: SensorType = Field(..., description="Sensor classification.")
    unit: str = Field(..., description="Measurement unit.")
    min_expected_value: Optional[float] = Field(
        default=None,
        description="Lower expected boundary for the measurement.",
    )
    max_expected_value: Optional[float] = Field(
        default=None,
        description="Upper expected boundary for the measurement.",
    )
    is_critical: bool = Field(
        default=False,
        description="Whether the sensor is critical for operational decisions.",
    )
    is_trusted_by_default: bool = Field(
        default=True,
        description="Whether the sensor is trusted unless evidence suggests otherwise.",
    )


class Actuator(BaseModel):
    """Represents an actuator that can change the greenhouse state."""

    actuator_id: str = Field(..., description="Unique actuator identifier.")
    asset_id: str = Field(..., description="Related asset identifier.")
    greenhouse_id: str = Field(..., description="Parent greenhouse identifier.")
    sector_id: Optional[str] = Field(
        default=None,
        description="Sector identifier when the actuator is sector-specific.",
    )
    name: str = Field(..., description="Human-readable actuator name.")
    actuator_type: ActuatorType = Field(..., description="Actuator classification.")
    command_type: str = Field(
        ...,
        description="Type of command accepted by the actuator, for example on_off or percentage.",
    )
    feedback_available: bool = Field(
        default=False,
        description="Whether actuator feedback is available to verify execution.",
    )
    manual_override_possible: bool = Field(
        default=True,
        description="Whether the actuator can be manually overridden.",
    )


class CropProfile(BaseModel):
    """Represents crop-specific operational context for one greenhouse or sector."""

    crop_profile_id: str = Field(..., description="Unique crop profile identifier.")
    crop_type: str = Field(..., description="Crop type, for example tomato.")
    crop_phase: CropPhase = Field(..., description="Active crop phase.")
    irrigation_sensitivity: str = Field(
        ...,
        description="Qualitative irrigation sensitivity level.",
    )
    climate_sensitivity: str = Field(
        ...,
        description="Qualitative climate sensitivity level.",
    )
    disease_risk_sensitivity: str = Field(
        ...,
        description="Qualitative disease-risk sensitivity level.",
    )
    target_temperature_min_c: Optional[float] = Field(
        default=None,
        description="Target minimum temperature in Celsius.",
    )
    target_temperature_max_c: Optional[float] = Field(
        default=None,
        description="Target maximum temperature in Celsius.",
    )
    target_humidity_min_pct: Optional[float] = Field(
        default=None,
        description="Target minimum relative humidity percentage.",
    )
    target_humidity_max_pct: Optional[float] = Field(
        default=None,
        description="Target maximum relative humidity percentage.",
    )