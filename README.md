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
## 📅 2026-06-08

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_intraday_20260608_1555.json` | SPX盘中5分钟快报 | 2026-06-08 15:55 | [下载](SPXalerts/20260608/spx_intraday_20260608_1555.json) | {} |
| `spx_intraday_20260608_1550.json` | SPX盘中5分钟快报 | 2026-06-08 15:50 | [下载](SPXalerts/20260608/spx_intraday_20260608_1550.json) | {} |
| `spx_intraday_20260608_1545.json` | SPX盘中5分钟快报 | 2026-06-08 15:45 | [下载](SPXalerts/20260608/spx_intraday_20260608_1545.json) | {} |
| `alerts_20260608_1545.json` | 期权流增量快照 | 2026-06-08 15:45 | [下载](alerts/20260608/alerts_20260608_1545.json) | {} |
| `spx_intraday_20260608_1540.json` | SPX盘中5分钟快报 | 2026-06-08 15:40 | [下载](SPXalerts/20260608/spx_intraday_20260608_1540.json) | {} |
| `alerts_20260608_full.json` | 期权流全天快照 | 2026-06-08 15:30 | [下载](alerts/20260608/alerts_20260608_full.json) | {"total": 36356, "big_premium": 21559, "bull_bear": "多7909/空4777", "time_range": |
| `alerts_20260608_1530.json` | 期权流增量快照 | 2026-06-08 15:30 | [下载](alerts/20260608/alerts_20260608_1530.json) | {} |
| `spx_intraday_20260608_1520.json` | SPX盘中5分钟快报 | 2026-06-08 15:20 | [下载](SPXalerts/20260608/spx_intraday_20260608_1520.json) | {} |
| `spx_intraday_20260608_1505.json` | SPX盘中5分钟快报 | 2026-06-08 15:05 | [下载](SPXalerts/20260608/spx_intraday_20260608_1505.json) | {} |
| `alerts_20260608_1500.json` | 期权流增量快照 | 2026-06-08 15:00 | [下载](alerts/20260608/alerts_20260608_1500.json) | {} |
| `spx_intraday_20260608_latest.json` | SPX盘中5分钟快报 | 2026-06-08 14:55 | [下载](SPXalerts/20260608/spx_intraday_20260608_latest.json) | {} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

