#!/usr/bin/env python3
"""
讯飞星火Agent集成
支持Function Calling和插件机制
"""

import json
import requests
import sys
import os
from typing import Dict, Any, List, Optional

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crypto_agent import CryptoAgent

class XinghuoIntegration:
    """讯飞星火集成类"""
    
    def __init__(self, api_base_url: str = "http://localhost:5000"):
        self.crypto_agent = CryptoAgent(api_base_url)
        self.function_definitions = self._create_function_definitions()
    
    def _create_function_definitions(self) -> List[Dict[str, Any]]:
        """创建讯飞星火Function Calling定义"""
        return [
            {
                "name": "query_crypto_price",
                "description": "查询加密货币价格信息，支持自然语言查询",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "自然语言查询，如'BTC价格'、'比特币多少钱'、'查询以太坊'等"
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "get_market_overview",
                "description": "获取主要加密货币市场概览",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            },
            {
                "name": "batch_query_crypto",
                "description": "批量查询多个加密货币价格",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbols": {
                            "type": "string",
                            "description": "逗号分隔的货币代码，如'BTC,ETH,ADA'"
                        }
                    },
                    "required": ["symbols"]
                }
            }
        ]
    
    def get_function_definitions(self) -> List[Dict[str, Any]]:
        """获取函数定义，用于星火API调用"""
        return self.function_definitions
    
    def handle_function_call(self, function_name: str, arguments: Dict[str, Any]) -> str:
        """处理星火的函数调用"""
        try:
            if function_name == "query_crypto_price":
                query = arguments.get("query", "")
                return self.crypto_agent.process_query(query)
            
            elif function_name == "get_market_overview":
                return self.crypto_agent.get_market_overview()
            
            elif function_name == "batch_query_crypto":
                symbols = arguments.get("symbols", "")
                symbol_list = [s.strip().upper() for s in symbols.split(',')]
                return self.crypto_agent.get_multiple_prices(symbol_list)
            
            else:
                return f"❌ 未知的函数: {function_name}"
                
        except Exception as e:
            return f"❌ 函数调用失败: {str(e)}"

# 全局集成实例
xinghuo_integration = XinghuoIntegration()

def get_xinghuo_functions() -> List[Dict[str, Any]]:
    """
    获取讯飞星火Function Calling定义
    
    Returns:
        函数定义列表，可直接用于星火API调用
    """
    return xinghuo_integration.get_function_definitions()

def handle_xinghuo_function_call(function_name: str, arguments: Dict[str, Any]) -> str:
    """
    处理讯飞星火的函数调用
    
    Args:
        function_name: 函数名称
        arguments: 函数参数
    
    Returns:
        函数执行结果
    """
    return xinghuo_integration.handle_function_call(function_name, arguments)

# 讯飞星火插件格式支持
class XinghuoPlugin:
    """讯飞星火插件格式"""
    
    @staticmethod
    def get_plugin_manifest() -> Dict[str, Any]:
        """获取插件清单"""
        return {
            "name": "crypto-price-checker",
            "version": "1.0.0",
            "description": "加密货币价格查询插件",
            "author": "Crypto Agent Team",
            "functions": xinghuo_integration.get_function_definitions(),
            "permissions": ["network"],
            "categories": ["finance", "cryptocurrency", "tools"]
        }
    
    @staticmethod
    def handle_plugin_request(request: Dict[str, Any]) -> Dict[str, Any]:
        """处理插件请求"""
        try:
            function_name = request.get("function")
            arguments = request.get("arguments", {})
            
            result = xinghuo_integration.handle_function_call(function_name, arguments)
            
            return {
                "success": True,
                "result": result,
                "timestamp": "2025-07-25T10:00:00Z"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": "2025-07-25T10:00:00Z"
            }

# 示例使用代码
def demo_xinghuo_integration():
    """演示讯飞星火集成使用"""
    
    print("🌟 讯飞星火加密货币查询插件演示")
    print("=" * 50)
    
    # 1. 获取函数定义
    functions = get_xinghuo_functions()
    print("📋 可用函数:")
    for func in functions:
        print(f"  • {func['name']}: {func['description']}")
    
    print("\n🧪 测试函数调用:")
    
    # 2. 测试价格查询
    result1 = handle_xinghuo_function_call("query_crypto_price", {"query": "BTC价格"})
    print(f"\n💰 BTC价格查询结果:\n{result1}")
    
    # 3. 测试市场概览
    result2 = handle_xinghuo_function_call("get_market_overview", {})
    print(f"\n📊 市场概览:\n{result2}")
    
    # 4. 测试批量查询
    result3 = handle_xinghuo_function_call("batch_query_crypto", {"symbols": "BTC,ETH,ADA"})
    print(f"\n📈 批量查询结果:\n{result3}")
    
    # 5. 插件格式演示
    plugin_manifest = XinghuoPlugin.get_plugin_manifest()
    print(f"\n🔌 插件清单:\n{json.dumps(plugin_manifest, indent=2, ensure_ascii=False)}")

if __name__ == "__main__":
    demo_xinghuo_integration()