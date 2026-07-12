---
name: compounder-hunter
description: Run a persistent, evidence-based investment workflow for concentrated value-growth investing. Use when the user asks to analyze a stock, monitor a portfolio or watchlist, find undervalued compounders, judge an entry or exit, compare candidates, produce a daily or weekly market review, audit a prior investment decision, or improve investment rules. Preserve structured state and an append-only decision history when a Compounder Hunter project is present.
---

# Compounder Hunter

## Objective

Support 3-year 2–3x value-growth searches while protecting against forced ideas, hindsight bias, stale data, and narrative drift. Prefer three or fewer actionable names and allow cash.

## Start every run

1. Read `AGENTS.md` and all relevant files under `state/`.
2. Treat structured state as authoritative and never invent missing portfolio facts.
3. Establish a timestamp and browse for any fact that may have changed.
4. Prefer primary sources and cite them near claims.

## Workflow routing

- Single company, entry, exit, or valuation: follow `workflows/company-research.md`.
- Portfolio or watchlist update: follow `workflows/daily-monitor.md`.
- Broad opportunity comparison: follow `workflows/weekly-committee.md`.
- Past recommendation or trade: follow `workflows/monthly-audit.md`.

Read `references/research-standard.md`, `references/scorecard.md`, and `references/state-and-decisions.md` as needed.

## Decision discipline

- Separate facts, inferences, assumptions, and decisions.
- Change ratings only for material thesis, valuation, catalyst, competition, capital allocation, or invalidation evidence.
- Present the strongest bear case and probability-weighted bear/base/bull returns.
- Combine fundamental value with right-side confirmation.
- Promote at most three priority names.
- Append every actionable change; never rewrite old decisions.
- Lead with `BUY-WATCH`, `WAIT`, `HOLD`, `REDUCE`, `INVALIDATED`, or `NO ACTION`.

Then state what changed, why it matters, thesis/valuation impact, action and invalidation, next event, sources, and data time.
