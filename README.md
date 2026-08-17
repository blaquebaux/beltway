# Blaque Baux Beltway

**Democratic-era darlings — Biden, Barry, Bill — do the regime's winners still hold up?**

Beltway is a member of the Blaque Baux family. The [core repo](https://github.com/blaquebaux/base)
is the **engine and blueprint** — a governed, systematic platform (Julia) with a venue-agnostic
execution controller and a Layer-3 live-money safety gate. Beltway points that engine in its own
direction and inherits the governance wholesale.

> **Not investment advice.** Educational/research software. Nothing here is validated. See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/blaquebaux/beltway.git
julia --project=engine -e 'using Pkg; Pkg.instantiate()'   # one-time engine setup
```

## The thesis

A common claim: **Democratic administrations bring stable growth**, and each era mints its own set
of market darlings. Clinton (**Bill**) had the 1990s tech-and-telecom boom; Obama (**Barry**) had the
FANG ascent, biotech, and the first clean-energy wave; Biden had the IRA / infrastructure / green /
reshoring / AI-industrial complex. Beltway asks whether any of that is **a real, tradable conditioning
variable** — or hindsight and coincidence dressed as causation.

Two honest tests sit at the core. First, **is "same-party regime" actually informative** for those
era baskets, or does it vanish once you control for the Fed, the business cycle, and simple base
rates? (Presidents do not cause bull markets; this sleeve is built to *try to kill* the thesis, not to
flatter it.) Second, **do the darlings persist or mean-revert** — does a regime's winning basket keep
winning into the next administration, or is buying last era's darlings a reversion trap? The partisan
framing is the hypothesis; the README name (`beltway`) keeps the repo neutral.

## Research plan (Path A)

- **Define the eras and their darlings, ex-ante-style.** For each Democratic term, assemble the sector
  / thematic baskets that policy actually favored (documented at the time, to limit look-ahead).
- **Regime as a conditioning variable.** Test whether returns to those baskets differ under D vs. R
  control — then re-test controlling for rates, cycle, and market beta. Report what survives the
  controls, and say plainly if nothing does.
- **Persistence vs. reversion.** Do era darlings carry into the following administration, or fade?
  This is the tradable question even if "party causes growth" fails.
- **Confound audit.** Explicitly document the confounds (Fed cycle, valuations at inauguration,
  small sample of terms) so the result is not oversold. A null here is a perfectly good outcome.

## Research — first pass done

Full detail in [`research/README.md`](research/README.md). The scorecard (Alpaca SIP; **2016+ only —
Clinton & most of Obama are out of sample**):

| # | Question | Verdict |
|---|----------|---------|
| 1 | Are the party baskets even good? | ⚠️ high-beta sector bets — DEM +0.50 Sharpe / REP +0.65 / **SPY +0.88**; clean energy −67%, solar −79% DD |
| 2 | Is "same-party regime" informative? | ❌❌ **not null — inverted**: aligned basket loses under its own party 4/4; DEM darlings −14.8%/yr under D, +39.8%/yr under R |
| 3 | Policy, or just macro? | ❌ macro dominates — under Biden, clean energy −21%/yr while fossil +26%/yr (the opposite of the narrative) |
| 4 | Do the darlings persist or revert? | ❌ reversion trap — rank persistence Trump-I→Biden **−0.95**; TAN went +61% winner → −26% dead-last |

**The synthesis:** the thesis doesn't just fail — in the testable window it runs **backwards**. If
"Democratic policy lifts the Democratic darlings" held, clean energy would shine under Biden and fossil
under Trump; instead the party-aligned basket **lost in all four administrations**, and pooled the
Democratic darlings returned **−14.8%/yr under Democrats vs +39.8%/yr under Republicans**. The reason
is macro, not politics: the long-duration clean-energy complex was inflated by 2020 ZIRP (late Trump)
and crushed by the 2022 rate shock (Biden), while the oil shock sent fossil energy soaring *under the
Democrat*. And the darlings **revert** (Trump-I→Biden rank persistence −0.95) — buying last regime's
winners is precisely wrong. Caveats keep it modest (only ~3–4 terms, marquee eras pre-2016, a
rate-regime artifact more than a political law), but within everything the data can see, **party regime
is macro in a partisan costume, not a tradable signal.** Joins the honest shelf with
[Bubble](https://github.com/blaquebaux/bubble) and [Burry](https://github.com/blaquebaux/burry).

## Status
**Research: first pass complete — an emphatic null (indeed inverted)** (`research/`). Party regime does
not drive the darlings; macro does, and the darlings revert. Marquee eras out of sample. No keeper, no
live driver; nothing validated to the spine's bar.

## About Blaque Baux

**Blaque Baux** is a quantitative research initiative and a subsidiary of **[Carter Warrens](https://carterwarrens.com)**.
[**BlaqueBaux.com**](https://blaquebaux.com) is the home for the work; the code lives here on GitHub — open to
study, test, and build bespoke strategies on top of.

Anyone can point an AI at a market. The edge is **understanding what the data actually says — and turning it
into something you can act on.** We test relentlessly and put most of it *on the record as rejected, with the
reason*; what survives is built, governed, and validated before it is ever called real. That combination —
honest research, reproducible evidence, and execution you can trust — is why Carter Warrens leads on
**strategy and implementation**, not merely uses the tools everyone now has.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/blaquebaux/base) is the
base/blueprint and holds the [full family roster](https://github.com/blaquebaux/base#the-blaquebaux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule -> blaquebaux/base)
research/   four Path-A sketches (baskets, regime, controls, persistence) + scorecard
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
