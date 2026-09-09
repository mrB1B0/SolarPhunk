# SolarPhunk

An open-source platform of projects that apply AI to Solarpunk-style work:
hacking together entirely new **tools, machines, art projects, and inventions**
from old, discarded, broken, donor, or natural materials. The core platform is a
multi-player, agentic, self-healing, secure, and environmentally safe set of
technology solutions, built around a set of core principles derived from the
Solarpunk movement.

## Project docs

| Doc | What it covers |
|---|---|
| [docs/principles.md](docs/principles.md) | Core principles and the platform obligations they impose |
| [docs/ideas.md](docs/ideas.md) | Seed ideas to prime the Ideator, plus the idea template |
| [docs/agent-roles.md](docs/agent-roles.md) | Agentic worker roles and the propose / gate / platform trust model |
| [docs/architecture.md](docs/architecture.md) | Target platform architecture, data model, and phased roadmap |

Everything above is a **v0 draft** meant to be argued with.

## Status

Phase 0. This repo currently contains the **agent scaffold** — a model-agnostic
`deepagents` runtime that the platform's worker roles will be built on:

| Piece | File | Purpose |
|---|---|---|
| Model resolution | `solarphunk/config.py` | Reads `AGENT_MODEL` etc.; builds the primary model + optional fallback chain |
| Tools | `solarphunk/tools.py` | `fetch_url`, `word_frequency` — placeholders for real agent tools |
| Agent assembly | `solarphunk/agent.py` | Wires model + tools + a `summarizer` sub-agent + optional SQLite persistence |
| CLI | `solarphunk/main.py` | `solarphunk "..."`, `--stream`, `--thread` |

Swapping between Claude, GPT, Gemini, or a self-hosted model is a change to
`.env` — never to code. The deepagents layer supplies a planning tool, a virtual
filesystem, sub-agent delegation, and long-thread summarisation.

## Setup

```powershell
uv sync
Copy-Item .env.example .env
```

Edit `.env`: set `AGENT_MODEL` and the matching API key. Only the providers you
name need a key.

### Windows path-length note

This project's dependency tree (the `anthropic` SDK especially) has very deeply
nested files. Keep the project at a **short path** like `C:\dev\SolarPhunk`
(where it lives now) or `uv sync` fails with `failed to persist temporary file` /
`The system cannot find the path specified` once `.venv\Lib\site-packages\...`
crosses the 260-char limit.

If you must nest it deeper, either enable Win32 long paths
(`LongPathsEnabled=1` + `git config --global core.longpaths true`, needs admin),
or push the venv elsewhere with `UV_PROJECT_ENVIRONMENT=C:\some\short\dir`.

## Run

```powershell
uv run solarphunk "Summarize https://github.com/langchain-ai/deepagents and list its top 5 keywords"
uv run solarphunk --stream "Fetch example.com and give me its word frequency"
```

Persistence: set `AGENT_CHECKPOINT_DB` in `.env`, then reuse a thread id to
resume:

```powershell
uv run solarphunk --thread proj1 "Start researching X"
uv run solarphunk --thread proj1 "Now go deeper on the second point"
```

## Switching models

Edit `.env` — nothing else:

```ini
# Claude (default)
AGENT_MODEL=anthropic:claude-sonnet-5

# OpenAI
AGENT_MODEL=openai:gpt-5.5

# Gemini
AGENT_MODEL=google_genai:gemini-2.5-pro

# Primary + automatic fallback if it errors
AGENT_MODEL=anthropic:claude-opus-4-8
AGENT_FALLBACK_MODELS=openai:gpt-5.5,google_genai:gemini-2.5-pro
```

`config.py` uses LangChain's `init_chat_model`, which also understands `groq:`,
`ollama:`, `bedrock:`, `together:` and more — add the matching
`langchain-*` package to `pyproject.toml` and it works with no code change.

The `summarizer` sub-agent runs on `AGENT_SUBAGENT_MODEL` (default a cheap
Haiku) so bulk condensing doesn't burn your primary model's budget.

## Notes / gotchas

- Tool-calling reliability, parallel tool calls, and prompt caching vary by
  provider. A prompt tuned on Claude may need tweaks when routed to another
  model.
- The virtual filesystem lives in graph state — nothing touches real disk
  unless you attach a filesystem backend in `agent.py`.
- Add [LangSmith](https://smith.langchain.com) tracing by setting
  `LANGSMITH_API_KEY` and `LANGSMITH_TRACING=true` in `.env`.
