# 🚀 快速开始指南

## 📦 安装

1. **克隆或下载项目**
```bash
# 如果是从GitHub克隆
git clone https://github.com/your-username/crypto-agent-integration.git
cd crypto-agent-integration

# 或者直接复制文件到新目录
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

## ⚡ 5分钟快速体验

### 方法1: 使用启动脚本 (推荐)
```bash
python start.py
```
然后按照菜单提示操作：
- 选择 `1` 启动价格服务
- 选择 `3` 运行测试
- 选择 `4` 体验交互式查询

### 方法2: 手动启动
```bash
# 终端1: 启动价格服务
python price_service.py

# 终端2: 测试Agent
python crypto_agent.py
```

## 🎯 Kiro IDE集成

### 1. 生成MCP配置
```bash
python mcp_server.py config
```

### 2. 添加到Kiro配置
将生成的 `mcp_config.json` 内容添加到 `~/.kiro/settings/mcp.json`

### 3. 在Kiro中使用
```
用户: 查询BTC价格
Kiro: [自动调用工具获取价格信息]
```

## 🧪 测试验证

```bash
# 运行完整测试套件
python test_suite.py

# 查看测试报告
cat test_report.json
```

## 💡 使用示例

### 基础查询
```python
from crypto_agent import query_crypto_price

# 查询比特币价格
result = query_crypto_price("BTC价格")
print(result)
```

### 批量查询
```python
from crypto_agent import batch_query_crypto

# 批量查询多个币种
result = batch_query_crypto("BTC,ETH,ADA")
print(result)
```

### 市场概览
```python
from crypto_agent import get_crypto_market_overview

# 获取市场概览
result = get_crypto_market_overview()
print(result)
```

## 🔧 自定义配置

### 修改API地址
在 `crypto_agent.py` 中修改：
```python
crypto_agent = CryptoAgent(api_base_url="http://your-server:5000")
```

### 添加新的货币支持
在 `price_service.py` 的 `common_pairs` 中添加：
```python
common_pairs = {
    'BTC': 'BTC/USDT',
    'YOUR_COIN': 'YOUR_COIN/USDT',  # 添加新币种
    # ...
}
```

## 📚 更多集成方式

- **LangChain**: `python integrations/langchain_integration.py`
- **OpenAI Functions**: `python integrations/openai_integration.py`
- **Kiro IDE**: `python examples/kiro_integration.py`

## ❓ 常见问题

**Q: 连接失败怎么办？**
A: 确保价格服务正在运行 (`python price_service.py`)

**Q: 查询结果为空？**
A: 检查网络连接和货币代码是否正确

**Q: MCP服务器无响应？**
A: 检查Python路径和依赖是否正确安装

## 📖 完整文档

- [README.md](README.md) - 项目概述
- [集成指南](docs/INTEGRATION_GUIDE.md) - 详细集成说明
- [API参考](docs/API_REFERENCE.md) - 完整API文档

---
