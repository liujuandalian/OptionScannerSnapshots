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
## 📅 2026-06-22

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_intraday_20260622_1330.json` | SPX盘中5分钟快报 | 2026-06-22 13:30 | [下载](SPXalerts/20260622/spx_intraday_20260622_1330.json) | {} |
| `ndx_ndte_report_20260622_1329.json` | NDX 非0DTE信号 | 2026-06-22 13:29 | [下载](NDXalerts/20260622/ndx_ndte_report_20260622_1329.json) | {} |
| `spx_stock_flow_latest.json` | 快照 | 2026-06-22 13:29 | [下载](misc/20260622/spx_stock_flow_latest.json) | {} |
| `ndx_0dte_20260622_1329.json` | NDX 0DTE信号 | 2026-06-22 13:29 | [下载](NDXalerts/20260622/ndx_0dte_20260622_1329.json) | {} |
| `spx_0dte_20260622_1329.json` | SPX 0DTE信号 | 2026-06-22 13:29 | [下载](SPXalerts/20260622/spx_0dte_20260622_1329.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `ndx_0dte_report_20260622_1327.json` | NDX 0DTE信号 | 2026-06-22 13:27 | [下载](NDXalerts/20260622/ndx_0dte_report_20260622_1327.json) | {} |
| `spx_0dte_report_20260622_1326.json` | SPX 0DTE信号 | 2026-06-22 13:26 | [下载](SPXalerts/20260622/spx_0dte_report_20260622_1326.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `ndx_0dte_20260622_1325.json` | NDX 0DTE信号 | 2026-06-22 13:25 | [下载](NDXalerts/20260622/ndx_0dte_20260622_1325.json) | {} |
| `spx_0dte_report_20260622_1322.json` | SPX 0DTE信号 | 2026-06-22 13:22 | [下载](SPXalerts/20260622/spx_0dte_report_20260622_1322.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `ndx_0dte_report_20260622_1320.json` | NDX 0DTE信号 | 2026-06-22 13:20 | [下载](NDXalerts/20260622/ndx_0dte_report_20260622_1320.json) | {} |
| `spx_intraday_20260622_latest.json` | SPX盘中5分钟快报 | 2026-06-22 13:20 | [下载](SPXalerts/20260622/spx_intraday_20260622_latest.json) | {} |
| `ndx_ndte_report_20260622_1319.json` | NDX 非0DTE信号 | 2026-06-22 13:19 | [下载](NDXalerts/20260622/ndx_ndte_report_20260622_1319.json) | {} |
| `spx_0dte_report_latest.json` | SPX 0DTE信号 | 2026-06-22 13:18 | [下载](SPXalerts/20260622/spx_0dte_report_latest.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_0dte_latest.json` | SPX 0DTE信号 | 2026-06-22 13:16 | [下载](SPXalerts/20260622/spx_0dte_latest.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_intraday_20260622_1315.json` | SPX盘中5分钟快报 | 2026-06-22 13:15 | [下载](SPXalerts/20260622/spx_intraday_20260622_1315.json) | {} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

