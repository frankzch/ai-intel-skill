# Contributing to AI Intelligence Skill

Thanks for your interest in contributing to AI Intelligence Skill! 🎉

## How to Contribute

### 🐛 Report Bugs
- Open an [Issue](https://github.com/frankzch/ai-news-skill/issues) with a clear description
- Include your agent platform (Claude Code, Antigravity, Codex, OpenClaw)
- Attach any error output from `pulse_fetcher.py`

### 💡 Suggest Features
- Open an Issue tagged with `enhancement`
- Describe your use case and expected behavior

### 🔧 Submit Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

### Good First Issues

We welcome first-time contributors! Look for issues tagged with `good first issue`. Some ideas:

- **Add a new agent platform**: Write installation instructions for a new AI agent
- **Improve output formatting**: Make the fetched results more readable
- **Add new filter options**: Extend `pulse_fetcher.py` with new filtering capabilities
- **Documentation**: Fix typos, improve examples, add translations

## Development Setup

```bash
git clone https://github.com/frankzch/ai-news-skill.git
cd ai-news-skill

# Option 1: Using uv (recommended, zero-setup)
uv run scripts/pulse_fetcher.py --limit 5

# Option 2: Using pip
pip install requests pyyaml
python scripts/pulse_fetcher.py --limit 5
```

## Project Structure (AgentSkills Standard)

```
ai-news-skill/
├── SKILL.md              # Required: metadata + agent instructions
├── scripts/              # Executable scripts
│   └── pulse_fetcher.py  # Main fetcher (PEP 723 self-contained)
├── references/           # Technical documentation
│   └── API.md            # InBrief.info API reference
├── assets/               # Templates, images, resources
│   ├── config.default.yaml
│   └── *.png / *.jpg
├── README.md
├── README.zh-CN.md
├── CONTRIBUTING.md
└── LICENSE
```

## Code Style
- Follow PEP 8 for Python code
- Keep functions focused and well-documented
- Add meaningful commit messages

## Questions?
Feel free to open an Issue or start a Discussion. We're happy to help!
