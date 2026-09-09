# SolarPhunk

A minimal, **model-agnostic** deep agent built on
[`langchain-ai/deepagents`](https://github.com/langchain-ai/deepagents).
Swapping between Claude, GPT, Gemini, or a self-hosted model is a change to
`.env` — never to code.

## What's in the box

| Piece | File | Purpose |
|---|---|---|
| Model resolution | `solarphunk/config.py` | Reads `AGENT_MODEL` etc.; builds the primary model + optional fallback chain |
| Tools | `solarphunk/tools.py` | `fetch_url`, `word_frequency` — replace with your own |
| Agent assembly | `solarphunk/agent.py` | Wires model + tools + a `summarizer` sub-agent + optional SQLite persistence |
| CLI | `solarphunk/main.py` | `solarphunk "..."`, `--stream`, `--thread` |

The deepagents layer adds the rest for free: a planning/todo tool, a virtual
filesystem the agent reads and writes, sub-agent delegation with isolated
context, and long-thread summarisation.

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
