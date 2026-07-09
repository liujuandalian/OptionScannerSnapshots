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
## 📅 2026-07-09

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_0dte_report_20260709_0947.json` | SPX 0DTE信号 | 2026-07-09 09:47 | [下载](SPXalerts/20260709/spx_0dte_report_20260709_0947.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `ndx_0dte_20260709_0946.json` | NDX 0DTE信号 | 2026-07-09 09:46 | [下载](NDXalerts/20260709/ndx_0dte_20260709_0946.json) | {} |
| `spx_0dte_report_20260709_0945.json` | SPX 0DTE信号 | 2026-07-09 09:45 | [下载](SPXalerts/20260709/spx_0dte_report_20260709_0945.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_0dte_20260709_0943.json` | SPX 0DTE信号 | 2026-07-09 09:43 | [下载](SPXalerts/20260709/spx_0dte_20260709_0943.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_0dte_report_20260709_0941.json` | SPX 0DTE信号 | 2026-07-09 09:41 | [下载](SPXalerts/20260709/spx_0dte_report_20260709_0941.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `ndx_ndte_report_20260709_0940.json` | NDX 非0DTE信号 | 2026-07-09 09:40 | [下载](NDXalerts/20260709/ndx_ndte_report_20260709_0940.json) | {} |
| `ndx_0dte_20260709_0940.json` | NDX 0DTE信号 | 2026-07-09 09:40 | [下载](NDXalerts/20260709/ndx_0dte_20260709_0940.json) | {} |
| `spx_intraday_20260709_0940.json` | SPX盘中5分钟快报 | 2026-07-09 09:40 | [下载](SPXalerts/20260709/spx_intraday_20260709_0940.json) | {} |
| `spx_0dte_20260709_0938.json` | SPX 0DTE信号 | 2026-07-09 09:38 | [下载](SPXalerts/20260709/spx_0dte_20260709_0938.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_0dte_report_20260709_0936.json` | SPX 0DTE信号 | 2026-07-09 09:36 | [下载](SPXalerts/20260709/spx_0dte_report_20260709_0936.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `ndx_0dte_20260709_0936.json` | NDX 0DTE信号 | 2026-07-09 09:36 | [下载](NDXalerts/20260709/ndx_0dte_20260709_0936.json) | {} |
| `spx_stock_flow_latest.json` | 个股期权流量报告 | 2026-07-09 09:35 | [下载](SPXalerts/20260709/spx_stock_flow_latest.json) | {} |
| `ndx_ndte_report_20260709_0935.json` | NDX 非0DTE信号 | 2026-07-09 09:35 | [下载](NDXalerts/20260709/ndx_ndte_report_20260709_0935.json) | {} |
| `spx_0dte_report_20260709_0932.json` | SPX 0DTE信号 | 2026-07-09 09:32 | [下载](SPXalerts/20260709/spx_0dte_report_20260709_0932.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_intraday_20260709_0930.json` | SPX盘中5分钟快报 | 2026-07-09 09:30 | [下载](SPXalerts/20260709/spx_intraday_20260709_0930.json) | {} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

