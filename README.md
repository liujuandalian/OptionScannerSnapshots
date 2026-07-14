# OptionScannerSnapshots

> Schwab Options Flow Scanner 自动快照仓库 · AI Agent 数据源

## 🤖 AI Agent 读取入口

```
最新数据索引：
https://raw.githubusercontent.com/liujuandalian/OptionScannerSnapshots/main/data/latest.json

GitHub Pages 仪表盘：
https://liujuandalian.github.io/OptionScannerSnapshots/
```

## 🗂️ 目录结构

| 目录 | 内容 | 生成方式 |
|---
## 📅 2026-07-14

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `ndx_0dte_20260714_0940.json` | NDX 0DTE信号 | 2026-07-14 09:40 | [下载](NDXalerts/20260714/ndx_0dte_20260714_0940.json) | {"signals": 8, "timestamp_et": "2026-07-14 09:40 ET"} |
| `ndx_ndte_20260714_0940.json` | NDX 非0DTE信号 | 2026-07-14 09:40 | [下载](NDXalerts/20260714/ndx_ndte_20260714_0940.json) | {"signals": 8, "timestamp_et": "2026-07-14 09:40 ET"} |
| `spx_0dte_20260714_0938.json` | SPX 0DTE信号 | 2026-07-14 09:39 | [下载](SPXalerts/20260714/spx_0dte_20260714_0938.json) | {"signals": 86, "timestamp_et": "2026-07-14 09:38 ET"} |
| `ndx_0dte_20260714_0936.json` | NDX 0DTE信号 | 2026-07-14 09:36 | [下载](NDXalerts/20260714/ndx_0dte_20260714_0936.json) | {"signals": 2, "timestamp_et": "2026-07-14 09:36 ET"} |
| `ndx_ndte_20260714_0935.json` | NDX 非0DTE信号 | 2026-07-14 09:35 | [下载](NDXalerts/20260714/ndx_ndte_20260714_0935.json) | {"signals": 6, "timestamp_et": "2026-07-14 09:35 ET"} |
| `spx_0dte_report_20260714_0934.json` | SPX 0DTE信号 | 2026-07-14 09:34 | [下载](SPXalerts/20260714/spx_0dte_report_20260714_0934.json) | {"label": "0DTE · 09:34 ET", "signals": 162, "direction": "偏多 🟢", "net_premium_M |
| `ndx_0dte_report_20260714_0934.json` | NDX 0DTE信号 | 2026-07-14 09:34 | [下载](NDXalerts/20260714/ndx_0dte_report_20260714_0934.json) | {"label": "0DTE · 09:34 ET", "signals": 1, "direction": "极度偏多 🟢🟢", "net_premium_ |
| `spx_0dte_report_20260714_0932.json` | SPX 0DTE信号 | 2026-07-14 09:32 | [下载](SPXalerts/20260714/spx_0dte_report_20260714_0932.json) | {"label": "0DTE · 09:32 ET", "signals": 61, "direction": "偏多 🟢", "net_premium_M" |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-07-14 09:30 | [下载](NDXalerts/20260714/ndx_gamma_latest.json) | {"ts": "09:30", "ts_full": "2026-07-14T09:30:21.362318-04:00", "symbol": "NDX",  |
| `spx_intraday_20260714_0930.json` | SPX盘中5分钟快报 | 2026-07-14 09:30 | [下载](SPXalerts/20260714/spx_intraday_20260714_0930.json) | {} |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-07-14 09:29 | [下载](SPXalerts/20260714/spx_gamma_latest.json) | {"ts": "09:29", "ts_full": "2026-07-14T09:29:13.113439-04:00", "symbol": "SPX",  |
| `oi_report_pre_mkt_20260714.json` | OI变化对比报告 | 2026-07-14 08:47 | [下载](oi_snapshots/20260714/oi_report_pre_mkt_20260714.json) | {"date": "2026-07-14", "surging": 100, "shrinking": 100} |
| `oi_pre_mkt_20260714.json` | 盘前OI快照 | 2026-07-14 08:46 | [下载](oi_snapshots/20260714/oi_pre_mkt_20260714.json) | {"tickers": 263} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

