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
## 📅 2026-08-12

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_0dte_report_20260812_1223.json` | SPX 0DTE信号 | 2026-08-12 12:23 | [下载](SPXalerts/20260812/spx_0dte_report_20260812_1223.json) | {"label": "0DTE · 12:23 ET", "signals": 19, "direction": "偏多 🟢", "net_premium_M" |
| `claude_analysis_122202.json` | Claude深度分析 | 2026-08-12 12:22 | [下载](ClaudeAnalysis/20260812/claude_analysis_122202.json) | {"generated_at": "2026-08-12T12:22:02.320906-04:00", "generated_at_display": "20 |
| `claude_analysis_122041.json` | Claude深度分析 | 2026-08-12 12:20 | [下载](ClaudeAnalysis/20260812/claude_analysis_122041.json) | {"generated_at": "2026-08-12T12:20:41.646113-04:00", "generated_at_display": "20 |
| `spx_intraday_20260812_1220.json` | SPX盘中5分钟快报 | 2026-08-12 12:20 | [下载](SPXalerts/20260812/spx_intraday_20260812_1220.json) | {} |
| `spx_0dte_20260812_1217.json` | SPX 0DTE信号 | 2026-08-12 12:17 | [下载](SPXalerts/20260812/spx_0dte_20260812_1217.json) | {"signals": 21, "timestamp_et": "2026-08-12 12:17 ET"} |
| `claude_analysis_121613.json` | Claude深度分析 | 2026-08-12 12:16 | [下载](ClaudeAnalysis/20260812/claude_analysis_121613.json) | {"generated_at": "2026-08-12T12:16:13.766265-04:00", "generated_at_display": "20 |
| `claude_analysis_121448.json` | Claude深度分析 | 2026-08-12 12:14 | [下载](ClaudeAnalysis/20260812/claude_analysis_121448.json) | {"generated_at": "2026-08-12T12:14:48.010203-04:00", "generated_at_display": "20 |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-08-12 12:14 | [下载](SPXalerts/20260812/spx_gamma_latest.json) | {"ts": "12:14", "ts_full": "2026-08-12T12:14:10.263515-04:00", "symbol": "SPX",  |
| `claude_analysis_121328.json` | Claude深度分析 | 2026-08-12 12:13 | [下载](ClaudeAnalysis/20260812/claude_analysis_121328.json) | {"generated_at": "2026-08-12T12:13:28.483046-04:00", "generated_at_display": "20 |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-08-12 12:13 | [下载](NDXalerts/20260812/ndx_gamma_latest.json) | {"ts": "12:13", "ts_full": "2026-08-12T12:13:07.365510-04:00", "symbol": "NDX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

