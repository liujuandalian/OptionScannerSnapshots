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
## 📅 2026-06-23

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `ndx_0dte_report_20260623_1329.json` | NDX 0DTE信号 | 2026-06-23 13:29 | [下载](NDXalerts/20260623/ndx_0dte_report_20260623_1329.json) | {} |
| `spx_stock_flow_latest.json` | 个股期权流量报告 | 2026-06-23 13:27 | [下载](SPXalerts/20260623/spx_stock_flow_latest.json) | {} |
| `ndx_0dte_report_20260623_1327.json` | NDX 0DTE信号 | 2026-06-23 13:27 | [下载](NDXalerts/20260623/ndx_0dte_report_20260623_1327.json) | {} |
| `spx_intraday_20260623_1325.json` | SPX盘中5分钟快报 | 2026-06-23 13:25 | [下载](SPXalerts/20260623/spx_intraday_20260623_1325.json) | {} |
| `spx_ndte_report_20260623_1324.json` | SPX 非0DTE信号 | 2026-06-23 13:24 | [下载](SPXalerts/20260623/spx_ndte_report_20260623_1324.json) | {} |
| `ndx_0dte_20260623_1323.json` | NDX 0DTE信号 | 2026-06-23 13:23 | [下载](NDXalerts/20260623/ndx_0dte_20260623_1323.json) | {} |
| `spx_0dte_report_20260623_1321.json` | SPX 0DTE信号 | 2026-06-23 13:21 | [下载](SPXalerts/20260623/spx_0dte_report_20260623_1321.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `ndx_0dte_report_latest.json` | NDX 0DTE信号 | 2026-06-23 13:20 | [下载](NDXalerts/20260623/ndx_0dte_report_latest.json) | {} |
| `spx_0dte_report_20260623_1319.json` | SPX 0DTE信号 | 2026-06-23 13:19 | [下载](SPXalerts/20260623/spx_0dte_report_20260623_1319.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `ndx_0dte_20260623_1318.json` | NDX 0DTE信号 | 2026-06-23 13:18 | [下载](NDXalerts/20260623/ndx_0dte_20260623_1318.json) | {} |
| `ndx_ndte_report_latest.json` | NDX 非0DTE信号 | 2026-06-23 13:17 | [下载](NDXalerts/20260623/ndx_ndte_report_latest.json) | {} |
| `ndx_0dte_latest.json` | NDX 0DTE信号 | 2026-06-23 13:16 | [下载](NDXalerts/20260623/ndx_0dte_latest.json) | {} |
| `spx_0dte_report_20260623_1313.json` | SPX 0DTE信号 | 2026-06-23 13:13 | [下载](SPXalerts/20260623/spx_0dte_report_20260623_1313.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `ndx_0dte_20260623_1312.json` | NDX 0DTE信号 | 2026-06-23 13:12 | [下载](NDXalerts/20260623/ndx_0dte_20260623_1312.json) | {} |
| `ndx_0dte_20260623_1306.json` | NDX 0DTE信号 | 2026-06-23 13:06 | [下载](NDXalerts/20260623/ndx_0dte_20260623_1306.json) | {} |
| `ndx_0dte_20260623_1258.json` | NDX 0DTE信号 | 2026-06-23 12:58 | [下载](NDXalerts/20260623/ndx_0dte_20260623_1258.json) | {} |
| `ndx_ndte_report_20260623_1247.json` | NDX 非0DTE信号 | 2026-06-23 12:47 | [下载](NDXalerts/20260623/ndx_ndte_report_20260623_1247.json) | {} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

