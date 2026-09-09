"""CLI entry point: `solarphunk "your request"` or `uv run solarphunk ...`."""

from __future__ import annotations

import argparse
import sys
import uuid

from solarphunk.agent import build_agent
from solarphunk.config import Settings


def _parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="solarphunk",
        description="Run the model-agnostic deep agent on a single request.",
    )
    p.add_argument("prompt", nargs="*", help="The request. If omitted, read from stdin.")
    p.add_argument(
        "--thread",
        default=None,
        help="Thread id for resumable state (needs AGENT_CHECKPOINT_DB set). "
        "Defaults to a fresh random id.",
    )
    p.add_argument(
        "--stream",
        action="store_true",
        help="Stream intermediate steps instead of printing only the final reply.",
    )
    return p.parse_args(argv)


def _get_prompt(args: argparse.Namespace) -> str:
    if args.prompt:
        return " ".join(args.prompt)
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return input("Request: ").strip()


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv if argv is not None else sys.argv[1:])
    prompt = _get_prompt(args)
    if not prompt:
        print("No prompt given.", file=sys.stderr)
        return 2

    settings = Settings()
    agent = build_agent(settings)

    config = {"configurable": {"thread_id": args.thread or f"cli-{uuid.uuid4().hex[:8]}"}}
    payload = {"messages": [{"role": "user", "content": prompt}]}

    print(f"model={settings.model}  thread={config['configurable']['thread_id']}\n")

    if args.stream:
        last = None
        for chunk in agent.stream(payload, config=config, stream_mode="values"):
            msgs = chunk.get("messages") or []
            if msgs and msgs[-1] is not last:
                last = msgs[-1]
                _print_message(last)
    else:
        result = agent.invoke(payload, config=config)
        _print_message(result["messages"][-1])

    return 0


def _print_message(msg) -> None:
    role = getattr(msg, "type", "?")
    content = getattr(msg, "content", msg)
    if isinstance(content, list):  # some providers return content blocks
        content = "".join(
            b.get("text", "") if isinstance(b, dict) else str(b) for b in content
        )
    tool_calls = getattr(msg, "tool_calls", None)
    if tool_calls:
        names = ", ".join(tc.get("name", "?") for tc in tool_calls)
        print(f"[{role}] -> tool call: {names}")
    if content:
        print(f"[{role}] {content}\n")


if __name__ == "__main__":
    raise SystemExit(main())
