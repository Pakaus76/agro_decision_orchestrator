"""OpenAI client adapter for the Agro Decision Orchestrator."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

from openai import OpenAI


class OpenAIConfigurationError(RuntimeError):
    """Raised when the OpenAI client cannot be configured correctly."""


@dataclass(frozen=True)
class OpenAIClientSettings:
    """Configuration values required to initialize the OpenAI client."""

    api_key: str
    model: str


def load_openai_settings() -> OpenAIClientSettings:
    """Load OpenAI settings from environment variables."""

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not api_key:
        raise OpenAIConfigurationError(
            "OPENAI_API_KEY is not configured. "
            "Set it in your local environment before using the generative orchestrator."
        )

    return OpenAIClientSettings(api_key=api_key, model=model)


def build_openai_client() -> tuple[OpenAI, OpenAIClientSettings]:
    """Create an OpenAI client and return it together with its settings."""

    settings = load_openai_settings()
    client = OpenAI(api_key=settings.api_key)
    return client, settings


def request_json_response(
    *,
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0.2,
) -> dict[str, Any]:
    """Request a JSON response from OpenAI using the configured model."""

    client, settings = build_openai_client()

    response = client.responses.create(
        model=settings.model,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        text={"format": {"type": "json_object"}},
    )

    if not response.output_text:
        raise RuntimeError("OpenAI response did not contain output_text.")

    # The API is instructed to return a JSON object, so parsing is expected upstream.
    import json

    return json.loads(response.output_text)