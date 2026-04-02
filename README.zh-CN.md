# PulseAI 

[English](./README.md) | [中文](./README.zh-CN.md)

---

## 🚀 PulseAI: 专为 AI Agent 打造的通用科技情报外挂

PulseAI 是一个完全开源的**通用大模型 Agent 技能插件 (Skill)**。无论你使用的是 Antigravity, Claude Code, Codex 还是 OpenClaw，PulseAI 都能让你的智能体瞬间拥有抓取最新 AI 新闻、热门开源项目以及社交媒体前沿讨论的能力。

**理念：** 提供实时、高质量、深度过滤的 AI 前沿资讯，抛弃低质量的信息噪音。

### 🌟 由 InBrief.info 强力驱动
此 Agent 技能背后的海量实时数据处理与引擎由 **[InBrief.info](https://inbrief.info)** 免费驱动。如果你只想直接通过网页查阅最新、最优质的 AI 资讯，强烈推荐直接访问 **[InBrief.info](https://inbrief.info)** 获取个性化的专属简报，无需折腾任何 Agent！

### ✨ 你会得到什么
安装此外挂后，你的 Agent 可以立刻抓取以下领域内容并按需为你生成简报：
- **新闻 (News)**：最新的 AI/ML 行业动向。
- **开源 (Open Source)**：GitHub 最新热门仓库和更新。
- **讨论 (Discussions)**：来自 Reddit 等社区的深度干货探讨。
- **KOL**: 追踪 Twitter 顶尖 AI 建造者的第一手观点。

### ⚡ 快速开始
1. 在你的 AI agent 中安装此 skill（支持 OpenClaw, Claude Code, Antigravity, Codex）
2. 要求 Agent："帮我看看今天有什么好玩的开源 AI 项目" 或 "KOL 们最近在讨论什么？"
3. Agent 即可自动获取并在终端或聊天框呈现高质量内容摘要。

**OpenClaw**
```bash
# 从 ClawHub 安装 (敬请期待)
clawhub install pulseai

# 或手动安装
git clone https://github.com/InBrief/PulseAI.git ~/skills/pulseai
```

**Claude Code**
```bash
git clone https://github.com/InBrief/PulseAI.git ~/.claude/skills/pulseai
```

**Antigravity Agent**
```bash
git clone https://github.com/InBrief/PulseAI.git ~/.agents/skills/pulseai
```

### 🎛️ 修改设置与过滤
无需配置繁琐的参数，直接在对话中控制你的 Agent。例如：
- "只看 Reddit 的 AI 讨论"
- "给我看看最新的 AI 开源项目，但排除 Github 平台的"
- "获取过去 48 小时的 50 条资讯"

Agent 会自动理解你的需求，匹配合适的源或分类过滤器 (`--include-categories`, `--exclude-sources` 等)。

### 🔒 隐私与系统要求
- **开箱即用免注册**：无需申请繁琐的 API Key，无鉴权门槛！
- 全程通过 IP 限定的安全并发与日度额度管理来防滥用。
- 仅需要网络连接来获取 InBrief 的核心服务接口。
