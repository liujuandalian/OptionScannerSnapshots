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
| `claude_analysis_093700.json` | Claude深度分析 | 2026-08-05 09:37 | [下载](ClaudeAnalysis/20260805/claude_analysis_093700.json) | {"generated_at": "2026-08-05T09:37:00.360909-04:00", "generated_at_display": "20 |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-08-05 09:36 | [下载](NDXalerts/20260805/ndx_gamma_latest.json) | {"ts": "09:36", "ts_full": "2026-08-05T09:36:49.215692-04:00", "symbol": "NDX",  |
| `claude_analysis_093529.json` | Claude深度分析 | 2026-08-05 09:35 | [下载](ClaudeAnalysis/20260805/claude_analysis_093529.json) | {"generated_at": "2026-08-05T09:35:29.827822-04:00", "generated_at_display": "20 |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-08-05 09:34 | [下载](SPXalerts/20260805/spx_gamma_latest.json) | {"ts": "09:34", "ts_full": "2026-08-05T09:34:29.828569-04:00", "symbol": "SPX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

