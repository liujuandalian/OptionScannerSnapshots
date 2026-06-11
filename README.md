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
## 📅 2026-06-11

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_intraday_20260611_0955.json` | SPX盘中5分钟快报 | 2026-06-11 09:55 | [下载](SPXalerts/20260611/spx_intraday_20260611_0955.json) | {} |
| `spx_0dte_latest.json` | SPX 0DTE信号 | 2026-06-11 09:54 | [下载](SPXalerts/20260611/spx_0dte_latest.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_0dte_report_latest.json` | SPX 0DTE信号 | 2026-06-11 09:52 | [下载](SPXalerts/20260611/spx_0dte_report_latest.json) | {"date": null, "signals": 0, "spx_close": 0, "0dte_dir": "N/A", "0dte_net": "$0. |
| `spx_intraday_20260611_latest.json` | SPX盘中5分钟快报 | 2026-06-11 09:50 | [下载](SPXalerts/20260611/spx_intraday_20260611_latest.json) | {} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

