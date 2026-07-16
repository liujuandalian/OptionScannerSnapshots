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
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-07-16 09:29 | [下载](SPXalerts/20260716/spx_gamma_latest.json) | {"ts": "09:29", "ts_full": "2026-07-16T09:29:12.064893-04:00", "symbol": "SPX",  |
| `oi_report_pre_mkt_20260716.json` | OI变化对比报告 | 2026-07-16 08:47 | [下载](oi_snapshots/20260716/oi_report_pre_mkt_20260716.json) | {"date": "2026-07-16", "surging": 100, "shrinking": 100} |
| `oi_pre_mkt_20260716.json` | 盘前OI快照 | 2026-07-16 08:47 | [下载](oi_snapshots/20260716/oi_pre_mkt_20260716.json) | {"tickers": 264} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

