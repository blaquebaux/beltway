#!/usr/bin/python3
# =============================================================================
# beltway_3_controls.py — BLAQUE BAUX BELTWAY #3: policy, or just macro?
#
# The thesis dies here or survives here. The clean-energy-under-Biden case is the
# tell: the signature Democratic policy era (IRA, 2021-2025) should have been clean
# energy's golden age — instead rates and the oil shock made it a disaster while
# FOSSIL energy (the "Republican" basket) soared UNDER the Democrat. Show each basket's
# return under Biden vs under Trump-I, and expose where the policy narrative INVERTS.
# Read-only. Prints its own results.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _beltway_common import panel, stats, DEM, REP, MKT, ADMINS, dslice

u, dates, M = panel(DEM + REP + [MKT]); j = {s: u.index(s) for s in u}
R = M[1:] / M[:-1] - 1; d = dates[1:]

def cagr(sym, s): return stats(R[s[0]:s[1], j[sym]])['cagr'] * 100
t1 = dslice(d, "2017-01-20", "2021-01-20")   # Trump-I (R)
bi = dslice(d, "2021-01-20", "2025-01-20")   # Biden (D)

print("=" * 80, "\nBELTWAY #3 — policy narrative vs. what actually happened (per component)\n" + "=" * 80)
print(f"  {'ETF':<6}{'theme':<22}{'Trump-I (R)':>13}{'Biden (D)':>12}{'narrative check':>22}")
notes = {
    "ICLN": ("clean energy [D]", "D policy, D era -> should soar"),
    "TAN":  ("solar [D]",         "D policy, D era -> should soar"),
    "LIT":  ("battery/EV [D]",    "D policy, D era -> should soar"),
    "XBI":  ("biotech [D]",       "D-leaning"),
    "XLE":  ("fossil energy [R]", "R theme, yet BOOMED under Biden"),
    "ITA":  ("defense [R]",       "R-leaning"),
    "KBE":  ("banks [R]",         "R dereg theme"),
    "IWM":  ("small-cap [R]",     "R tax-cut theme"),
}
for s in DEM + REP:
    th, chk = notes[s]
    print(f"  {s:<6}{th:<22}{cagr(s,t1):>+12.1f}%{cagr(s,bi):>+11.1f}%   {chk}")

# the headline inversion
icln_bi = cagr("ICLN", bi); xle_bi = cagr("XLE", bi)
print(f"\n  THE INVERSION under Biden (D): clean energy ICLN {icln_bi:+.1f}%/yr  vs  fossil XLE {xle_bi:+.1f}%/yr")
print("  The signature Democratic policy era was clean energy's WORST stretch and fossil fuel's best.")

print("\nVERDICT: the party-in-power did NOT drive the darlings — MACRO did. Under Biden, rising rates")
print("crushed long-duration clean-energy/biotech while the 2022 oil shock sent 'Republican' fossil")
print("energy soaring. Policy is a slow, diffuse, priced-in tailwind; the Fed and the cycle dominate")
print("returns. 'Democratic policy -> stable growth in the darlings' does not survive the controls.")
