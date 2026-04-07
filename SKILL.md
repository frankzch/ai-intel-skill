---
name: ai-news-skill
description: >
  Fetch the latest AI/ML news, trending open-source projects, social media discussions,
  and KOL (Key Opinion Leader) perspectives from 75+ curated sources. Use when the user
  asks about recent AI news, AI trends, what's happening in machine learning, open-source
  AI projects, AI Twitter/Reddit discussions, or wants a daily AI briefing.
license: MIT
compatibility: Requires Python 3.9+ and internet access. Dependencies (requests, pyyaml) are declared inline via PEP 723; use `uv run` for zero-setup execution.
metadata:
  author: frankzch
  version: "1.1"
---

# AI Intelligence Skill

## When to use this skill

Use when the user wants to:
- Get the latest AI/ML news and announcements
- Browse trending open-source AI projects from GitHub
- Read AI discussion highlights from Reddit, X (Twitter), HackerNews
- See what AI KOLs (Key Opinion Leaders) are saying
- Get a comprehensive daily AI briefing

## Workflow

### Default: Fetch latest AI briefing

Run the fetcher script from the skill directory:

```bash
uv run scripts/pulse_fetcher.py
```

If `uv` is not available, install dependencies manually and use:
```bash
pip install requests pyyaml
python scripts/pulse_fetcher.py
```

### Filtered fetch

Map the user's intent to CLI flags:

| User says | Flags |
|-----------|-------|
| "Only Reddit discussions" | `--include-categories discussion --include-sources reddit` |
| "Open source, no Github" | `--include-categories opensource --exclude-sources github` |
| "50 items, past 48 hours" | `--limit 50 --hours 48` |
| "Show full summaries with links" | `--show-long-summary true --show-link true` |
| "AI news in Chinese" | `--include-categories news --language zh` |

### Available options

Run `uv run scripts/pulse_fetcher.py --help` for the full list. Key flags:

- `--include-categories "cat1,cat2"` — Only fetch these categories: `news`, `opensource`, `discussion`, `kol`
- `--exclude-categories "cat1,cat2"` — Skip these categories
- `--include-sources "src1,src2"` — Only from these sources
- `--exclude-sources "src1,src2"` — Skip these sources
- `--hours INT` — Time window in hours (default: 24)
- `--limit INT` — Max items to return (default: 20)
- `--language en|zh` — Output language (default: auto-detect from system locale)
- `--show-short-summary true|false` — Show short summary (default: true)
- `--show-long-summary true|false` — Show long summary (default: false)
- `--show-link true|false` — Show article URLs (default: false)
- `--output-file FILE` — Export full JSON to file (default: pulse_output.json). Pass empty string to disable.

## Output format

Each item is printed as:
```
1. [NEWS] Title of the article (from TechCrunch)
   Short Summary: One-line summary text
----------------------------------------
```

When `--output-file` is used, the full JSON response is saved to disk. See [references/API.md](references/API.md) for the response schema.

## Gotchas

- **HTTP 429** means the user hit an IP rate limit (anti-spam interval or daily cap). Tell them to wait a few minutes and try again.
- **No API keys or registration required.** Rate limits are IP-based.
- Use `--output-file` when links are included — terminal line-wrapping can corrupt long URLs.
- If `config.yaml` exists in the skill root, it overrides default settings. See [assets/config.default.yaml](assets/config.default.yaml) for the template.
- The `--include-*` flags take precedence over `--exclude-*` flags for the same dimension.
