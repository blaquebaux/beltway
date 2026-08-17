#!/usr/bin/python3
# =============================================================================
# _beltway_common.py — shared helpers for the Blaque Baux Beltway sketches.
# Alpaca SIP daily bars; reads ALPACA_KEY_ID / ALPACA_SECRET_KEY from env. Read-only.
#
# HARD DATA LIMIT, stated up front: Alpaca history begins 2016-01. Clinton (1993-2001)
# and nearly all of Obama (2009-2017) are therefore UNTESTABLE here — the thesis's
# marquee eras are out of sample. What the data *can* test is one clean natural
# experiment: Trump-I (R), Biden (D), Trump-II (R), plus a one-year Obama-II tail. That
# is a handful of terms, dominated by COVID, the 2022 rate shock, and the AI boom — so
# a NULL is the expected, honest outcome, not a disappointment.
#
# Party-favoured baskets (policy-associated, tradable, full 2016 history):
#   Democratic: ICLN clean-energy, TAN solar, LIT battery/EV, XBI biotech(ACA)
#   Republican: XLE fossil energy, ITA defense, KBE banks(deregulation), IWM small-cap(tax)
# =============================================================================
import os, json, urllib.request, math
import numpy as np

H = {"APCA-API-KEY-ID": os.environ["ALPACA_KEY_ID"], "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
START, END = "2016-01-01", "2026-08-01"
_cache = {}

DEM = ["ICLN", "TAN", "LIT", "XBI"]        # clean energy / solar / battery-EV / biotech
REP = ["XLE", "ITA", "KBE", "IWM"]         # fossil energy / defense / banks / small-cap
MKT = "SPY"

# administrations inside the data window (inauguration ~Jan 20). party: D / R
ADMINS = [
    ("Obama-II tail", "2016-01-04", "2017-01-20", "D"),
    ("Trump-I",       "2017-01-20", "2021-01-20", "R"),
    ("Biden",         "2021-01-20", "2025-01-20", "D"),
    ("Trump-II",      "2025-01-20", "2026-08-01", "R"),
]

def bars(s):
    if s in _cache: return _cache[s]
    u = (f"https://data.alpaca.markets/v2/stocks/bars?symbols={s}&timeframe=1Day"
         f"&start={START}&end={END}&adjustment=all&feed=sip&limit=10000")
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=40))
        _cache[s] = {b["t"][:10]: b for b in d.get("bars", {}).get(s, [])}
    except Exception:
        _cache[s] = {}
    return _cache[s]

def panel(syms):
    D = {s: bars(s) for s in syms}; D = {s: v for s, v in D.items() if len(v) > 250}
    u = list(D); dates = sorted(set.intersection(*[set(D[s]) for s in u]))
    M = np.array([[D[s][d]["c"] for s in u] for d in dates], float)
    return u, dates, M

def stats(r):
    r = np.asarray(r, float); r = r[np.isfinite(r)]
    if len(r) < 20 or r.std() == 0: return dict(sh=float('nan'), cagr=float('nan'), dd=float('nan'), vol=float('nan'))
    cum = np.cumprod(1 + r)
    return dict(sh=r.mean() / r.std() * math.sqrt(252), cagr=cum[-1] ** (252 / len(r)) - 1,
                dd=(cum / np.maximum.accumulate(cum) - 1).min(), vol=r.std() * math.sqrt(252))

def capm(y, x):
    y = np.asarray(y, float); x = np.asarray(x, float)
    m = np.isfinite(y) & np.isfinite(x); y, x = y[m], x[m]
    if len(y) < 20 or np.var(x) == 0: return float('nan'), float('nan')
    b = np.cov(y, x)[0, 1] / np.var(x)
    return (y.mean() - b * x.mean()) * 252, b

def dslice(dates, a, b):
    lo = next((i for i, x in enumerate(dates) if x >= a), 0)
    hi = next((i for i, x in enumerate(dates) if x >= b), len(dates))
    return lo, hi
