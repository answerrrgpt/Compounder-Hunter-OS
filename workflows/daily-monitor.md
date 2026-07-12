# Daily market and watchlist monitor

Run after A-share and Hong Kong close. Use current, directly sourced information.

1. Read authoritative project state.
2. Check index regime, rates, FX, commodities, sector breadth, and relevant overseas leads.
3. Check each priority and secondary name for price/volume, filings, earnings, guidance, policy, competitors, and consensus revisions.
4. Compare only against the last recorded view. Classify every change as `noise`, `monitor`, `thesis-positive`, `thesis-negative`, or `invalidation`.
5. Test recorded price, evidence, technical, and invalidation triggers.
6. Search for at most three genuinely new candidates only when a material industry or company signal appears.
7. Write `reports/daily/YYYY-MM-DD.md` using `reports/templates/daily.md`.
8. Update state only for verified, material changes. Append decisions; never overwrite history.

If nothing material changed, return `NO ACTION` and a short explanation.
