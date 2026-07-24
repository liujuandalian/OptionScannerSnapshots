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
## 📅 2026-07-24

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `ndx_0dte_report_20260724_1333.json` | NDX 0DTE信号 | 2026-07-24 13:34 | [下载](NDXalerts/20260724/ndx_0dte_report_20260724_1333.json) | {"label": "0DTE · 13:34 ET", "signals": 14287, "direction": "偏空 🔴", "net_premium |
| `oi_report_core72_20260724.json` | OI变化对比报告 | 2026-07-24 04:44 | [下载](oi_snapshots/20260724/oi_report_core72_20260724.json) | {"date": "2026-07-24", "surging": 100, "shrinking": 100} |
| `oi_core72_20260724.json` | 盘后OI核心快照 | 2026-07-24 04:43 | [下载](oi_snapshots/20260724/oi_core72_20260724.json) | {"tickers": 72} |


## 📅 2026-07-23

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-07-23 21:29 | [下载](NDXalerts/20260723/ndx_gamma_latest.json) | {"ts": "09:29", "ts_full": "2026-07-23T09:29:01.423554-04:00", "symbol": "NDX",  |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-07-23 21:29 | [下载](SPXalerts/20260723/spx_gamma_latest.json) | {"ts": "09:29", "ts_full": "2026-07-23T09:29:01.599470-04:00", "symbol": "SPX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

