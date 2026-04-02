---
name: PulseAI
description: |
  Fetch the latest AI/ML news, open-source projects, social media discussions, and KOL perspectives.
  Supports sophisticated filtering by categories and sources.
---

# PulseAI Skill

When a user wants to explore recent AI news, open source AI projects, or social media discussions, run the `pulse_fetcher.py` script.
**Important**: You don't need any API credentials. Rate limits are applied based on IP interval and daily limits.

## Configuration & Filters

When running the fetch request, map the user's intent to specific parameters.
Available categories: `news`, `opensource`, `discussion`, `kol`

Examples:
- "Only show Reddit AI discussions": `--include-categories discussion --include-sources reddit`
- "Latest AI open source stuff, don't show Github": `--include-categories opensource --exclude-sources github`

### Execution
Run `python scripts/pulse_fetcher.py [options]` inside the skill directory.

Options:
  --include-categories "cat1,cat2" (Comma separated. Will ignore exclude-categories if used)
  --exclude-categories "cat1,cat2" (Comma separated)
  --include-sources "src1,src2" (Comma separated. Will ignore exclude-sources if used)
  --exclude-sources "src1,src2" (Comma separated)
  --hours INT (default 24)
  --limit INT (default 20)

**Error Handling**:
If you receive HTTP 429 Too Many Requests, explain to the user that they hit an IP rate limit (either the immediate anti-spam interval or the daily max cap) and should wait.
