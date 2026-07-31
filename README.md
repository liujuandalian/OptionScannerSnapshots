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
## 📅 2026-07-31

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `ndx_ndte_report_20260731_1359.json` | NDX 非0DTE信号 | 2026-07-31 13:59 | [下载](NDXalerts/20260731/ndx_ndte_report_20260731_1359.json) | {"label": "非0DTE · 13:59 ET", "signals": 286, "direction": "偏多 🟢", "net_premium_ |
| `ndx_0dte_report_20260731_1358.json` | NDX 0DTE信号 | 2026-07-31 13:58 | [下载](NDXalerts/20260731/ndx_0dte_report_20260731_1358.json) | {"label": "0DTE · 13:58 ET", "signals": 140, "direction": "极度偏多 🟢🟢", "net_premiu |
| `oi_report_pre_mkt_20260731.json` | OI变化对比报告 | 2026-07-31 13:57 | [下载](oi_snapshots/20260731/oi_report_pre_mkt_20260731.json) | {"date": "2026-07-31", "surging": 100, "shrinking": 100} |
| `oi_pre_mkt_20260731.json` | 盘前OI快照 | 2026-07-31 13:57 | [下载](oi_snapshots/20260731/oi_pre_mkt_20260731.json) | {"tickers": 264} |
| `spx_0dte_report_20260731_1355.json` | SPX 0DTE信号 | 2026-07-31 13:55 | [下载](SPXalerts/20260731/spx_0dte_report_20260731_1355.json) | {"label": "0DTE · 13:55 ET", "signals": 188, "direction": "极度偏多 🟢🟢", "net_premiu |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-07-31 13:55 | [下载](SPXalerts/20260731/spx_gamma_latest.json) | {"ts": "13:55", "ts_full": "2026-07-31T13:55:30.872274-04:00", "symbol": "SPX",  |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-07-31 13:54 | [下载](NDXalerts/20260731/ndx_gamma_latest.json) | {"ts": "13:54", "ts_full": "2026-07-31T13:54:14.627898-04:00", "symbol": "NDX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

