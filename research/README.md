# Blaque Baux Beltway — research

First-pass Path-A research on the **"Democratic policy → stable growth in the darlings"** thesis. All
sketches read Alpaca SIP daily bars, are read-only, and print their own results.

> **Hard data limit, stated up front.** Alpaca history begins **2016** — so **Clinton (1993–2001) and
> nearly all of Obama (2009–2017), the thesis's marquee eras, are out of sample.** What the data can
> test is one clean natural experiment: **Trump-I (R), Biden (D), Trump-II (R)** plus a one-year
> Obama-II tail — a handful of terms, dominated by COVID, the 2022 rate shock, and the AI boom. A null
> is the expected, honest outcome. It was built to *try to kill* the thesis, not flatter it.

```bash
export $(grep -v '^#' ~/.config/blaquebaux/alpaca.env | xargs)   # or source it
python research/beltway_1_baskets.py       # the party-favoured baskets, profiled
python research/beltway_2_regime.py        # does the aligned basket win under its own party?
python research/beltway_3_controls.py      # policy, or just macro?  (the inversion)
python research/beltway_4_persistence.py   # do the darlings persist, or revert?
```

## Scorecard

| # | Question | Result | Verdict |
|---|----------|--------|---------|
| 1 | Are the party baskets even good? | DEM basket +0.50 Sharpe / REP +0.65 / **SPY +0.88**; both high-beta, drawdown-prone (clean energy −67%, solar −79%) | ⚠️ high-beta sector bets, not free money |
| 2 | Is "same-party regime" informative? | the party-aligned basket **loses under its own party in 4/4 admins**; pooled, DEM darlings **−14.8%/yr under D** but **+39.8%/yr under R** | ❌❌ **not null — inverted** |
| 3 | Policy, or just macro? | under Biden (D): clean energy ICLN **−21%/yr**, fossil XLE **+26%/yr**; the exact opposite of the narrative | ❌ **macro dominates** (rates, oil) |
| 4 | Do the darlings persist or revert? | rank persistence Trump-I→Biden **−0.95**; TAN went winner (+61%) → dead-last (−26%) | ❌ **reversion trap** |

## The synthesis

**The thesis does not merely fail to hold — in the testable window it runs backwards.** This is one of
the more emphatic entries on the honest shelf.

Start with the natural experiment. If "Democratic policy lifts the Democratic darlings" were true, the
clean-energy / EV / biotech basket would shine under Biden and the fossil / defense / banks basket
under Trump. Instead the **party-aligned basket lost to the rival basket in all four administrations
(0/4)**. Pooled, it is a clean inversion: the **Democratic darlings returned −14.8%/yr under
Democratic administrations and +39.8%/yr under Republican ones.** The signature case is the tell —
under Biden, the IRA president, **clean energy (ICLN) fell −21%/yr while fossil energy (XLE) rose
+26%/yr.** Solar under Trump-I: **+61%/yr**; solar under Biden: **−26%/yr**.

The reason is #3: **the party in power did not drive the darlings — the Fed and the cycle did.** The
clean-energy/biotech complex is long-duration; the 2020 ZIRP/COVID melt-up (late Trump) inflated it and
the 2022 rate shock (Biden) crushed it, while the 2022 oil shock sent "Republican" fossil energy
soaring *under the Democrat*. Policy is a slow, diffuse, already-priced-in tailwind; rates and the
business cycle set the returns. And #4 closes it: **darlings revert, they do not persist** — rank
persistence from Trump-I to Biden was **−0.95** (a near-perfect flip), and TAN went from the best sleeve
(+61%/yr) to the worst (−26%/yr). "Buy the last regime's winners" is precisely the wrong trade.

**The honest caveats keep it modest, not less clear.** Only ~3–4 terms sit in-sample, the marquee eras
(Clinton, Obama) are pre-2016, and the "inversion" is really a *rate-regime timing artifact*, not a
causal political law — with n≈3 terms even the reversion is a whisper. But within everything the data
can see, **political-party regime is not a tradable signal**; it is macro (rates, oil, cycle) wearing a
partisan costume, and chasing last-era darlings is a reversion trap.

## Status
**Research: first pass complete — an emphatic null (indeed inverted)** (`research/`). Party regime does
not drive the darlings; macro does, and the darlings revert. Marquee eras are out of sample. No keeper,
no live driver; nothing validated to the spine's bar — a clean lesson for the graveyard.
