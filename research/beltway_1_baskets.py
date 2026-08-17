#!/usr/bin/python3
# =============================================================================
# beltway_1_baskets.py — BLAQUE BAUX BELTWAY #1: the party-favoured baskets.
#
# Before any regime test: build the policy-associated baskets as tradable ETFs and
# profile them over the full window. This establishes what "Democratic darlings" and
# "Republican darlings" mean in numbers — and states plainly what the data cannot see
# (Clinton, most of Obama: pre-2016, out of sample).
# Read-only. Prints its own results.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _beltway_common import panel, stats, capm, DEM, REP, MKT

u, dates, M = panel(DEM + REP + [MKT]); j = {s: u.index(s) for s in u}
R = M[1:] / M[:-1] - 1
print("=" * 80, "\nBELTWAY #1 — the party-favoured baskets (2016-2026; pre-2016 out of sample)\n" + "=" * 80)
print(f"  {dates[0]} .. {dates[-1]}\n")
mkt = R[:, j[MKT]]
def line(lbl, r):
    st = stats(r); a, b = capm(r, mkt)
    print(f"  {lbl:<28}{st['sh']:>+8.2f}{st['cagr']*100:>+7.1f}%{st['vol']*100:>6.1f}%{st['dd']*100:>+7.0f}%{a*100:>+7.1f}%{b:>+6.2f}")

print(f"  {'component':<28}{'Sharpe':>8}{'CAGR':>8}{'vol':>7}{'maxDD':>8}{'alpha':>8}{'beta':>6}")
print("  Democratic-favoured:")
for s in DEM: line(f"    {s}", R[:, j[s]])
print("  Republican-favoured:")
for s in REP: line(f"    {s}", R[:, j[s]])
print("  " + "-" * 64)
dem = R[:, [j[s] for s in DEM]].mean(axis=1)
rep = R[:, [j[s] for s in REP]].mean(axis=1)
line("DEM basket (equal-wt)", dem)
line("REP basket (equal-wt)", rep)
line("SPY (the market)", mkt)

print("\nVERDICT: both baskets are high-beta sector bets, not free money — the Democratic basket in")
print("particular is a volatile, drawdown-prone clean-energy/biotech book. Whether the PARTY IN")
print("POWER is what drives them (vs the Fed, the cycle, the oil price) is the real question — #2.")
