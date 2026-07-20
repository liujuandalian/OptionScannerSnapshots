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
## 📅 2026-07-20

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_stock_flow_latest.json` | 个股期权流量报告 | 2026-07-20 09:41 | [下载](SPXalerts/20260720/spx_stock_flow_latest.json) | {} |
| `spx_ndte_20260720_0940.json` | SPX 非0DTE信号 | 2026-07-20 09:40 | [下载](SPXalerts/20260720/spx_ndte_20260720_0940.json) | {"signals": 732, "timestamp_et": "2026-07-20 09:40 ET"} |
| `spx_0dte_20260720_0939.json` | SPX 0DTE信号 | 2026-07-20 09:39 | [下载](SPXalerts/20260720/spx_0dte_20260720_0939.json) | {"signals": 84, "timestamp_et": "2026-07-20 09:39 ET"} |
| `ndx_0dte_20260720_0938.json` | NDX 0DTE信号 | 2026-07-20 09:38 | [下载](NDXalerts/20260720/ndx_0dte_20260720_0938.json) | {"signals": 4, "timestamp_et": "2026-07-20 09:38 ET"} |
| `spx_0dte_report_20260720_0937.json` | SPX 0DTE信号 | 2026-07-20 09:37 | [下载](SPXalerts/20260720/spx_0dte_report_20260720_0937.json) | {"label": "0DTE · 09:37 ET", "signals": 155, "direction": "极度偏多 🟢🟢", "net_premiu |
| `ndx_0dte_report_20260720_0936.json` | NDX 0DTE信号 | 2026-07-20 09:36 | [下载](NDXalerts/20260720/ndx_0dte_report_20260720_0936.json) | {"label": "0DTE · 09:36 ET", "signals": 8, "direction": "极度偏多 🟢🟢", "net_premium_ |
| `spx_0dte_20260720_0934.json` | SPX 0DTE信号 | 2026-07-20 09:34 | [下载](SPXalerts/20260720/spx_0dte_20260720_0934.json) | {"signals": 78, "timestamp_et": "2026-07-20 09:34 ET"} |
| `ndx_0dte_20260720_0934.json` | NDX 0DTE信号 | 2026-07-20 09:34 | [下载](NDXalerts/20260720/ndx_0dte_20260720_0934.json) | {"signals": 3, "timestamp_et": "2026-07-20 09:34 ET"} |
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-07-20 09:30 | [下载](SPXalerts/20260720/spx_gamma_latest.json) | {"ts": "09:30", "ts_full": "2026-07-20T09:30:41.382109-04:00", "symbol": "SPX",  |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-07-20 09:29 | [下载](NDXalerts/20260720/ndx_gamma_latest.json) | {"ts": "09:29", "ts_full": "2026-07-20T09:29:28.106659-04:00", "symbol": "NDX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

