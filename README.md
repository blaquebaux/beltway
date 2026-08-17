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

## Research plan (Path A — not yet built)

- **Define the eras and their darlings, ex-ante-style.** For each Democratic term, assemble the sector
  / thematic baskets that policy actually favored (documented at the time, to limit look-ahead).
- **Regime as a conditioning variable.** Test whether returns to those baskets differ under D vs. R
  control — then re-test controlling for rates, cycle, and market beta. Report what survives the
  controls, and say plainly if nothing does.
- **Persistence vs. reversion.** Do era darlings carry into the following administration, or fade?
  This is the tradable question even if "party causes growth" fails.
- **Confound audit.** Explicitly document the confounds (Fed cycle, valuations at inauguration,
  small sample of terms) so the result is not oversold. A null here is a perfectly good outcome.

Nothing above is implemented or validated. This is the map, not the territory.

## Status
**Concept.** Thesis and research plan only — no sketches run, no driver, nothing validated to the
spine's bar. A politically-flavored hypothesis, to be tested skeptically like everything else here.

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
research/   the research plan (Path A) — sketches land here once run
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
