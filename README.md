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
## 📅 2026-08-05

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `claude_analysis_141932.json` | Claude深度分析 | 2026-08-05 14:19 | [下载](ClaudeAnalysis/20260805/claude_analysis_141932.json) | {"generated_at": "2026-08-05T14:19:32.027262-04:00", "generated_at_display": "20 |
| `spx_0dte_report_20260805_1417.json` | SPX 0DTE信号 | 2026-08-05 14:17 | [下载](SPXalerts/20260805/spx_0dte_report_20260805_1417.json) | {"label": "0DTE · 14:17 ET", "signals": 261, "direction": "多空均衡 ⚪", "net_premium |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-08-05 14:16 | [下载](NDXalerts/20260805/ndx_gamma_latest.json) | {"ts": "14:16", "ts_full": "2026-08-05T14:16:31.513635-04:00", "symbol": "NDX",  |
| `claude_analysis_141559.json` | Claude深度分析 | 2026-08-05 14:16 | [下载](ClaudeAnalysis/20260805/claude_analysis_141559.json) | {"generated_at": "2026-08-05T14:15:59.302141-04:00", "generated_at_display": "20 |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-08-05 14:15 | [下载](SPXalerts/20260805/spx_gamma_latest.json) | {"ts": "14:15", "ts_full": "2026-08-05T14:15:09.115495-04:00", "symbol": "SPX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

