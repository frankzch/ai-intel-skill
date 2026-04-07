# AI Intelligence Skill

<p align="center">
  <img src="./assets/logo.jpg" alt="AI Intelligence Skill" width="600">
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/frankzch/ai-news-skill/blob/main/LICENSE)
[![Agent Skills](https://img.shields.io/badge/AgentSkills-compatible-blue)](https://agentskills.io/)

[English](./README.en.md) | [中文](./README.md)

---

This is an agent skill that fetches real-time, comprehensive, and deeply filtered first-hand AI intelligence. **Completely free, works out of the box — no API keys needed, no self-scraping required.**

📊 Currently aggregating **75 AI sources** (and growing — contributions of new sources are welcome!), including:
- **15 News Sources** — covering mainstream AI/ML industry media like TechReview, TheVerge AI, Venturebeat, artificialintelligence-news, TechCrunch, Machine Learning Mastery, MarkTechPost, plus official blogs from Nvidia Blog, Apple AI, Microsoft Blog, Google Deepmind Blog, OpenAI, Google Research Blog, etc.
- **46 Social Media Hotspots** — including Reddit, X, HackerNews and other major social platforms, trending topics, hot keywords, and top KOL accounts. X KOLs include: Andrej Karpathy, Sam Altman, Peter Steinberger, Aditya Agarwal, Dan Shipper, Nikunj Kothari, Ryo Lu, Matt Turck, Aaron Levie, Alex Albert, Guillermo Rauch, Amjad Masad, Amanda Askell, Madhu Guru, Kevin Weil, etc.
- **13 Top Video Creators** — leading YouTube AI content creators, including: Matt Wolfe, Dwarkesh Patel, DataDrivenNYC, Latent Space, Sequoia Capital, Yannic Kilcher, NoPriorsPodcast, RedpointAI, EveryInc, Fireship, Lex Fridman, Wes Roth, etc.
- **GitHub Trending** — weekly hot AI repositories

> 🔄 All sources are automatically refreshed every **3 hours**

### 🌟 Powered by InBrief.info
The data processing behind this Agent Skill is powered for free by **[InBrief.info](https://inbrief.info)**. If you just want to browse the latest, highest-quality AI news directly via a web page, we highly recommend visiting **[InBrief.info](https://inbrief.info)** for your personalized daily briefing — no Agent setup needed!

<p align="center">
  <img src="./assets/screenshot_news_en.png" alt="News" width="48%">
  <img src="./assets/screenshot_social_en.png" alt="Social" width="48%">
</p>
<p align="center">
  <img src="./assets/screenshot_video_en.png" alt="Video" width="48%">
  <img src="./assets/screenshot_opensource_en.png" alt="Open Source" width="48%">
</p>

### ⚡ Quick Start
Install this skill into your AI agent (supports OpenClaw, Claude Code, Antigravity, Codex)

**OpenClaw**
```bash
# Currently manual installation, will be submitted to ClawHub later
git clone https://github.com/frankzch/ai-news-skill.git ~/skills/ai-news-skill
```

**Claude Code**
```bash
git clone https://github.com/frankzch/ai-news-skill.git ~/.claude/skills/ai-news-skill
```

**Antigravity Agent**
```bash
git clone https://github.com/frankzch/ai-news-skill.git ~/.agents/skills/ai-news-skill
```

**Codex**
```bash
git clone https://github.com/frankzch/ai-news-skill.git ~/.codex/skills/ai-news-skill
```

### 🎛️ Modifying Settings & Filters
No complex configuration needed — just control your Agent through natural conversation. For example:
- "Show me AI videos released by top KOLs in the past 5 days"
- "Give me today's AI news, but exclude TechReview"
- "Fetch Reddit AI discussions from the past 3 days"

The agent automatically understands your intent and translates it into precise filtering conditions. You can control:

- 📂 **Filter by Category** — Include or exclude content types: News, Open Source, Social Discussions, KOL Insights
- 📡 **Filter by Source** — Include or exclude specific platforms (e.g., Reddit, TechCrunch, etc.)
- ⏰ **Time Range** — Customize how far back to fetch (default: past 24 hours)
- 🔢 **Result Limit** — Control the number of items returned (default: 20)
- 📝 **Summary Display** — Choose whether to show short summaries, long summaries
- 🔗 **Link Display** — Choose whether to show original article links
- 🌐 **Language** — Choose output language (English or Chinese). Defaults to your system language; falls back to English if neither
- 💾 **Output Format** — Results can be printed directly to the terminal or exported as a JSON file

### 🔧 AgentSkills Compatible
This skill follows the [AgentSkills](https://agentskills.io/) open standard. The `SKILL.md` file contains all metadata and instructions needed for any compatible agent to discover, activate, and execute this skill automatically.

### 🤝 Contributing
We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### 📄 License
This project is licensed under the [MIT License](./LICENSE).
