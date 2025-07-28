# 🤖 加密货币Agent集成工具

一个专门用于将加密货币查询功能集成到各种AI Agent系统中的完整工具包。

## ✨ 功能特性

- 🔍 **智能查询**：支持自然语言查询加密货币价格
- 🌐 **多框架支持**：LangChain、OpenAI Functions、MCP协议、讯飞星火等
- 📡 **实时数据**：集成多个数据源（OKX、Binance、CoinGecko）
- 🛠️ **易于集成**：提供多种集成方式和示例代码
- 🧪 **完整测试**：包含完整的测试套件和验证工具
- 🐳 **容器化部署**：支持Docker和docker-compose部署

## 🚀 快速开始

### 方式一：使用启动脚本（推荐）
```bash
# 安装依赖并启动所有服务
python start.py
```

### 方式二：手动启动
```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 启动价格服务
python price_service.py

# 3. 测试Agent功能
python crypto_agent.py
```

### 方式三：Docker部署
```bash
# 使用Docker Compose
docker-compose up -d
```

## 📋 支持的集成平台

### 🎯 主流AI平台
- **Kiro IDE** - MCP协议集成（推荐）
- **讯飞星火** - 工作流集成
- **LangChain** - 工具链集成
- **OpenAI** - Function Calling集成

### 🔗 集成方式

#### Kiro IDE集成
```bash
# 生成MCP配置
python mcp_server.py config

# 将配置添加到 ~/.kiro/settings/mcp.json
```

#### 讯飞星火集成
```python
# 使用工作流YAML文件
# 参考 temp/ 目录中的示例文件
```

#### 直接Python集成
```python
from crypto_agent import query_crypto_price

# 在你的Agent中使用
result = query_crypto_price("BTC价格")
print(result)
```

## 📁 项目结构

```
crypto-agent-integration/
├── 📄 README.md                    # 项目主要说明
├── 📄 PROJECT_STRUCTURE.md         # 详细项目结构说明
├── 📄 LICENSE                      # MIT开源许可证
├── 📄 requirements.txt             # Python依赖列表
├── 📄 .gitignore                   # Git忽略文件配置
├── 📄 docker-compose.yml           # Docker容器编排
├── 📄 Dockerfile                   # Docker镜像构建
│
├── 🤖 crypto_agent.py              # 核心加密货币查询Agent
├── 🌐 price_service.py             # Flask价格查询Web服务
├── 📡 mcp_server.py                # MCP协议服务器
├── 📡 crypto_mcp_server.py         # 加密货币专用MCP服务器
├── 🚀 start.py                     # 项目一键启动脚本
├── 🎮 demo.py                      # 功能演示脚本
│
├── 📁 integrations/                # 各种框架集成代码
│   ├── langchain_integration.py   # LangChain工具集成
│   ├── openai_integration.py      # OpenAI Functions集成
│   └── xinghuo_integration.py     # 讯飞星火平台集成
│
├── 📁 examples/                    # 实际使用示例
│   └── kiro_integration.py        # Kiro IDE集成示例
│
├── 📁 test/                        # 测试文件目录
│   ├── test_suite.py              # 完整测试套件
│   └── test_agent_integration.py  # Agent集成测试
│
├── 📁 docs/                        # 详细文档
│   ├── AGENT_INTEGRATION_GUIDE.md # Agent集成指南
│   ├── DEPLOYMENT.md              # 部署指南
│   ├── PROJECT_SUMMARY.md         # 项目总结
│   └── QUICK_START.md             # 快速开始指南
│
├── 📁 scripts/                     # 维护脚本
│   └── cleanup_project.py         # 项目清理脚本
│
├── 📁 temp/                        # 临时文件（开发测试用）
└── 📁 logs/                        # 日志文件目录
```

## 🎯 支持的查询格式

### 中文查询
- `"BTC价格"` / `"比特币价格"`
- `"以太坊多少钱"`
- `"查询SOL"`
- `"告诉我ADA的价格"`
- `"市场概览"`

### 英文查询
- `"BTC price"`
- `"What's Bitcoin price?"`
- `"Check ETH"`
- `"Market overview"`

### 交易对格式
- `"BTC/USDT"`
- `"ETH/USDT"`
- `"OP/USDT"`

### 批量查询
- `"BTC,ETH,ADA"`
- `"查询BTC,SOL,OP"`

## 🧪 测试和验证

### 运行完整测试套件
```bash
python test/test_suite.py
```

### 运行集成测试
```bash
python test/test_agent_integration.py
```

### 验证特定平台集成
```bash
# 测试讯飞星火集成
python integrations/xinghuo_integration.py

# 测试LangChain集成
python integrations/langchain_integration.py
```

## 🌐 支持的加密货币

**主要币种**: BTC, ETH, BNB, ADA, SOL, DOGE, XRP, LTC, LINK, DOT, UNI, ATOM

**新兴币种**: OP, ARB, MATIC, AVAX, NEAR, FTM, ALGO, VET, ICP, SHIB

**中文名称**: 比特币, 以太坊, 艾达币, 索拉纳, 币安币, 狗狗币等

## 📖 详细文档

- [项目结构说明](PROJECT_STRUCTURE.md) - 完整的项目结构文档
- [集成指南](docs/AGENT_INTEGRATION_GUIDE.md) - 详细的集成说明
- [部署指南](docs/DEPLOYMENT.md) - 生产环境部署
- [快速开始](docs/QUICK_START.md) - 新手入门指南

## 🔧 开发和维护

### 项目清理
```bash
python scripts/cleanup_project.py
```

### 代码规范
- 遵循Python PEP 8编码规范
- 所有新功能需要包含测试
- 文档与代码同步更新

## 🤝 贡献指南

1. Fork项目到你的GitHub
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

## 📞 技术支持

- 📧 提交Issue获取帮助
- 📚 查看docs/目录获取详细文档
- 🧪 运行test/目录中的测试验证功能

## 📄 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

⭐ **如果这个项目对你有帮助，请给个Star支持一下！**

🚀 **快速体验**: `python start.py` 一键启动所有服务