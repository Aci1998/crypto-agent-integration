"""
Kiro IDE集成示例
演示如何在Kiro IDE中使用加密货币查询功能
"""

import sys
import os

# 添加父目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crypto_agent import query_crypto_price, get_crypto_market_overview, batch_query_crypto

def kiro_crypto_assistant(user_input: str) -> str:
    """
    Kiro IDE中的加密货币助手函数
    
    Args:
        user_input: 用户输入的查询内容
    
    Returns:
        格式化的响应内容
    """
    user_input = user_input.strip().lower()
    
    # 判断查询类型
    if any(keyword in user_input for keyword in ['市场', 'market', '概览', 'overview']):
        return get_crypto_market_overview()
    
    elif ',' in user_input and not any(word in user_input for word in ['价格', '多少', '查询']):
        # 批量查询格式：BTC,ETH,ADA
        return batch_query_crypto(user_input.upper())
    
    else:
        # 普通价格查询
        return query_crypto_price(user_input)

def demo_kiro_integration():
    """演示Kiro集成"""
    print("🎯 Kiro IDE集成演示")
    print("=" * 40)
    
    # 模拟用户查询
    test_queries = [
        "BTC价格",
        "比特币多少钱",
        "查询以太坊",
        "市场概览",
        "BTC,ETH,ADA"
    ]
    
    for query in test_queries:
        print(f"\n👤 用户: {query}")
        response = kiro_crypto_assistant(query)
        print(f"🤖 Kiro: {response}")
        print("-" * 40)

# Kiro IDE可以直接调用的函数
def get_crypto_price_for_kiro(symbol: str) -> str:
    """
    专门为Kiro IDE设计的简化接口
    
    Args:
        symbol: 货币代码，如 BTC, ETH, ADA
    
    Returns:
        简洁的价格信息
    """
    result = query_crypto_price(symbol)
    
    # 提取关键信息，返回更简洁的格式
    if "❌" in result:
        return result
    
    # 简化输出格式
    lines = result.split('\n')
    price_line = next((line for line in lines if '当前价格' in line), '')
    change_line = next((line for line in lines if '24小时涨跌' in line), '')
    
    if price_line and change_line:
        return f"{symbol} {price_line.split('**')[1]} {change_line.split('**')[1]}"
    
    return result

def setup_kiro_mcp():
    """设置Kiro MCP配置的说明"""
    print("📋 Kiro IDE MCP配置设置")
    print("=" * 40)
    
    config_content = '''
{
  "mcpServers": {
    "crypto-price-checker": {
      "command": "python",
      "args": ["mcp_server.py"],
      "env": {},
      "disabled": false,
      "autoApprove": [
        "query_crypto_price",
        "get_market_overview",
        "batch_query_crypto"
      ]
    }
  }
}
'''
    
    print("1. 将以下配置添加到 ~/.kiro/settings/mcp.json:")
    print(config_content)
    
    print("\n2. 或者运行以下命令生成配置文件:")
    print("   python mcp_server.py config")
    
    print("\n3. 在Kiro中使用:")
    print("   用户: 查询BTC价格")
    print("   Kiro: [自动调用 query_crypto_price 工具]")

if __name__ == "__main__":
    demo_kiro_integration()
    print("\n" + "=" * 50)
    setup_kiro_mcp()