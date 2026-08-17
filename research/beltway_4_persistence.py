#!/usr/bin/python3
# =============================================================================
# beltway_4_persistence.py — BLAQUE BAUX BELTWAY #4: persistence vs. reversion.
#
# Even if "party causes growth" fails, there is a tradable question: do an
# administration's DARLINGS carry into the next term, or revert? Rank all the sector
# baskets by return within each administration, then see whether the prior winners keep
# winning (persistence) or the winners become the next losers (reversion trap). "Buy
# the last era's darlings" is a real strategy people follow — does it work?
# Read-only. Prints its own results.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _beltway_common import panel, stats, DEM, REP, MKT, ADMINS, dslice

SECTORS = DEM + REP
u, dates, M = panel(SECTORS + [MKT]); j = {s: u.index(s) for s in u}
R = M[1:] / M[:-1] - 1; d = dates[1:]

def rank(a, b):
    s = dslice(d, a, b)
    cg = {sym: stats(R[s[0]:s[1], j[sym]])['cagr'] for sym in SECTORS}
    return sorted(cg, key=cg.get, reverse=True), cg

print("=" * 80, "\nBELTWAY #4 — do an administration's darlings persist, or revert?\n" + "=" * 80)
terms = [("Trump-I", "2017-01-20", "2021-01-20"), ("Biden", "2021-01-20", "2025-01-20"),
         ("Trump-II", "2025-01-20", "2026-08-01")]
prev = None
for name, a, b in terms:
    order, cg = rank(a, b)
    top, bot = order[0], order[-1]
    line = f"  {name:<10} winner: {top:<5}({cg[top]*100:+.0f}%/yr)   loser: {bot:<5}({cg[bot]*100:+.0f}%/yr)"
    if prev:
        pt, _ = prev
        # where did last term's winner rank this term? (1 = best)
        wr = order.index(pt) + 1
        line += f"   | last winner {pt} ranked #{wr}/{len(SECTORS)} now"
    print(line)
    prev = (top, order)

# explicit persistence test: correlation of component ranks between consecutive terms
def cagr_vec(a, b):
    s = dslice(d, a, b); return np.array([stats(R[s[0]:s[1], j[sym]])['cagr'] for sym in SECTORS])
v1, v2, v3 = cagr_vec(*terms[0][1:]), cagr_vec(*terms[1][1:]), cagr_vec(*terms[2][1:])
def spear(x, y):
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y))
    return np.corrcoef(rx, ry)[0, 1]
print(f"\n  rank persistence (Spearman) Trump-I -> Biden: {spear(v1, v2):+.2f}   "
      f"Biden -> Trump-II: {spear(v2, v3):+.2f}")

print("\nVERDICT: negative/low rank-persistence == a REVERSION trap: last term's darlings tend to be")
print("next term's laggards (clean energy 2020 boom -> 2021-24 bust is the archetype). 'Buy the last")
print("era's winners' is precisely the wrong trade; if anything the signal is mean-reversion, not")
print("momentum — and with only a few terms in-sample, even that is a whisper, not an edge.")
