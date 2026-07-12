# Compounder Hunter OS

A persistent investment decision agent for monitoring markets, researching compounders, tracking a concentrated watchlist, preserving an auditable decision history, and improving its rules through scheduled reviews.

## What this project is

- `AGENTS.md` defines the agent's durable behavior.
- `state/` is the authoritative memory for portfolio facts, theses, decisions, and strategy versions.
- `workflows/` defines repeatable daily, weekly, monthly, and company-research runs.
- `reports/` stores dated outputs.
- `skills/compounder-hunter/` contains the reusable analysis skill.
- `scripts/validate_state.py` checks that the persistent state remains structurally valid.

## First conversation

Ask the agent: `读取项目状态，告诉我还缺哪些初始化数据，并生成今天的投资驾驶舱。`

Unknown financial facts are deliberately recorded as `needs_user_input`; they are never guessed.
