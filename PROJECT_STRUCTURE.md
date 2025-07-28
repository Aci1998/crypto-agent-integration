# 🏗️ 项目结构说明

## 📁 目录结构

```
crypto-agent-integration/
├── 📄 README.md                    # 项目主要说明文档
├── 📄 LICENSE                      # 开源许可证
├── 📄 requirements.txt             # Python依赖列表
├── 📄 .gitignore                   # Git忽略文件配置
├── 📄 PROJECT_STRUCTURE.md         # 项目结构说明（本文件）
├── 📄 docker-compose.yml           # Docker容器编排配置
├── 📄 Dockerfile                   # Docker镜像构建配置
│
├── 🤖 crypto_agent.py              # 核心加密货币查询Agent
├── 🌐 price_service.py             # Flask价格查询服务
├── 📡 mcp_server.py                # MCP协议服务器
├── 📡 crypto_mcp_server.py         # 加密货币专用MCP服务器
├── 🚀 start.py                     # 项目启动脚本
├── 🎮 demo.py                      # 演示脚本
├── 📋 mcp_config.json              # MCP配置文件（可选）
│
├── 📁 integrations/                # 各种框架集成
│   ├── langchain_integration.py   # LangChain集成
│   ├── openai_integration.py      # OpenAI Functions集成
│   └── xinghuo_integration.py     # 讯飞星火集成
│
├── 📁 examples/                    # 使用示例
│   └── kiro_integration.py        # Kiro IDE集成示例
│
├── 📁 test/                        # 测试文件
│   ├── test_suite.py              # 完整测试套件
│   ├── test_agent_integration.py  # Agent集成测试
│   └── test_report.json           # 测试报告（自动生成）
│
├── 📁 docs/                        # 文档目录（重命名自doce）
│   ├── AGENT_INTEGRATION_GUIDE.md # Agent集成指南
│   ├── DEPLOYMENT.md              # 部署指南
│   ├── PROJECT_SUMMARY.md         # 项目总结
│   ├── QUICK_START.md             # 快速开始指南
│   └── UPLOAD_GUIDE.md            # 上传指南
│
├── 📁 .github/                     # GitHub配置
│   └── workflows/
│       └── ci.yml                  # CI/CD配置
│
└── 📁 __pycache__/                 # Python缓存（被.gitignore忽略）
```

## 🎯 核心文件说明

### 主要组件

- **crypto_agent.py**: 核心Agent类，处理自然语言查询
- **price_service.py**: Flask Web服务，提供REST API接口
- **mcp_server.py**: MCP协议服务器，支持Kiro IDE等工具

### 集成支持

- **integrations/**: 各种AI框架的集成代码
  - LangChain工具集成
  - OpenAI Function Calling
  - 讯飞星火平台集成

### 测试和示例

- **test/**: 完整的测试套件
- **examples/**: 实际使用示例

### 文档

- **docs/**: 详细的使用和部署文档

## 🚀 快速开始

1. **安装依赖**:
   ```bash
   pip install -r requirements.txt
   ```

2. **启动服务**:
   ```bash
   python start.py
   ```

3. **运行测试**:
   ```bash
   python test/test_suite.py
   ```

## 📦 部署选项

- **本地部署**: 直接运行Python脚本
- **Docker部署**: 使用docker-compose.yml
- **云平台部署**: 参考docs/DEPLOYMENT.md

## 🔧 配置文件

- **requirements.txt**: Python依赖
- **mcp_config.json**: MCP服务器配置（可选）
- **docker-compose.yml**: Docker容器配置

## 📝 开发指南

1. 所有新功能应该包含测试
2. 文档应该与代码同步更新
3. 遵循Python PEP 8编码规范
4. 提交前运行完整测试套件

## 🤝 贡献指南

1. Fork项目
2. 创建功能分支
3. 提交更改
4. 创建Pull Request

详细信息请参考各个docs/目录下的具体文档。