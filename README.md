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
## 📅 2026-06-09

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_0dte_20260609_0938.json` | SPX 0DTE信号 | 2026-06-09 09:38 | [下载](SPXalerts/20260609/spx_0dte_20260609_0938.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_0dte_latest.json` | SPX 0DTE信号 | 2026-06-09 09:36 | [下载](SPXalerts/20260609/spx_0dte_latest.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_0dte_report_20260609_0934.json` | SPX 0DTE信号 | 2026-06-09 09:34 | [下载](SPXalerts/20260609/spx_0dte_report_20260609_0934.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_intraday_20260609_latest.json` | SPX盘中5分钟快报 | 2026-06-09 09:30 | [下载](SPXalerts/20260609/spx_intraday_20260609_latest.json) | {} |
| `alerts_20260609_0915.json` | 期权流增量快照 | 2026-06-09 09:15 | [下载](alerts/20260609/alerts_20260609_0915.json) | {} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

