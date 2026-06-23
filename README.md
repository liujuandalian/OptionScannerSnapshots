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
| `ndx_ndte_report_20260623_1007.json` | NDX 非0DTE信号 | 2026-06-23 10:07 | [下载](NDXalerts/20260623/ndx_ndte_report_20260623_1007.json) | {} |
| `ndx_0dte_report_20260623_1006.json` | NDX 0DTE信号 | 2026-06-23 10:06 | [下载](NDXalerts/20260623/ndx_0dte_report_20260623_1006.json) | {} |
| `spx_intraday_20260623_1005.json` | SPX盘中5分钟快报 | 2026-06-23 10:05 | [下载](SPXalerts/20260623/spx_intraday_20260623_1005.json) | {} |
| `spx_0dte_report_20260623_1004.json` | SPX 0DTE信号 | 2026-06-23 10:04 | [下载](SPXalerts/20260623/spx_0dte_report_20260623_1004.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `ndx_ndte_report_latest.json` | NDX 非0DTE信号 | 2026-06-23 10:01 | [下载](NDXalerts/20260623/ndx_ndte_report_latest.json) | {} |
| `ndx_0dte_report_latest.json` | NDX 0DTE信号 | 2026-06-23 10:00 | [下载](NDXalerts/20260623/ndx_0dte_report_latest.json) | {} |
| `spx_intraday_20260623_1000.json` | SPX盘中5分钟快报 | 2026-06-23 10:00 | [下载](SPXalerts/20260623/spx_intraday_20260623_1000.json) | {} |
| `alerts_20260623_1000.json` | 期权流增量快照 | 2026-06-23 10:00 | [下载](alerts/20260623/alerts_20260623_1000.json) | {} |
| `ndx_0dte_report_20260623_0958.json` | NDX 0DTE信号 | 2026-06-23 09:58 | [下载](NDXalerts/20260623/ndx_0dte_report_20260623_0958.json) | {} |
| `ndx_ndte_report_20260623_0956.json` | NDX 非0DTE信号 | 2026-06-23 09:56 | [下载](NDXalerts/20260623/ndx_ndte_report_20260623_0956.json) | {} |
| `spx_stock_flow_latest.json` | 个股期权流量报告 | 2026-06-23 09:56 | [下载](SPXalerts/20260623/spx_stock_flow_latest.json) | {} |
| `ndx_0dte_20260623_0955.json` | NDX 0DTE信号 | 2026-06-23 09:56 | [下载](NDXalerts/20260623/ndx_0dte_20260623_0955.json) | {} |
| `ndx_0dte_latest.json` | NDX 0DTE信号 | 2026-06-23 09:51 | [下载](NDXalerts/20260623/ndx_0dte_latest.json) | {} |
| `ndx_0dte_report_20260623_0949.json` | NDX 0DTE信号 | 2026-06-23 09:49 | [下载](NDXalerts/20260623/ndx_0dte_report_20260623_0949.json) | {} |
| `spx_0dte_report_20260623_0947.json` | SPX 0DTE信号 | 2026-06-23 09:47 | [下载](SPXalerts/20260623/spx_0dte_report_20260623_0947.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `ndx_ndte_latest.json` | NDX 非0DTE信号 | 2026-06-23 09:46 | [下载](NDXalerts/20260623/ndx_ndte_latest.json) | {} |
| `alerts_20260623_0945.json` | 期权流增量快照 | 2026-06-23 09:45 | [下载](alerts/20260623/alerts_20260623_0945.json) | {} |
| `ndx_0dte_report_20260623_0943.json` | NDX 0DTE信号 | 2026-06-23 09:43 | [下载](NDXalerts/20260623/ndx_0dte_report_20260623_0943.json) | {} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

