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
## 📅 2026-07-13

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_ndte_report_20260713_1609.json` | SPX 非0DTE信号 | 2026-07-13 22:11 | [下载](SPXalerts/20260713/spx_ndte_report_20260713_1609.json) | {"label": "非0DTE · 22:10 ET", "signals": 2484, "direction": "多空均衡 ⚪", "net_premi |


## 📅 2026-07-14

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `oi_report_pre_mkt_20260714.json` | OI变化对比报告 | 2026-07-14 07:00 | [下载](oi_snapshots/20260714/oi_report_pre_mkt_20260714.json) | {"date": "2026-07-14", "surging": 100, "shrinking": 100} |
| `oi_pre_mkt_20260714.json` | 盘前OI快照 | 2026-07-14 06:59 | [下载](oi_snapshots/20260714/oi_pre_mkt_20260714.json) | {"tickers": 263} |
| `oi_report_core72_20260714.json` | OI变化对比报告 | 2026-07-14 04:20 | [下载](oi_snapshots/20260714/oi_report_core72_20260714.json) | {"date": "2026-07-14", "surging": 0, "shrinking": 0} |
| `oi_core72_20260714.json` | 盘后OI核心快照 | 2026-07-14 04:19 | [下载](oi_snapshots/20260714/oi_core72_20260714.json) | {"tickers": 72} |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-07-14 01:34 | [下载](SPXalerts/20260714/spx_gamma_latest.json) | {"ts": "13:34", "ts_full": "2026-07-13T13:34:12.205731-04:00", "symbol": "SPX",  |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-07-14 01:33 | [下载](NDXalerts/20260714/ndx_gamma_latest.json) | {"ts": "13:33", "ts_full": "2026-07-13T13:33:06.326851-04:00", "symbol": "NDX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

