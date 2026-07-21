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
## 📅 2026-07-21

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `claude_analysis_094406.json` | Claude深度分析 | 2026-07-21 09:44 | [下载](ClaudeAnalysis/20260721/claude_analysis_094406.json) | {"generated_at": "2026-07-21T09:44:06.318567-04:00", "generated_at_display": "20 |
| `spx_0dte_report_20260721_0943.json` | SPX 0DTE信号 | 2026-07-21 09:43 | [下载](SPXalerts/20260721/spx_0dte_report_20260721_0943.json) | {"label": "0DTE · 09:43 ET", "signals": 186, "direction": "多空均衡 ⚪", "net_premium |
| `ndx_0dte_report_20260721_0943.json` | NDX 0DTE信号 | 2026-07-21 09:43 | [下载](NDXalerts/20260721/ndx_0dte_report_20260721_0943.json) | {"label": "0DTE · 09:43 ET", "signals": 7, "direction": "偏多 🟢", "net_premium_M": |
| `claude_analysis_094148.json` | Claude深度分析 | 2026-07-21 09:41 | [下载](ClaudeAnalysis/20260721/claude_analysis_094148.json) | {"generated_at": "2026-07-21T09:41:48.210979-04:00", "generated_at_display": "20 |
| `spx_0dte_20260721_0941.json` | SPX 0DTE信号 | 2026-07-21 09:41 | [下载](SPXalerts/20260721/spx_0dte_20260721_0941.json) | {"signals": 117, "timestamp_et": "2026-07-21 09:41 ET"} |
| `spx_intraday_20260721_0940.json` | SPX盘中5分钟快报 | 2026-07-21 09:40 | [下载](SPXalerts/20260721/spx_intraday_20260721_0940.json) | {} |
| `spx_ndte_20260721_0940.json` | SPX 非0DTE信号 | 2026-07-21 09:40 | [下载](SPXalerts/20260721/spx_ndte_20260721_0940.json) | {"signals": 445, "timestamp_et": "2026-07-21 09:40 ET"} |
| `spx_0dte_20260721_0936.json` | SPX 0DTE信号 | 2026-07-21 09:36 | [下载](SPXalerts/20260721/spx_0dte_20260721_0936.json) | {"signals": 113, "timestamp_et": "2026-07-21 09:36 ET"} |
| `ndx_ndte_report_20260721_0935.json` | NDX 非0DTE信号 | 2026-07-21 09:35 | [下载](NDXalerts/20260721/ndx_ndte_report_20260721_0935.json) | {"label": "非0DTE · 09:35 ET", "signals": 13, "direction": "极度偏多 🟢🟢", "net_premiu |
| `spx_0dte_20260721_0934.json` | SPX 0DTE信号 | 2026-07-21 09:34 | [下载](SPXalerts/20260721/spx_0dte_20260721_0934.json) | {"signals": 93, "timestamp_et": "2026-07-21 09:34 ET"} |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-07-21 09:30 | [下载](SPXalerts/20260721/spx_gamma_latest.json) | {"ts": "09:30", "ts_full": "2026-07-21T09:30:25.940168-04:00", "symbol": "SPX",  |
| `spx_intraday_20260721_0930.json` | SPX盘中5分钟快报 | 2026-07-21 09:30 | [下载](SPXalerts/20260721/spx_intraday_20260721_0930.json) | {} |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-07-21 09:29 | [下载](NDXalerts/20260721/ndx_gamma_latest.json) | {"ts": "09:29", "ts_full": "2026-07-21T09:29:21.125842-04:00", "symbol": "NDX",  |
| `oi_report_pre_mkt_20260721.json` | OI变化对比报告 | 2026-07-21 08:47 | [下载](oi_snapshots/20260721/oi_report_pre_mkt_20260721.json) | {"date": "2026-07-21", "surging": 100, "shrinking": 100} |
| `oi_pre_mkt_20260721.json` | 盘前OI快照 | 2026-07-21 08:47 | [下载](oi_snapshots/20260721/oi_pre_mkt_20260721.json) | {"tickers": 264} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

