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
## 📅 2026-08-03

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `claude_analysis_094124.json` | Claude深度分析 | 2026-08-03 09:41 | [下载](ClaudeAnalysis/20260803/claude_analysis_094124.json) | {"generated_at": "2026-08-03T09:41:24.075982-04:00", "generated_at_display": "20 |
| `ndx_ndte_report_20260803_0940.json` | NDX 非0DTE信号 | 2026-08-03 09:40 | [下载](NDXalerts/20260803/ndx_ndte_report_20260803_0940.json) | {"label": "非0DTE · 09:40 ET", "signals": 5, "direction": "极度偏多 🟢🟢", "net_premium |
| `ndx_0dte_report_20260803_0940.json` | NDX 0DTE信号 | 2026-08-03 09:40 | [下载](NDXalerts/20260803/ndx_0dte_report_20260803_0940.json) | {"label": "0DTE · 09:40 ET", "signals": 4, "direction": "极度偏多 🟢🟢", "net_premium_ |
| `spx_0dte_report_20260803_0938.json` | SPX 0DTE信号 | 2026-08-03 09:38 | [下载](SPXalerts/20260803/spx_0dte_report_20260803_0938.json) | {"label": "0DTE · 09:38 ET", "signals": 163, "direction": "极度偏多 🟢🟢", "net_premiu |
| `ndx_0dte_report_20260803_0938.json` | NDX 0DTE信号 | 2026-08-03 09:38 | [下载](NDXalerts/20260803/ndx_0dte_report_20260803_0938.json) | {"label": "0DTE · 09:38 ET", "signals": 2, "direction": "极度偏多 🟢🟢", "net_premium_ |
| `spx_0dte_report_20260803_0936.json` | SPX 0DTE信号 | 2026-08-03 09:36 | [下载](SPXalerts/20260803/spx_0dte_report_20260803_0936.json) | {"label": "0DTE · 09:36 ET", "signals": 84, "direction": "极度偏多 🟢🟢", "net_premium |
| `ndx_ndte_20260803_0935.json` | NDX 非0DTE信号 | 2026-08-03 09:35 | [下载](NDXalerts/20260803/ndx_ndte_20260803_0935.json) | {"signals": 3, "timestamp_et": "2026-08-03 09:35 ET"} |
| `ndx_0dte_20260803_0934.json` | NDX 0DTE信号 | 2026-08-03 09:34 | [下载](NDXalerts/20260803/ndx_0dte_20260803_0934.json) | {"signals": 2, "timestamp_et": "2026-08-03 09:34 ET"} |
| `spx_0dte_20260803_0932.json` | SPX 0DTE信号 | 2026-08-03 09:32 | [下载](SPXalerts/20260803/spx_0dte_20260803_0932.json) | {"signals": 64, "timestamp_et": "2026-08-03 09:32 ET"} |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-08-03 09:30 | [下载](NDXalerts/20260803/ndx_gamma_latest.json) | {"ts": "09:30", "ts_full": "2026-08-03T09:30:32.664483-04:00", "symbol": "NDX",  |
| `spx_intraday_20260803_0930.json` | SPX盘中5分钟快报 | 2026-08-03 09:30 | [下载](SPXalerts/20260803/spx_intraday_20260803_0930.json) | {} |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-08-03 09:29 | [下载](SPXalerts/20260803/spx_gamma_latest.json) | {"ts": "09:29", "ts_full": "2026-08-03T09:29:27.153842-04:00", "symbol": "SPX",  |
| `oi_report_pre_mkt_20260803.json` | OI变化对比报告 | 2026-08-03 09:13 | [下载](oi_snapshots/20260803/oi_report_pre_mkt_20260803.json) | {"date": "2026-08-03", "surging": 100, "shrinking": 100} |
| `oi_pre_mkt_20260803.json` | 盘前OI快照 | 2026-08-03 09:13 | [下载](oi_snapshots/20260803/oi_pre_mkt_20260803.json) | {"tickers": 264} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

