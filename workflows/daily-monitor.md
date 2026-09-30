# Daily market and watchlist monitor

Run after A-share and Hong Kong close. Use current, directly sourced information.

1. Read authoritative project state.
2. **Run the Liquidity Regime Gate first.** Classify the U.S. market as `GREEN`, `YELLOW`, or `RED` using:
   - high-yield OAS and CCC spreads, including speed of change;
   - 2Y/10Y Treasury yields and real yields;
   - bank reserves, TGA, reverse repo, and funding/repo stress;
   - SPY/QQQ trend, equal-weight vs cap-weight, small caps, financials, and percentage above 50D/200D;
   - financing conditions, refinancing risk, equity issuance, and external-capital dependence;
   - index -> sector -> stock relative strength and 50D/200D structure.
3. **Apply the regime action before stock selection.**
   - `GREEN`: normal risk budget and normal tranche progression.
   - `YELLOW`: only strongest sectors/stocks qualify; require positive relative strength and operating evidence; first tranche at most 1/4-1/3 of intended full position; add only after positive feedback.
   - `RED`: no new high-beta equity risk; prefer cash/short-duration government securities until credit/liquidity stress stabilizes and right-side confirmation returns.
4. Check index regime, rates, FX, commodities, sector breadth, and relevant overseas leads.
5. **Run Sector Heat.** Compare major U.S. sectors and relevant themes on 1M/3M/6M relative performance vs SPY/QQQ, 50D/200D trend, breadth, earnings revisions, and volume. A weak sector cannot promote a stock to core risk solely because valuation looks cheap.
6. Check each priority and secondary name for price/volume, filings, earnings, guidance, policy, competitors, consensus revisions, insider selling, dilution, and capital allocation.
7. Compare only against the last recorded view. Classify every change as `noise`, `monitor`, `thesis-positive`, `thesis-negative`, or `invalidation`.
8. Test recorded price, evidence, technical, relative-strength, capital-allocation, and invalidation triggers.
9. Search for at most three genuinely new candidates only when a material industry or company signal appears.
10. Write `reports/daily/YYYY-MM-DD.md` using `reports/templates/daily.md`.
11. Update state only for verified, material changes. Append decisions; never overwrite history.

Daily output must begin with:
- `Liquidity Regime: GREEN / YELLOW / RED`
- `Sector Heat: top 3 improving / top 3 deteriorating`
- `Risk Action: add risk / selective risk / no new risk`

If nothing material changed, return `NO ACTION` and a short explanation.
