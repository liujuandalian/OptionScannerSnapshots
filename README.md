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
## 📅 2026-07-16

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `ndx_0dte_20260716_0942.json` | NDX 0DTE信号 | 2026-07-16 09:42 | [下载](NDXalerts/20260716/ndx_0dte_20260716_0942.json) | {"signals": 17, "timestamp_et": "2026-07-16 09:42 ET"} |
| `claude_analysis_094201.json` | Claude深度分析 | 2026-07-16 09:42 | [下载](ClaudeAnalysis/20260716/claude_analysis_094201.json) | {"generated_at": "2026-07-16T09:42:01.589550-04:00", "generated_at_display": "20 |
| `spx_ndte_20260716_0940.json` | SPX 非0DTE信号 | 2026-07-16 09:40 | [下载](SPXalerts/20260716/spx_ndte_20260716_0940.json) | {"signals": 559, "timestamp_et": "2026-07-16 09:40 ET"} |
| `ndx_0dte_20260716_0936.json` | NDX 0DTE信号 | 2026-07-16 09:36 | [下载](NDXalerts/20260716/ndx_0dte_20260716_0936.json) | {"signals": 5, "timestamp_et": "2026-07-16 09:36 ET"} |
| `spx_0dte_20260716_0934.json` | SPX 0DTE信号 | 2026-07-16 09:34 | [下载](SPXalerts/20260716/spx_0dte_20260716_0934.json) | {"signals": 81, "timestamp_et": "2026-07-16 09:34 ET"} |
| `spx_0dte_20260716_0932.json` | SPX 0DTE信号 | 2026-07-16 09:32 | [下载](SPXalerts/20260716/spx_0dte_20260716_0932.json) | {"signals": 58, "timestamp_et": "2026-07-16 09:32 ET"} |
| `spx_stock_flow_latest.json` | 个股期权流量报告 | 2026-07-16 09:31 | [下载](SPXalerts/20260716/spx_stock_flow_latest.json) | {} |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-07-16 09:30 | [下载](NDXalerts/20260716/ndx_gamma_latest.json) | {"ts": "09:30", "ts_full": "2026-07-16T09:30:18.306714-04:00", "symbol": "NDX",  |
| `spx_intraday_20260716_0930.json` | SPX盘中5分钟快报 | 2026-07-16 09:30 | [下载](SPXalerts/20260716/spx_intraday_20260716_0930.json) | {} |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-07-16 09:29 | [下载](SPXalerts/20260716/spx_gamma_latest.json) | {"ts": "09:29", "ts_full": "2026-07-16T09:29:12.064893-04:00", "symbol": "SPX",  |
| `oi_report_pre_mkt_20260716.json` | OI变化对比报告 | 2026-07-16 08:47 | [下载](oi_snapshots/20260716/oi_report_pre_mkt_20260716.json) | {"date": "2026-07-16", "surging": 100, "shrinking": 100} |
| `oi_pre_mkt_20260716.json` | 盘前OI快照 | 2026-07-16 08:47 | [下载](oi_snapshots/20260716/oi_pre_mkt_20260716.json) | {"tickers": 264} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

