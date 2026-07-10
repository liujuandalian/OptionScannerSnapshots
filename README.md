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
## 📅 2026-07-10

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_0dte_20260710_1019.json` | SPX 0DTE信号 | 2026-07-10 10:19 | [下载](SPXalerts/20260710/spx_0dte_20260710_1019.json) | {"signals": 88, "timestamp_et": "2026-07-10 10:19 ET"} |
| `ndx_0dte_20260710_1017.json` | NDX 0DTE信号 | 2026-07-10 10:17 | [下载](NDXalerts/20260710/ndx_0dte_20260710_1017.json) | {"signals": 44, "timestamp_et": "2026-07-10 10:17 ET"} |
| `ndx_ndte_20260710_1017.json` | NDX 非0DTE信号 | 2026-07-10 10:17 | [下载](NDXalerts/20260710/ndx_ndte_20260710_1017.json) | {"signals": 51, "timestamp_et": "2026-07-10 10:17 ET"} |
| `ndx_0dte_report_20260710_1015.json` | NDX 0DTE信号 | 2026-07-10 10:15 | [下载](NDXalerts/20260710/ndx_0dte_report_20260710_1015.json) | {"label": "0DTE · 10:15 ET", "signals": 50, "direction": "极度偏多 🟢🟢", "net_premium |
| `ndx_0dte_20260710_1013.json` | NDX 0DTE信号 | 2026-07-10 10:13 | [下载](NDXalerts/20260710/ndx_0dte_20260710_1013.json) | {"signals": 45, "timestamp_et": "2026-07-10 10:13 ET"} |
| `spx_0dte_20260710_1013.json` | SPX 0DTE信号 | 2026-07-10 10:13 | [下载](SPXalerts/20260710/spx_0dte_20260710_1013.json) | {"signals": 89, "timestamp_et": "2026-07-10 10:13 ET"} |
| `ndx_ndte_20260710_1012.json` | NDX 非0DTE信号 | 2026-07-10 10:12 | [下载](NDXalerts/20260710/ndx_ndte_20260710_1012.json) | {"signals": 37, "timestamp_et": "2026-07-10 10:12 ET"} |
| `ndx_0dte_report_20260710_1011.json` | NDX 0DTE信号 | 2026-07-10 10:11 | [下载](NDXalerts/20260710/ndx_0dte_report_20260710_1011.json) | {"label": "0DTE · 10:11 ET", "signals": 45, "direction": "极度偏多 🟢🟢", "net_premium |
| `claude_analysis_101035.json` | Claude深度分析 | 2026-07-10 10:10 | [下载](ClaudeAnalysis/20260710/claude_analysis_101035.json) | {"generated_at": "2026-07-10T10:10:35.428133-04:00", "generated_at_display": "20 |
| `claude_analysis_100931.json` | Claude深度分析 | 2026-07-10 10:09 | [下载](ClaudeAnalysis/20260710/claude_analysis_100931.json) | {"generated_at": "2026-07-10T10:09:31.366034-04:00", "generated_at_display": "20 |
| `ndx_0dte_report_20260710_1008.json` | NDX 0DTE信号 | 2026-07-10 10:08 | [下载](NDXalerts/20260710/ndx_0dte_report_20260710_1008.json) | {"label": "0DTE · 10:08 ET", "signals": 38, "direction": "极度偏多 🟢🟢", "net_premium |
| `spx_0dte_20260710_1008.json` | SPX 0DTE信号 | 2026-07-10 10:08 | [下载](SPXalerts/20260710/spx_0dte_20260710_1008.json) | {"signals": 169, "timestamp_et": "2026-07-10 10:08 ET"} |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-07-10 10:08 | [下载](NDXalerts/20260710/ndx_gamma_latest.json) | {"ts": "10:08", "ts_full": "2026-07-10T10:08:31.633071-04:00", "symbol": "NDX",  |
| `claude_analysis_100757.json` | Claude深度分析 | 2026-07-10 10:07 | [下载](ClaudeAnalysis/20260710/claude_analysis_100757.json) | {"generated_at": "2026-07-10T10:07:57.221142-04:00", "generated_at_display": "20 |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-07-10 10:07 | [下载](SPXalerts/20260710/spx_gamma_latest.json) | {"ts": "10:07", "ts_full": "2026-07-10T10:07:19.274121-04:00", "symbol": "SPX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

