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
## 📅 2026-06-26

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `ndx_0dte_20260626_1033.json` | NDX 0DTE信号 | 2026-06-26 10:33 | [下载](NDXalerts/20260626/ndx_0dte_20260626_1033.json) | {} |
| `ndx_0dte_20260626_1030.json` | NDX 0DTE信号 | 2026-06-26 10:30 | [下载](NDXalerts/20260626/ndx_0dte_20260626_1030.json) | {} |
| `alerts_20260626_1030.json` | 期权流增量快照 | 2026-06-26 10:30 | [下载](alerts/20260626/alerts_20260626_1030.json) | {} |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

