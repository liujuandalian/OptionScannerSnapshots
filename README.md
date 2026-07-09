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
| `ndx_0dte_report_20260709_1023.json` | NDX 0DTE信号 | 2026-07-09 10:23 | [下载](NDXalerts/20260709/ndx_0dte_report_20260709_1023.json) | {} |
| `ndx_ndte_report_20260709_1022.json` | NDX 非0DTE信号 | 2026-07-09 10:22 | [下载](NDXalerts/20260709/ndx_ndte_report_20260709_1022.json) | {} |
| `spx_0dte_report_20260709_1021.json` | SPX 0DTE信号 | 2026-07-09 10:21 | [下载](SPXalerts/20260709/spx_0dte_report_20260709_1021.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_intraday_20260709_1020.json` | SPX盘中5分钟快报 | 2026-07-09 10:20 | [下载](SPXalerts/20260709/spx_intraday_20260709_1020.json) | {} |
| `ndx_0dte_report_20260709_1018.json` | NDX 0DTE信号 | 2026-07-09 10:18 | [下载](NDXalerts/20260709/ndx_0dte_report_20260709_1018.json) | {} |
| `ndx_ndte_20260709_1017.json` | NDX 非0DTE信号 | 2026-07-09 10:17 | [下载](NDXalerts/20260709/ndx_ndte_20260709_1017.json) | {} |
| `ndx_0dte_report_20260709_1016.json` | NDX 0DTE信号 | 2026-07-09 10:16 | [下载](NDXalerts/20260709/ndx_0dte_report_20260709_1016.json) | {} |
| `spx_intraday_20260709_1015.json` | SPX盘中5分钟快报 | 2026-07-09 10:15 | [下载](SPXalerts/20260709/spx_intraday_20260709_1015.json) | {} |
| `ndx_0dte_report_20260709_1014.json` | NDX 0DTE信号 | 2026-07-09 10:14 | [下载](NDXalerts/20260709/ndx_0dte_report_20260709_1014.json) | {} |
| `spx_0dte_20260709_1012.json` | SPX 0DTE信号 | 2026-07-09 10:13 | [下载](SPXalerts/20260709/spx_0dte_20260709_1012.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_0dte_report_20260709_1012.json` | SPX 0DTE信号 | 2026-07-09 10:13 | [下载](SPXalerts/20260709/spx_0dte_report_20260709_1012.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `ndx_0dte_report_20260709_1012.json` | NDX 0DTE信号 | 2026-07-09 10:12 | [下载](NDXalerts/20260709/ndx_0dte_report_20260709_1012.json) | {} |


## 📅 2026-07-08

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_ndte_20260708_1609.json` | SPX 非0DTE信号 | 2026-07-08 22:10 | [下载](SPXalerts/20260708/spx_ndte_20260708_1609.json) | {} |
| `ndx_ndte_report_20260708_2210.json` | NDX 非0DTE信号 | 2026-07-08 22:10 | [下载](NDXalerts/20260708/ndx_ndte_report_20260708_2210.json) | {} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

