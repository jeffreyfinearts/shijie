# AI PRD Kit

A local-first PRD and agent prompt quality toolkit for AI product teams.

It helps product managers, designers, founders, and AI-assisted development teams write clearer product specs, agent tasks, UI state matrices, and release boundaries — without sending private documents to any external API.

> 中文：这是一个面向 AI 产品团队的本地化 PRD / Agent 任务质量检查工具。它可以生成模板、检查需求文档中的模糊表述、版本边界混乱、UI 状态缺失、字段契约不完整和潜在隐私暴露。

## Why this project

AI teams are moving from simple prompt usage to agentic workflows. That makes product specs more important, not less important:

- Agents need precise boundaries.
- Engineers need field-level contracts.
- Designers need full UI state coverage.
- Founders need reusable delivery playbooks.
- Public examples must not leak private data.

AI PRD Kit gives teams a practical baseline before handing work to Codex, Claude Code, Cursor, Copilot Agent, or any internal agent workflow.

## Features

- **Template generator** for PRDs, agent tasks, UI state matrices, and release boundaries.
- **Local linting** for Markdown specs. No API key. No upload. No telemetry.
- **PRD scoring** from 0 to 100 for quick review gates.
- **Privacy checks** for emails, phone numbers, ID-like patterns, and sensitive placeholders.
- **Agent guardrail checks** for prompt/task handoff documents.
- **Bilingual templates**: English and Simplified Chinese.

## Quick start

```bash
npx ai-prd-kit init specs --lang=zh-CN
npx ai-prd-kit lint specs
npx ai-prd-kit score specs/prd-template.zh-CN.md
```

Local usage after cloning:

```bash
git clone https://github.com/jeffreyfinearts/shijie.git
cd shijie
npm test
node bin/ai-prd-kit.js lint examples/example-prd.zh-CN.md
```

## CLI

```bash
ai-prd-kit init [dir] [--lang=zh-CN|en]
ai-prd-kit lint <file-or-dir> [--json]
ai-prd-kit score <file-or-dir>
ai-prd-kit doctor
```

## Example report

```text
AI PRD Kit Report
=================
Files checked: 1
Score: 61/100
Findings: 5 (0 error, 4 warn, 1 info)

[WARN] PRD-002 Potentially vague requirement wording
Fix: Replace vague wording with explicit scope, trigger, state, owner, and boundary.
```

## What it checks

| Rule | Level | Purpose |
|---|---:|---|
| PRD-001 | error | Missing measurable acceptance criteria |
| PRD-002 | warn | Vague requirement wording |
| PRD-003 | warn | Mixed release boundary |
| PRD-004 | warn | Incomplete UI state coverage |
| PRD-005 | info | Incomplete API/data contract |
| PRD-006 | warn | Potential privacy exposure |
| PRD-007 | info | Missing metrics / event tracking |
| AGENT-001 | warn | Agent task lacks guardrails |

## Recommended workflow

1. Start with `ai-prd-kit init`.
2. Write your feature spec with explicit release boundary.
3. Add UI states and field contracts.
4. Run `ai-prd-kit lint` before handing work to an AI coding agent.
5. Fix error-level findings before implementation.
6. Publish only anonymized examples.

## Star-friendly roadmap

- [ ] Add configurable rule packs.
- [ ] Add GitHub Action for PRD review.
- [ ] Add VS Code snippets.
- [ ] Add JSON schema export for agent workflows.
- [ ] Add more AI-product examples: onboarding, notification center, agent cards, payments, permission states.
- [ ] Add English documentation site.

## Privacy promise

AI PRD Kit runs locally. It does not call LLM APIs, does not collect telemetry, and does not upload your documents.

## Contributing

Contributions are welcome. Good first issues:

- Add a new PRD rule.
- Improve bilingual templates.
- Add an anonymized product spec example.
- Add GitHub Actions integration.

## License

MIT
