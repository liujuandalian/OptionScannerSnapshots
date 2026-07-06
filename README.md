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
## 📅 2026-07-06

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `ndx_ndte_20260706_1211.json` | NDX 非0DTE信号 | 2026-07-06 12:11 | [下载](NDXalerts/20260706/ndx_ndte_20260706_1211.json) | {} |
| `spx_intraday_20260706_1210.json` | SPX盘中5分钟快报 | 2026-07-06 12:10 | [下载](SPXalerts/20260706/spx_intraday_20260706_1210.json) | {} |
| `ndx_0dte_20260706_1208.json` | NDX 0DTE信号 | 2026-07-06 12:08 | [下载](NDXalerts/20260706/ndx_0dte_20260706_1208.json) | {} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

