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
## 📅 2026-08-10

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_0dte_report_20260810_0932.json` | SPX 0DTE信号 | 2026-08-10 09:32 | [下载](SPXalerts/20260810/spx_0dte_report_20260810_0932.json) | {"label": "0DTE · 09:32 ET", "signals": 61, "direction": "极度偏多 🟢🟢", "net_premium |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-08-10 09:30 | [下载](NDXalerts/20260810/ndx_gamma_latest.json) | {"ts": "09:30", "ts_full": "2026-08-10T09:30:11.061337-04:00", "symbol": "NDX",  |
| `spx_intraday_20260810_0930.json` | SPX盘中5分钟快报 | 2026-08-10 09:30 | [下载](SPXalerts/20260810/spx_intraday_20260810_0930.json) | {} |
| `oi_pre_mkt_20260810.json` | 盘前OI快照 | 2026-08-10 09:29 | [下载](oi_snapshots/20260810/oi_pre_mkt_20260810.json) | {"tickers": 269} |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-08-10 09:29 | [下载](SPXalerts/20260810/spx_gamma_latest.json) | {"ts": "09:29", "ts_full": "2026-08-10T09:29:08.630110-04:00", "symbol": "SPX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

