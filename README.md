# OptionScannerSnapshots

> Schwab Options Flow Scanner 自动快照仓库
> 由 main.py 扫描器自动同步，AI Agent 可直接读取

## 🗂️ 目录结构

```
OptionScannerSnapshots/
├── alerts/
│   └── YYYYMMDD/
│       ├── alerts_YYYYMMDD_full.json      # 全天期权流快照
│       └── alerts_YYYYMMDD_HHMM.json     # 增量快照
├── oi_snapshots/
│   └── YYYYMMDD/
│       ├── oi_pre_mkt_YYYYMMDD.json      # 盘前OI（277只）
│       ├── oi_core72_YYYYMMDD.json       # 盘后OI（72只核心）
│       └── oi_report_YYYYMMDD.json       # OI变化对比报告
└── SPXalerts/
    └── YYYYMMDD/
        ├── spx_eod_YYYYMMDD.json         # SPX盘后EOD报告
        ├── spx_eod_YYYYMMDD_0dte.json    # SPX 0DTE信号
        └── spx_intraday_YYYYMMDD_HHMM.json  # 盘中5分钟快报
```

## 🤖 AI Agent 使用说明

每个文件均附有元数据说明（见下方日期章节）。
直接读取 JSON 文件的 GitHub raw URL：
```
https://raw.githubusercontent.com/liujuandalian/OptionScannerSnapshots/main/{path}
```

---



## 📅 2026-06-06

> 本日快照文件列表，AI Agent 可直接读取下方 JSON 路径

### 📄 `test_connection.json`
- **类型**：快照文件
- **上传时间**：2026-06-06 04:25 ET
- **GitHub路径**：`SPXalerts/20260606/test_connection.json`
- **AI Agent提示**：期权扫描数据
- **内容摘要**：
  - test: `True`
  - message: `GitHub同步测试`
  - time: `2026-06-06T04:25:22.664810`
