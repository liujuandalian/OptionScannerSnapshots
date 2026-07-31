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
## 📅 2026-07-31

| 文件 | 类型 | 上传时间 | 链接 | 摘要 |
|---|---|---|---|---|
| `spx_gamma_latest.json` | SPX GammaTracker快照 | 2026-07-31 13:55 | [下载](SPXalerts/20260731/spx_gamma_latest.json) | {"ts": "13:55", "ts_full": "2026-07-31T13:55:30.872274-04:00", "symbol": "SPX",  |
| `ndx_gamma_latest.json` | NDX GammaTracker快照 | 2026-07-31 13:54 | [下载](NDXalerts/20260731/ndx_gamma_latest.json) | {"ts": "13:54", "ts_full": "2026-07-31T13:54:14.627898-04:00", "symbol": "NDX",  |

---|------|---------|
| `alerts/YYYYMMDD/` | 期权流快照（Append模式，持续追加） | main.py 每15分钟 |
| `oi_snapshots/YYYYMMDD/` | OI盘前/盘后快照 | 盘前自动 + 盘后手动 |
| `SPXalerts/YYYYMMDD/` | SPX EOD报告 + 盘中快报 | 16:15自动 + 每5分钟 |
| `data/latest.json` | 各类型最新文件索引 | 每次同步自动更新 |

---

