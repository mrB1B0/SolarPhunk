"""Example tools for the agent.

Keep tools small, well-typed, and docstring'd -- the docstring is what the model
sees when deciding whether to call them. Add your own here.
"""

from __future__ import annotations

import httpx
from langchain_core.tools import tool

_HTTP_TIMEOUT = 20.0
_MAX_CHARS = 8_000


@tool
def fetch_url(url: str) -> str:
    """Fetch a URL over HTTP(S) and return its response body as text.

    Use this to look at a web page or JSON API the user references. Returns at
    most ~8k characters; long bodies are truncated.
    """
    if not url.lower().startswith(("http://", "https://")):
        return "Error: url must start with http:// or https://"
    try:
        resp = httpx.get(
            url,
            timeout=_HTTP_TIMEOUT,
            follow_redirects=True,
            headers={"User-Agent": "solarphunk/0.1"},
        )
        resp.raise_for_status()
    except httpx.HTTPError as exc:  # network error, bad status, timeout
        return f"Error fetching {url}: {exc}"
    body = resp.text
    if len(body) > _MAX_CHARS:
        body = body[:_MAX_CHARS] + f"\n...[truncated {len(resp.text) - _MAX_CHARS} chars]"
    return body


@tool
def word_frequency(text: str, top_n: int = 10) -> dict[str, int]:
    """Return the `top_n` most common whitespace-delimited words in `text`.

    Punctuation is stripped and matching is case-insensitive. Handy for quick
    summarisation or keyword extraction over fetched content.
    """
    import re
    from collections import Counter

    words = re.findall(r"[a-z0-9']+", text.lower())
    return dict(Counter(words).most_common(max(1, top_n)))


ALL_TOOLS = [fetch_url, word_frequency]
