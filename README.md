# 🤖 加密货币Agent集成工具

一个专门用于将加密货币查询功能集成到各种AI Agent系统中的工具包。

## ✨ 功能特性

- 🔍 **智能查询**：支持自然语言查询加密货币价格
- 🌐 **多框架支持**：LangChain、OpenAI Functions、MCP协议等
- 📡 **实时数据**：集成多个数据源（OKX、Binance、CoinGecko）
- 🛠️ **易于集成**：提供多种集成方式和示例代码
- 🧪 **完整测试**：包含完整的测试套件

## 🚀 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 启动价格服务
```bash
python price_service.py
```

### 3. 测试Agent功能
```bash
python crypto_agent.py
```

## 📋 集成方式

### 🎯 Kiro IDE集成 (推荐)

#### MCP协议集成
```bash
# 生成MCP配置
python mcp_server.py config

# 将配置添加到 ~/.kiro/settings/mcp.json
```

#### 直接集成
```python
from crypto_agent import query_crypto_price

# 在你的Agent中使用
result = query_crypto_price("BTC价格")
```

### 🔗 其他框架集成

- **LangChain**: 使用 `integrations/langchain_integration.py`
- **OpenAI Functions**: 使用 `integrations/openai_integration.py`
- **REST API**: 使用 `integrations/api_integration.py`
- **Webhook**: 使用 `integrations/webhook_integration.py`

## 📁 项目结构

```
crypto-agent-integration/
├── 📄 README.md                    # 项目说明
├── 🤖 crypto_agent.py             # 核心Agent类
├── 🌐 price_service.py            # 价格查询服务
├── 📡 mcp_server.py               # MCP协议服务器
├── 🧪 test_suite.py               # 测试套件
├── 📋 requirements.txt            # 依赖列表
├── 📁 integrations/               # 集成示例
│   ├── langchain_integration.py   # LangChain集成
│   ├── openai_integration.py      # OpenAI Functions集成
│   ├── api_integration.py         # REST API集成
│   └── webhook_integration.py     # Webhook集成
├── 📁 examples/                   # 使用示例
│   ├── basic_usage.py             # 基础使用
│   ├── kiro_integration.py        # Kiro IDE集成
│   └── custom_agent.py            # 自定义Agent
└── 📁 docs/                       # 文档
    ├── INTEGRATION_GUIDE.md       # 集成指南
    ├── API_REFERENCE.md           # API参考
    └── TROUBLESHOOTING.md         # 故障排除
```

## 🎯 支持的查询格式

- `"BTC价格"` → 查询比特币价格
- `"比特币多少钱"` → 查询比特币价格
- `"查询以太坊"` → 查询以太坊价格
- `"ETH/USDT交易对"` → 查询ETH/USDT价格
- `"市场概览"` → 获取主要币种概览
- `"BTC,ETH,ADA"` → 批量查询多个币种

## 🧪 测试

```bash
# 运行完整测试套件
python test_suite.py

# 测试特定集成
python test_suite.py --integration mcp
python test_suite.py --integration langchain
```

## 📖 文档

- [集成指南](docs/INTEGRATION_GUIDE.md) - 详细的集成说明
- [API参考](docs/API_REFERENCE.md) - 完整的API文档
- [故障排除](docs/TROUBLESHOOTING.md) - 常见问题解决

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License - 查看 [LICENSE](LICENSE) 文件了解详情

---

⭐ 如果这个项目对你有帮助，请给个Star支持一下！