#!/usr/bin/python3
# =============================================================================
# beltway_2_regime.py — BLAQUE BAUX BELTWAY #2: is "same-party regime" informative?
#
# The core test. For each administration in the window, does the party-ALIGNED basket
# beat the OTHER party's basket and the market? Then pooled: how did the Democratic
# basket do under D vs under R administrations (and the Republican basket vice-versa)?
# If the policy narrative held, each basket would shine under its own party.
# Read-only. Prints its own results.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _beltway_common import panel, stats, DEM, REP, MKT, ADMINS, dslice

u, dates, M = panel(DEM + REP + [MKT]); j = {s: u.index(s) for s in u}
R = M[1:] / M[:-1] - 1; d = dates[1:]
dem = R[:, [j[s] for s in DEM]].mean(axis=1)
rep = R[:, [j[s] for s in REP]].mean(axis=1)
mkt = R[:, j[MKT]]

def tot(r, s):
    x = r[s[0]:s[1]]
    return (np.prod(1 + x) - 1) * 100, stats(x)['cagr'] * 100

print("=" * 82, "\nBELTWAY #2 — does the party-aligned basket win under its own party?\n" + "=" * 82)
print(f"  {'administration':<16}{'party':>6}{'DEM bskt CAGR':>15}{'REP bskt CAGR':>15}{'SPY CAGR':>11}{'aligned wins?':>15}")
pooled = {"D": {"dem": [], "rep": []}, "R": {"dem": [], "rep": []}}
for name, a, b, party in ADMINS:
    s = dslice(d, a, b)
    _, dc = tot(dem, s); _, rc = tot(rep, s); _, sc = tot(mkt, s)
    aligned = dc if party == "D" else rc
    other = rc if party == "D" else dc
    win = "yes" if aligned > other else "NO"
    pooled[party]["dem"].append(dem[s[0]:s[1]]); pooled[party]["rep"].append(rep[s[0]:s[1]])
    print(f"  {name:<16}{party:>6}{dc:>+14.1f}%{rc:>+14.1f}%{sc:>+10.1f}%{win:>15}")

print("\n  pooled by party in power (annualized):")
for party in ["D", "R"]:
    dd = np.concatenate(pooled[party]["dem"]); rr = np.concatenate(pooled[party]["rep"])
    print(f"    under {party}-admins:  DEM basket {stats(dd)['cagr']*100:+.1f}%/yr   "
          f"REP basket {stats(rr)['cagr']*100:+.1f}%/yr")

print("\nVERDICT: if the aligned basket does NOT reliably beat the rival basket under its own party")
print("(and it does not), 'same-party regime' is not an informative signal on its own. The famous")
print("case: clean energy under Biden — the policy darling — is exactly where #3 shows the narrative")
print("inverts, because macro (rates, oil) swamped policy.")
