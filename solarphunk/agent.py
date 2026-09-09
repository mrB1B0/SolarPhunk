"""Assemble the deep agent: model + tools + sub-agents + optional persistence."""

from __future__ import annotations

from typing import Any

from deepagents import create_deep_agent

from solarphunk.config import Settings, build_model, build_subagent_model
from solarphunk.tools import ALL_TOOLS

SYSTEM_PROMPT = """\
You are a capable research assistant.

Work in this loop:
1. Use the planning tool (write_todos) to break non-trivial requests into steps.
2. Gather facts with your tools (fetch_url, word_frequency) instead of guessing.
3. For long documents, delegate condensing to the `summarizer` sub-agent via `task`.
4. Write intermediate notes and the final answer to the virtual filesystem.
5. Finish with a concise, sourced summary in your reply.
"""

SUMMARIZER_SUBAGENT: dict[str, Any] = {
    "name": "summarizer",
    "description": (
        "Condenses long text into tight, faithful summaries. Delegate bulky "
        "content here to keep the main context small."
    ),
    "prompt": (
        "You summarise text accurately and concisely. Preserve facts, numbers, "
        "and named entities. No preamble."
    ),
}

# Module-level ref so a SqliteSaver stays open for the process lifetime.
_CHECKPOINTER_CM = None


def build_agent(settings: Settings | None = None):
    """Return a compiled deep agent graph.

    Model, fallbacks, sub-agent model and persistence are all resolved from
    `Settings` (environment). Nothing here is provider-specific.
    """
    global _CHECKPOINTER_CM
    settings = settings or Settings()

    subagent = dict(SUMMARIZER_SUBAGENT)
    subagent["model"] = build_subagent_model(settings)

    checkpointer = None
    cm = _make_checkpointer(settings)
    if cm is not None:
        _CHECKPOINTER_CM = cm
        checkpointer = cm.__enter__()

    return create_deep_agent(
        model=build_model(settings),
        tools=ALL_TOOLS,
        system_prompt=SYSTEM_PROMPT,
        subagents=[subagent],
        checkpointer=checkpointer,
    )


def _make_checkpointer(settings: Settings):
    """A SqliteSaver context manager, or None for in-memory runs.

    `SqliteSaver.from_conn_string` returns a context manager; the caller enters
    it and keeps the reference alive for the process lifetime.
    """
    if not settings.checkpoint_db:
        return None
    try:
        from langgraph.checkpoint.sqlite import SqliteSaver
    except ImportError:
        return None
    return SqliteSaver.from_conn_string(settings.checkpoint_db)
