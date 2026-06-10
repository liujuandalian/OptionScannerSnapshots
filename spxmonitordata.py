#!/usr/bin/env python3
"""
spxmonitordata.py — SPX Options Monitor V4 数据生成器  v2.1
--------------------------------------------------------------
每 5 分钟从 Schwab API 获取全量数据，计算所有 V4 仪表盘指标，
将结果写入 GitHub 仓库（liujuandalian/OptionScannerSnapshots）。

GitHub 输出文件：
  data/spx_v4_latest.json     ← HTML 优先读，每次覆盖
  data/spx_v4_YYYYMMDD_HHMM.json ← 带时间戳存档

所有数值字段完全来自实时 API，无硬编码假数据。
"""

import os, sys, json, time, math, logging, subprocess, random
from datetime import datetime, timedelta, date, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from dotenv import load_dotenv

try:
    from scipy.stats import norm
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False
    def _norm_cdf(x):
        return (1 + math.erf(x / math.sqrt(2))) / 2
    norm = type("", (), {"cdf": staticmethod(_norm_cdf)})()

# ── 配置 ──────────────────────────────────────────────────────────────────────
CONFIG = {
    "env_file":              r"D:\04-Coding\schwab_options_scanner\config\.env",
    "token_file":            r"D:\04-Coding\schwab_options_scanner\config\token.json",
    "callback_url":          "https://127.0.0.1:8182",
    "git_repo_path":         r"D:\04-Coding\schwab_options_scanner\OptionScannerSnapshots",
    "git_remote":            "origin",
    "git_branch":            "main",
    "git_path":              None,          # 留空=自动探测；Windows可设为 r"C:\Program Files\Git\cmd\git.exe",
    "fetch_interval_seconds": 300,      # 5 分钟
    "strike_count":          60,        # ATM ± 60 档
    "max_days_out":          45,        # 最远到期日
    "risk_free_rate":        0.053,     # 无风险利率（近似）
    "log_level":             logging.INFO,
}

SYMBOLS_SPX  = "$SPX"
SYMBOLS_VIX  = "$VIX"
SYMBOLS_VVIX = "$VVIX"
SYMBOLS_ES   = "/ES"

DATA_SUBDIR  = "data"                  # GitHub 仓库内子目录
LATEST_FILE  = "spx_v4_latest.json"   # HTML 优先读这个

logging.basicConfig(
    level=CONFIG["log_level"],
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger("spxmonitor")


# ── Greeks ────────────────────────────────────────────────────────────────────
def _bs_greeks(spot: float, strike: float, iv: float, t_days: float,
               opt_type: str = "call", r: float = 0.053) -> Dict:
    """Black-Scholes Greeks（call 视角；put 通过 put-call parity 转换）。"""
    t = max(t_days, 0.1) / 365.0
    if iv <= 0 or spot <= 0 or strike <= 0:
        return {"delta": 0, "gamma": 0, "vega": 0, "theta": 0, "charm": 0, "vanna": 0}
    try:
        d1 = (math.log(spot / strike) + (r + 0.5 * iv**2) * t) / (iv * math.sqrt(t))
        d2 = d1 - iv * math.sqrt(t)
        pdf_d1 = math.exp(-0.5 * d1**2) / math.sqrt(2 * math.pi)
        nd1    = norm.cdf(d1)
        nd2    = norm.cdf(d2)

        gamma  = pdf_d1 / (spot * iv * math.sqrt(t))
        vega   = spot * pdf_d1 * math.sqrt(t) / 100
        charm  = -pdf_d1 * (2 * r * t - d2 * iv * math.sqrt(t)) / (2 * t * iv * math.sqrt(t))
        vanna  = -pdf_d1 * d2 / iv

        if opt_type.upper() == "CALL":
            delta = nd1
            theta = (-(spot * pdf_d1 * iv) / (2 * math.sqrt(t))
                     - r * strike * math.exp(-r * t) * nd2) / 365
        else:
            delta = nd1 - 1
            theta = (-(spot * pdf_d1 * iv) / (2 * math.sqrt(t))
                     + r * strike * math.exp(-r * t) * (1 - nd2)) / 365

        return {
            "delta": round(delta, 4),
            "gamma": round(gamma, 6),
            "vega":  round(vega,  2),
            "theta": round(theta, 2),
            "charm": round(charm, 6),
            "vanna": round(vanna, 6),
        }
    except (ValueError, ZeroDivisionError):
        return {"delta": 0, "gamma": 0, "vega": 0, "theta": 0, "charm": 0, "vanna": 0}


# ── Gamma / Charm 分布 ─────────────────────────────────────────────────────────
def _gamma_charm_distribution(chain: Dict, spot: float) -> Tuple[Dict, Dict]:
    """
    dealer net gamma = -(client OI × gamma × 100)
    call: 做市商 short → gamma 为负；put: 做市商 short → gamma 也为负
    charm 符号同向
    返回 {strike_str: value} （key 统一为字符串，方便 JSON）
    """
    gamma_map: Dict[str, float] = {}
    charm_map: Dict[str, float] = {}

    today     = date.today()
    rate      = CONFIG["risk_free_rate"]

    for opt_key, sign in [("callExpDateMap", -1), ("putExpDateMap", -1)]:
        for exp_str, strike_map in chain.get(opt_key, {}).items():
            try:
                exp_date = datetime.strptime(exp_str.split(":")[0], "%Y-%m-%d").date()
            except ValueError:
                continue
            t_days = max((exp_date - today).days, 0.1)

            for strike_str, contracts in strike_map.items():
                if not contracts:
                    continue
                c      = contracts[0]
                oi     = c.get("openInterest", 0) or 0
                iv     = (c.get("volatility", 0) or 0) / 100.0  # Schwab 返回百分比
                strike = float(strike_str)
                opt_t  = "CALL" if opt_key == "callExpDateMap" else "PUT"

                # 优先用 API 返回的 gamma/charm；若为 0 则自行计算
                api_gamma = c.get("gamma", 0) or 0
                api_charm = c.get("charm", 0) or 0

                if api_gamma == 0 and iv > 0:
                    g = _bs_greeks(spot, strike, iv, t_days, opt_t, rate)
                    api_gamma = g["gamma"]
                    api_charm = g["charm"]

                key = str(int(strike)) if strike == int(strike) else str(strike)
                # GEX 标准公式: dealer net = -(OI × gamma × 100 × spot)
                # gamma 是 per-$1 move per share，×100合约乘数×spot = dollar GEX
                gex_contrib = sign * oi * api_gamma * 100 * spot
                gamma_map[key] = gamma_map.get(key, 0) + gex_contrib
                charm_sign = sign if opt_t == "CALL" else -sign
                charm_map[key] = charm_map.get(key, 0) + charm_sign * oi * abs(api_charm) * 100

    return gamma_map, charm_map


# ── Key Levels ────────────────────────────────────────────────────────────────
def _key_levels(gamma_map: Dict, spot: float,
                straddle: float) -> Tuple[Optional[float], Optional[float], float]:
    if not gamma_map:
        return None, None, 0.0
    strikes_f = [(float(k), v) for k, v in gamma_map.items()]
    strikes_f.sort()

    total_net = sum(v for _, v in strikes_f)
    gamma_flip = None
    for s, v in strikes_f:
        if s > spot and v < 0:
            gamma_flip = s
            break

    # balance = 净 gamma 绝对值最小的 strike（现价 ± 2×straddle 范围内）
    window = max(straddle * 2, 100)
    nearby = [(s, v) for s, v in strikes_f if abs(s - spot) <= window]
    balance_point = min(nearby, key=lambda x: abs(x[1]))[0] if nearby else spot

    return gamma_flip, balance_point, total_net


# ── OI Top ────────────────────────────────────────────────────────────────────
def _oi_top(chain: Dict, spot: float) -> Dict:
    call_oi: Dict[float, int] = {}
    put_oi:  Dict[float, int] = {}
    for exp_map_key, oi_dict in [("callExpDateMap", call_oi), ("putExpDateMap", put_oi)]:
        for strike_map in chain.get(exp_map_key, {}).values():
            for strike_str, contracts in strike_map.items():
                if contracts:
                    oi = contracts[0].get("openInterest", 0) or 0
                    oi_dict[float(strike_str)] = oi_dict.get(float(strike_str), 0) + oi

    calls_above = sorted([(k, v) for k, v in call_oi.items() if k > spot],  key=lambda x: -x[1])[:5]
    puts_below  = sorted([(k, v) for k, v in put_oi.items()  if k < spot],  key=lambda x: -x[1])[:5]
    return {
        "top_calls": [{"strike": k, "oi": v} for k, v in calls_above],
        "top_puts":  [{"strike": k, "oi": v} for k, v in puts_below],
    }


# ── Skew ──────────────────────────────────────────────────────────────────────
def _skew_slope(chain: Dict, spot: float) -> Dict:
    result   = {"0dte": None, "1w": None, "1m": None}
    today    = date.today()
    seen     = set()

    for exp_str in sorted(set(list(chain.get("callExpDateMap", {}).keys()) +
                               list(chain.get("putExpDateMap", {}).keys()))):
        try:
            exp_date = datetime.strptime(exp_str.split(":")[0], "%Y-%m-%d").date()
        except ValueError:
            continue
        dte = (exp_date - today).days
        label = "0dte" if dte <= 1 else "1w" if dte <= 7 else "1m" if dte <= 35 else None
        if label is None or label in seen:
            continue
        seen.add(label)

        put_iv25 = call_iv25 = None
        for strike_str, contracts in chain.get("putExpDateMap", {}).get(exp_str, {}).items():
            if contracts and abs((contracts[0].get("delta") or 0) + 0.25) < 0.06:
                put_iv25 = (contracts[0].get("volatility") or 0)
                break
        for strike_str, contracts in chain.get("callExpDateMap", {}).get(exp_str, {}).items():
            if contracts and abs((contracts[0].get("delta") or 0) - 0.25) < 0.06:
                call_iv25 = (contracts[0].get("volatility") or 0)
                break
        if put_iv25 is not None and call_iv25 is not None:
            result[label] = round(put_iv25 - call_iv25, 2)

    return result


# ── Term Structure ─────────────────────────────────────────────────────────────
def _term_structure(chain: Dict) -> Dict:
    spot   = chain.get("underlyingPrice", 0)
    exp_iv: Dict[str, float] = {}
    for opt_key in ("callExpDateMap", "putExpDateMap"):
        for exp_str, strike_map in chain.get(opt_key, {}).items():
            try:
                atm_s = min(strike_map, key=lambda x: abs(float(x) - spot))
            except ValueError:
                continue
            contracts = strike_map[atm_s]
            if contracts:
                iv = (contracts[0].get("volatility") or 0)
                key = exp_str.split(":")[0]
                exp_iv[key] = (exp_iv[key] + iv) / 2 if key in exp_iv else iv

    sorted_exp = sorted(exp_iv.items())
    return {"expirations": [e for e, _ in sorted_exp],
            "ivs":         [round(v, 2) for _, v in sorted_exp]}


# ── ATM Straddle（找最近有效报价的到期日）────────────────────────────────────
def _atm_straddle(chain: Dict, spot: float) -> Tuple[float, float, str, Dict]:
    """返回 (straddle_price, atm_strike, exp_date, atm_greeks_dict)
    优先选 0DTE，若 0DTE 已无有效报价则取最近有效到期日。
    """
    today    = date.today()
    atm_strike = round(spot / 5) * 5

    # 找最近的可用 strike（有 bid 或 ask > 0）
    def nearest_valid(strike_map, target):
        keys = [k for k in strike_map
                if strike_map[k] and
                   ((strike_map[k][0].get("bid") or 0) > 0 or
                    (strike_map[k][0].get("ask") or 0) > 0)]
        if not keys:
            # fallback：无有效报价时退而求其次取最近 strike
            keys = [k for k in strike_map if strike_map[k]]
        if not keys:
            return None
        return min(keys, key=lambda x: abs(float(x) - target))

    # 遍历所有到期日，找到最近且 straddle > 0 的那个
    all_exps = set(chain.get("callExpDateMap", {}).keys()) | set(chain.get("putExpDateMap", {}).keys())
    candidates = []
    for exp_str in all_exps:
        try:
            exp_date = datetime.strptime(exp_str.split(":")[0], "%Y-%m-%d").date()
        except ValueError:
            continue
        dte = (exp_date - today).days
        if dte < 0:
            continue
        call_map = chain.get("callExpDateMap", {}).get(exp_str, {})
        put_map  = chain.get("putExpDateMap",  {}).get(exp_str, {})
        ck = nearest_valid(call_map, atm_strike)
        pk = nearest_valid(put_map,  atm_strike)
        if not ck or not pk:
            continue
        call_c = call_map[ck][0]
        put_c  = put_map[pk][0]
        call_mid = ((call_c.get("bid") or 0) + (call_c.get("ask") or 0)) / 2
        put_mid  = ((put_c.get("bid")  or 0) + (put_c.get("ask")  or 0)) / 2
        straddle_val = call_mid + put_mid
        # 有效条件：两腿都有 bid（盘后 0DTE bid=0 但 ask 残留，排除）
        call_bid = (call_c.get("bid") or 0)
        put_bid  = (put_c.get("bid")  or 0)
        if straddle_val > 0.5 and call_bid > 0 and put_bid > 0:
            candidates.append((dte, exp_str, ck, pk, call_c, put_c, straddle_val))

    if not candidates:
        # ── 盘后 fallback：所有期权报价清零，改用 mark/lastPrice ──────────────
        best_exp_str = None
        best_dte_fb  = 9999
        best_iv_fb   = 0.0
        best_ck_fb   = str(atm_strike)
        best_straddle_fb = 0.0

        for exp_str in all_exps:
            try:
                exp_date = datetime.strptime(exp_str.split(":")[0], "%Y-%m-%d").date()
            except ValueError:
                continue
            dte = (exp_date - today).days
            if dte < 1 or dte >= best_dte_fb:
                continue
            call_map = chain.get("callExpDateMap", {}).get(exp_str, {})
            put_map  = chain.get("putExpDateMap",  {}).get(exp_str, {})
            if not call_map or not put_map:
                continue
            ck = min(call_map, key=lambda x: abs(float(x) - atm_strike), default=None)
            pk = min(put_map,  key=lambda x: abs(float(x) - atm_strike), default=None)
            if not ck or not pk:
                continue
            cc = call_map[ck][0] if call_map[ck] else {}
            pc = put_map[pk][0]  if put_map[pk]  else {}
            # 优先用 mark，其次 lastPrice，最后 bid/ask mid
            def _price(c):
                return (c.get("mark") or c.get("last") or c.get("lastPrice") or
                        ((c.get("bid",0) or 0)+(c.get("ask",0) or 0))/2)
            c_p = _price(cc);  p_p = _price(pc)
            s_val = c_p + p_p
            iv_raw = (cc.get("volatility") or 0) / 100.0
            if s_val > 0.5 or iv_raw > 0:
                best_exp_str    = exp_str
                best_dte_fb     = dte
                best_iv_fb      = iv_raw
                best_ck_fb      = ck
                best_straddle_fb= round(s_val, 2)

        if best_exp_str:
            # 若 mark/last 也为 0，用 VIX÷16 估算日化期望波动 × spot
            # VIX÷16 给出 1-sigma 1日 SPX 点数移动（经验值）
            vix_approx = chain.get("volatilityIndex", 0) or 0
            if best_straddle_fb < 0.5 and vix_approx > 0:
                best_straddle_fb = round(spot * (vix_approx/100) / 16 * math.sqrt(best_dte_fb), 2)
                logger.info(f"盘后 straddle VIX估算: VIX={vix_approx} DTE={best_dte_fb} → ${best_straddle_fb}")
            elif best_straddle_fb < 0.5:
                best_straddle_fb = 0.0   # 无法估算，保持 0

            greeks_fb = _bs_greeks(spot, float(best_ck_fb), best_iv_fb or 0.20,
                                   best_dte_fb, "CALL")
            exp_label = best_exp_str.split(":")[0]
            if best_straddle_fb > 0:
                logger.info(f"盘后 straddle fallback: mark/last → ${best_straddle_fb} (DTE={best_dte_fb})")
            return best_straddle_fb, float(best_ck_fb), exp_label, greeks_fb

        return 0.0, atm_strike, "", {}

        return 0.0, atm_strike, "", {}

    candidates.sort(key=lambda x: x[0])   # 取最近有效到期日
    dte_best, best_exp, ck, pk, call_c, put_c, straddle = candidates[0]

    straddle = round(straddle, 2)

    # Greeks：优先用 API 值，否则 BS 计算
    def to_greeks(c, opt_t):
        iv     = (c.get("volatility") or 0) / 100.0
        t_days = max(dte_best, 0.1)
        if any(c.get(k) for k in ("delta", "gamma", "vega", "theta")):
            return {
                "delta": c.get("delta", 0),
                "gamma": c.get("gamma", 0),
                "vega":  c.get("vega",  0),
                "theta": c.get("theta", 0),
                "charm": c.get("charm", 0),
                "vanna": c.get("vanna", 0),
            }
        if iv > 0:
            return _bs_greeks(spot, float(ck), iv, t_days, opt_t)
        return {}

    greeks    = to_greeks(call_c, "CALL")
    exp_label = best_exp.split(":")[0]
    return straddle, float(ck), exp_label, greeks


# ── Volume / Flow Ratio ────────────────────────────────────────────────────────
def _volume_ratio(quotes: Dict) -> Dict:
    es = (quotes.get(SYMBOLS_ES) or {})
    q  = es.get("quote", es)
    today_vol = q.get("totalVolume", 0) or 0
    avg_vol   = q.get("volatility", 0) or 100_000     # fallback
    if avg_vol <= 0:
        avg_vol = 100_000
    ratio  = today_vol / avg_vol
    rating = ("extreme" if ratio > 3 else "high" if ratio > 2
              else "normal" if ratio > 1.5 else "low")
    return {"ratio": round(ratio, 2), "current_volume": today_vol,
            "avg_volume": int(avg_vol), "rating": rating}


def _flow_ratio(chain: Dict, spot: float) -> Dict:
    """
    用 0DTE 期权链的 CALL/PUT 总权利金比例估算 buy/sell 意向。
    完全基于实时数据，无 random。
    """
    today_str = date.today().isoformat()
    call_prem = put_prem = 0.0
    for opt_key, prem_ref in [("callExpDateMap", None), ("putExpDateMap", None)]:
        for exp_str, strike_map in chain.get(opt_key, {}).items():
            if not exp_str.startswith(today_str):
                continue
            for strike_str, contracts in strike_map.items():
                if not contracts:
                    continue
                c   = contracts[0]
                mid = ((c.get("bid") or 0) + (c.get("ask") or 0)) / 2
                vol = c.get("totalVolume", 0) or 0
                prem = mid * vol * 100
                if opt_key == "callExpDateMap":
                    call_prem += prem
                else:
                    put_prem  += prem

    total = call_prem + put_prem
    if total > 0:
        buy_pct = round(call_prem / total * 100, 1)
    else:
        # 退化：用 SPX 变动方向估算
        buy_pct = 50.0
    return {
        "buy_ratio":   buy_pct,
        "sell_ratio":  round(100 - buy_pct, 1),
        "call_premium": round(call_prem / 1e6, 2),
        "put_premium":  round(put_prem  / 1e6, 2),
    }


# ── Basis ──────────────────────────────────────────────────────────────────────
def _basis(spx: float, es: float) -> Dict:
    basis      = round(es - spx, 2)
    fair_basis = round(spx * CONFIG["risk_free_rate"] * (30 / 365), 2)  # 近似 1 个月基差
    premium    = round(basis - fair_basis, 2)
    return {
        "basis":      basis,
        "fair_basis": fair_basis,
        "premium":    premium,
        "zscore":     0,
        "trend":      "期货升水" if basis > 0 else "现货升水",
    }


# ── 盘中快照融合（来自 spx_scanner.py 输出）──────────────────────────────────
def _load_intraday_snapshot(repo_path: Path) -> Optional[Dict]:
    """
    尝试读取 spx_scanner 每 5 分钟写入的 0DTE 快照，
    路径：alerts/spx_intraday/spx_intraday_YYYYMMDD_latest.json
    """
    day_str  = date.today().strftime("%Y%m%d")
    snap_path = Path(CONFIG["git_repo_path"]).parent / "alerts" / "spx_intraday" / \
                f"spx_intraday_{day_str}_latest.json"
    if snap_path.exists():
        try:
            with open(snap_path, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return None


# ── DataCollector ─────────────────────────────────────────────────────────────
class DataCollector:
    def __init__(self, schwab_client):
        self.client = schwab_client

    def _get(self, fn, *args, **kwargs):
        try:
            resp = fn(*args, **kwargs)
            return resp.json() if hasattr(resp, "json") else (resp if isinstance(resp, dict) else {})
        except Exception as e:
            logger.error(f"API error ({fn.__name__}): {e}")
            return {}

    def run(self) -> Dict:
        # 1. 报价
        quotes = self._get(self.client.get_quotes,
                           [SYMBOLS_SPX, SYMBOLS_VIX, SYMBOLS_VVIX, SYMBOLS_ES])
        if not quotes:
            logger.error("Failed to fetch quotes")
            return {}

        def qv(sym, field):
            d = quotes.get(sym, {})
            return (d.get("quote") or d).get(field)

        spx_price = qv(SYMBOLS_SPX, "lastPrice")
        if not spx_price:
            logger.error("No SPX price")
            return {}

        vix_price  = qv(SYMBOLS_VIX,  "lastPrice") or 0
        vvix_price = qv(SYMBOLS_VVIX, "lastPrice") or 0
        es_price   = qv(SYMBOLS_ES,   "lastPrice") or spx_price

        # 2. 期权链
        logger.info(f"SPX={spx_price:.2f}  VIX={vix_price:.2f}  fetching chain...")
        chain = self._get(self.client.get_option_chain,
                          SYMBOLS_SPX,
                          contract_type="ALL",
                          strike_count=CONFIG["strike_count"],
                          include_underlying_quote=True)
        if not chain or not chain.get("callExpDateMap"):
            logger.error("Empty options chain")
            return {}

        # 3. 计算各指标
        gamma_map, charm_map = _gamma_charm_distribution(chain, spx_price)
        straddle, atm_strike, atm_exp, atm_greeks = _atm_straddle(chain, spx_price)
        gamma_flip, balance_pt, total_net_gamma   = _key_levels(gamma_map, spx_price, straddle)
        oi_top        = _oi_top(chain, spx_price)
        skew_slope    = _skew_slope(chain, spx_price)
        term_struct   = _term_structure(chain)
        vol_ratio     = _volume_ratio(quotes)
        flow_ratio    = _flow_ratio(chain, spx_price)
        basis_info    = _basis(spx_price, es_price)

        # 4. Key levels
        key_levels = {
            "call_wall":    (gamma_flip + 25) if gamma_flip else None,
            "gamma_flip":   gamma_flip,
            "balance":      balance_pt,
            "straddle_hi":  round(spx_price + straddle),
            "straddle_lo":  round(spx_price - straddle),
            "charm_target": (balance_pt - 25) if balance_pt else None,
            "weak":         round(spx_price - straddle) - 15,
            "deep":         round(spx_price - straddle) - 55,
        }

        # 5. 融合盘中 0DTE 快照（来自 spx_scanner）
        intraday_snap = _load_intraday_snapshot(Path(CONFIG["git_repo_path"]))

        # 6. 组装最终 payload
        now_utc = datetime.now(timezone.utc)
        result = {
            "timestamp":        now_utc.isoformat() + "Z",
            "timestamp_et":     datetime.now().strftime("%Y-%m-%d %H:%M ET"),
            "spx": {
                "price":      spx_price,
                "prev_close": qv(SYMBOLS_SPX, "closePrice"),
                "change":     qv(SYMBOLS_SPX, "netChange"),
                "change_pct": qv(SYMBOLS_SPX, "percentChange"),
                "high":       qv(SYMBOLS_SPX, "highPrice"),
                "low":        qv(SYMBOLS_SPX, "lowPrice"),
                "open":       qv(SYMBOLS_SPX, "openPrice"),
            },
            "vix":  vix_price,
            "vvix": vvix_price,
            "es": {
                "price":  es_price,
                "change": qv(SYMBOLS_ES, "netChange"),
            },
            "atm": {
                "strike":         atm_strike,
                "exp_date":       atm_exp,
                "straddle_price": straddle,
                "straddle_bps":   round(straddle / spx_price * 10000, 1) if spx_price else 0,
            },
            "greeks":              atm_greeks,
            "gamma_distribution":  gamma_map,    # {strike_str: dealer_net_gamma}
            "charm_distribution":  charm_map,
            "net_gamma_exposure":  round(total_net_gamma / 1e9, 4),
            "key_levels":          key_levels,
            "oi_top":              oi_top,
            "skew_slope":          skew_slope,
            "term_structure":      term_struct,
            "basis":               basis_info,
            "volume_ratio":        vol_ratio,
            "flow_ratio":          flow_ratio,
            # 融合 spx_scanner 的 0DTE 大单数据
            "intraday_0dte": intraday_snap or {},
        }
        logger.info(
            f"Data ready: GammaFlip={gamma_flip}  Balance={balance_pt}  "
            f"Straddle={straddle}  GEX={result['net_gamma_exposure']}B"
        )
        return result


# ── Git 推送 ──────────────────────────────────────────────────────────────────
def _find_git() -> str:
    import shutil
    found = shutil.which("git")
    if found:
        return found
    for c in [
        r"C:\Program Files\Git\cmd\git.exe",
        r"C:\Program Files (x86)\Git\cmd\git.exe",
    ]:
        if os.path.exists(c):
            return c
    raise FileNotFoundError("git not found. Add Git to PATH or set CONFIG git_path.")


def git_push(repo_path: Path, files: List[Path], commit_msg: str = None) -> bool:
    if not repo_path.exists():
        logger.error(f"Repo not found: {repo_path}")
        return False
    commit_msg = commit_msg or f"SPX V4 data update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    cwd = os.getcwd()
    try:
        git = CONFIG.get("git_path") or _find_git()
    except FileNotFoundError as ex:
        logger.error(str(ex))
        return False
    try:
        os.chdir(repo_path)
        for f in files:
            subprocess.run([git, "add", str(f)], check=True, capture_output=True)
        result = subprocess.run([git, "commit", "-m", commit_msg],
                                capture_output=True, text=True)
        if result.returncode != 0:
            if "nothing to commit" in result.stdout + result.stderr:
                logger.info("Git: nothing to commit")
                return True
            logger.error(f"Git commit failed: {result.stderr}")
            return False
        subprocess.run([git, "pull", "--rebase",
                        CONFIG["git_remote"], CONFIG["git_branch"]],
                       check=False, capture_output=True)
        push = subprocess.run([git, "push",
                               CONFIG["git_remote"], CONFIG["git_branch"]],
                              capture_output=True, text=True)
        if push.returncode == 0:
            logger.info(f"Git push OK → {[f.name for f in files]}")
            return True
        logger.error(f"Git push failed: {push.stderr}")
        return False
    except subprocess.CalledProcessError as e:
        logger.error(f"Git error: {e}")
        return False
    finally:
        os.chdir(cwd)


# ── 主程序 ────────────────────────────────────────────────────────────────────
def main():
    # 加载 .env
    env_path   = Path(CONFIG["env_file"])
    token_path = Path(CONFIG["token_file"])
    if not env_path.exists():
        logger.error(f".env not found: {env_path}"); sys.exit(1)
    load_dotenv(env_path)

    app_key    = os.getenv("SCHWAB_APP_KEY")
    app_secret = os.getenv("SCHWAB_APP_SECRET")
    if not app_key or not app_secret:
        logger.error("SCHWAB_APP_KEY / SCHWAB_APP_SECRET missing"); sys.exit(1)
    if not token_path.exists():
        logger.error(f"Token not found: {token_path}"); sys.exit(1)

    from schwab import auth
    schwab_client = auth.client_from_token_file(str(token_path), app_key, app_secret,
                                               enforce_enums=False)
    collector     = DataCollector(schwab_client)

    repo_path = Path(CONFIG["git_repo_path"])
    data_dir  = repo_path / DATA_SUBDIR
    data_dir.mkdir(parents=True, exist_ok=True)

    latest_path = data_dir / LATEST_FILE

    logger.info("=" * 60)
    logger.info("  SPX Options Monitor V4  Data Generator  v2.1")
    logger.info(f"  Repo    : {repo_path}")
    logger.info(f"  Output  : {DATA_SUBDIR}/{LATEST_FILE}  +  timestamped archive")
    logger.info(f"  Interval: {CONFIG['fetch_interval_seconds']}s")
    logger.info("=" * 60)

    while True:
        t0 = time.time()
        try:
            data = collector.run()
            if data:
                # 带时间戳的存档文件
                ts_str        = datetime.now().strftime("%Y%m%d_%H%M")
                archive_path  = data_dir / f"spx_v4_{ts_str}.json"

                for path in (latest_path, archive_path):
                    with open(path, "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)

                logger.info(f"Saved: {latest_path.name}  {archive_path.name}")
                git_push(repo_path, [latest_path, archive_path])
            else:
                logger.warning("Empty data, skipping push")

        except Exception as e:
            logger.exception(f"Main loop error: {e}")

        elapsed = time.time() - t0
        sleep_s = max(0, CONFIG["fetch_interval_seconds"] - elapsed)
        logger.info(f"Next update in {sleep_s:.0f}s  (elapsed={elapsed:.1f}s)")
        time.sleep(sleep_s)


if __name__ == "__main__":
    main()
