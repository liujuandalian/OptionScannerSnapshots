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
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-08-05 09:30 | [下载](SPXalerts/20260805/spx_gamma_latest.json) | {"ts": "09:30", "ts_full": "2026-08-05T09:30:14.449907-04:00", "symbol": "SPX",  |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-08-05 09:29 | [下载](NDXalerts/20260805/ndx_gamma_latest.json) | {"ts": "09:29", "ts_full": "2026-08-05T09:29:09.492175-04:00", "symbol": "NDX",  |
| `oi_report_pre_mkt_20260805.json` | OI变化对比报告 | 2026-08-05 08:55 | [下载](oi_snapshots/20260805/oi_report_pre_mkt_20260805.json) | {"date": "2026-08-05", "surging": 100, "shrinking": 100} |
| `oi_pre_mkt_20260805.json` | 盘前OI快照 | 2026-08-05 08:55 | [下载](oi_snapshots/20260805/oi_pre_mkt_20260805.json) | {"tickers": 264} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

