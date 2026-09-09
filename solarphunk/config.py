"""Central place for model selection so the rest of the code stays provider-agnostic.

Everything is driven by environment variables (see .env.example). Swapping providers
is a config change, never a code change.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

load_dotenv()

DEFAULT_MODEL = "anthropic:claude-sonnet-5"


@dataclass(frozen=True)
class Settings:
    model: str = field(default_factory=lambda: os.getenv("AGENT_MODEL", DEFAULT_MODEL))
    fallback_models: tuple[str, ...] = field(
        default_factory=lambda: tuple(
            m.strip()
            for m in os.getenv("AGENT_FALLBACK_MODELS", "").split(",")
            if m.strip()
        )
    )
    subagent_model: str = field(
        default_factory=lambda: os.getenv("AGENT_SUBAGENT_MODEL", "")
        or os.getenv("AGENT_MODEL", DEFAULT_MODEL)
    )
    temperature: float = field(
        default_factory=lambda: float(os.getenv("AGENT_TEMPERATURE", "0"))
    )
    checkpoint_db: str = field(
        default_factory=lambda: os.getenv("AGENT_CHECKPOINT_DB", "").strip()
    )


def _init_one(spec: str, temperature: float) -> BaseChatModel:
    """Build a single chat model from a "<provider>:<model>" string.

    `init_chat_model` understands anthropic, openai, google_genai, groq, ollama,
    bedrock, and more, so new providers need no code here.
    """
    return init_chat_model(spec, temperature=temperature)


def build_model(settings: Settings | None = None) -> BaseChatModel:
    """Primary model, with an optional fallback chain layered on top."""
    settings = settings or Settings()
    primary = _init_one(settings.model, settings.temperature)
    if not settings.fallback_models:
        return primary
    fallbacks = [_init_one(s, settings.temperature) for s in settings.fallback_models]
    return primary.with_fallbacks(fallbacks)


def build_subagent_model(settings: Settings | None = None) -> BaseChatModel:
    """Cheaper/faster model for delegated sub-agent tasks."""
    settings = settings or Settings()
    return _init_one(settings.subagent_model, settings.temperature)
