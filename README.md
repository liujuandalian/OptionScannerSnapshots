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
## 📅 2026-08-04

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_0dte_report_20260804_0938.json` | SPX 0DTE信号 | 2026-08-04 09:38 | [下载](SPXalerts/20260804/spx_0dte_report_20260804_0938.json) | {"label": "0DTE · 09:38 ET", "signals": 190, "direction": "极度偏多 🟢🟢", "net_premiu |
| `ndx_ndte_report_20260804_0935.json` | NDX 非0DTE信号 | 2026-08-04 09:35 | [下载](NDXalerts/20260804/ndx_ndte_report_20260804_0935.json) | {"label": "非0DTE · 09:35 ET", "signals": 6, "direction": "极度偏多 🟢🟢", "net_premium |
| `spx_0dte_20260804_0934.json` | SPX 0DTE信号 | 2026-08-04 09:34 | [下载](SPXalerts/20260804/spx_0dte_20260804_0934.json) | {"signals": 86, "timestamp_et": "2026-08-04 09:34 ET"} |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-08-04 09:30 | [下载](SPXalerts/20260804/spx_gamma_latest.json) | {"ts": "09:30", "ts_full": "2026-08-04T09:30:28.995436-04:00", "symbol": "SPX",  |
| `spx_intraday_20260804_0930.json` | SPX盘中5分钟快报 | 2026-08-04 09:30 | [下载](SPXalerts/20260804/spx_intraday_20260804_0930.json) | {} |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-08-04 09:29 | [下载](NDXalerts/20260804/ndx_gamma_latest.json) | {"ts": "09:29", "ts_full": "2026-08-04T09:29:20.856264-04:00", "symbol": "NDX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

