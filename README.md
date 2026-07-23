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
## 📅 2026-07-23

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `oi_report_core72_20260723.json` | OI变化对比报告 | 2026-07-23 10:53 | [下载](oi_snapshots/20260723/oi_report_core72_20260723.json) | {"date": "2026-07-23", "surging": 0, "shrinking": 0} |


## 📅 2026-07-22

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `oi_report_pre_mkt_20260722.json` | OI变化对比报告 | 2026-07-22 22:48 | [下载](oi_snapshots/20260722/oi_report_pre_mkt_20260722.json) | {"date": "2026-07-22", "surging": 0, "shrinking": 0} |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-07-22 22:42 | [下载](NDXalerts/20260722/ndx_gamma_latest.json) | {"ts": "10:42", "ts_full": "2026-07-22T10:42:13.335170-04:00", "symbol": "NDX",  |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-07-22 22:40 | [下载](SPXalerts/20260722/spx_gamma_latest.json) | {"ts": "10:40", "ts_full": "2026-07-22T10:40:03.209221-04:00", "symbol": "SPX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

