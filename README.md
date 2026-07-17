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
## 📅 2026-07-17

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `ndx_0dte_20260717_0954.json` | NDX 0DTE信号 | 2026-07-17 09:54 | [下载](NDXalerts/20260717/ndx_0dte_20260717_0954.json) | {"signals": 39, "timestamp_et": "2026-07-17 09:54 ET"} |
| `ndx_0dte_20260717_0952.json` | NDX 0DTE信号 | 2026-07-17 09:52 | [下载](NDXalerts/20260717/ndx_0dte_20260717_0952.json) | {"signals": 31, "timestamp_et": "2026-07-17 09:52 ET"} |
| `ndx_0dte_20260717_0949.json` | NDX 0DTE信号 | 2026-07-17 09:49 | [下载](NDXalerts/20260717/ndx_0dte_20260717_0949.json) | {"signals": 30, "timestamp_et": "2026-07-17 09:49 ET"} |
| `claude_analysis_094230.json` | Claude深度分析 | 2026-07-17 09:42 | [下载](ClaudeAnalysis/20260717/claude_analysis_094230.json) | {"generated_at": "2026-07-17T09:42:30.904816-04:00", "generated_at_display": "20 |
| `spx_0dte_20260717_0941.json` | SPX 0DTE信号 | 2026-07-17 09:41 | [下载](SPXalerts/20260717/spx_0dte_20260717_0941.json) | {"signals": 215, "timestamp_et": "2026-07-17 09:41 ET"} |
| `ndx_0dte_20260717_0941.json` | NDX 0DTE信号 | 2026-07-17 09:41 | [下载](NDXalerts/20260717/ndx_0dte_20260717_0941.json) | {"signals": 15, "timestamp_et": "2026-07-17 09:41 ET"} |
| `spx_intraday_20260717_0940.json` | SPX盘中5分钟快报 | 2026-07-17 09:40 | [下载](SPXalerts/20260717/spx_intraday_20260717_0940.json) | {} |
| `spx_0dte_report_20260717_0936.json` | SPX 0DTE信号 | 2026-07-17 09:36 | [下载](SPXalerts/20260717/spx_0dte_report_20260717_0936.json) | {"label": "0DTE · 09:36 ET", "signals": 103, "direction": "偏空 🔴", "net_premium_M |
| `ndx_0dte_report_20260717_0934.json` | NDX 0DTE信号 | 2026-07-17 09:34 | [下载](NDXalerts/20260717/ndx_0dte_report_20260717_0934.json) | {"label": "0DTE · 09:34 ET", "signals": 3, "direction": "纯空 🔴🔴（无CALL信号）", "net_p |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-07-17 09:31 | [下载](SPXalerts/20260717/spx_gamma_latest.json) | {"ts": "09:30", "ts_full": "2026-07-17T09:30:23.514034-04:00", "symbol": "SPX",  |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-07-17 09:29 | [下载](NDXalerts/20260717/ndx_gamma_latest.json) | {"ts": "09:29", "ts_full": "2026-07-17T09:29:15.395625-04:00", "symbol": "NDX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

