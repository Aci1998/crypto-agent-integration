"""
OpenAI Function Calling集成示例
"""

import json
import sys
import os

# 添加父目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crypto_agent import CryptoAgent

def get_openai_function_schema():
    """获取OpenAI Function Calling的schema"""
    return {
        "name": "query_crypto_price",
        "description": "查询加密货币的实时价格信息",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "加密货币代码，如BTC、ETH、ADA等"
                },
                "query_type": {
                    "type": "string",
                    "enum": ["price", "overview", "batch"],
                    "description": "查询类型：price(单个价格)、overview(市场概览)、batch(批量查询)"
                }
            },
            "required": ["symbol"]
        }
    }

def handle_openai_function_call(function_call: dict) -> str:
    """处理OpenAI Function Calling"""
    crypto_agent = CryptoAgent()
    
    try:
        args = json.loads(function_call.get("arguments", "{}"))
        symbol = args.get("symbol", "")
        query_type = args.get("query_type", "price")
        
        if query_type == "overview":
            return crypto_agent.get_market_overview()
        elif query_type == "batch":
            symbols = symbol.split(",")
            return crypto_agent.get_multiple_prices(symbols)
        else:
            return crypto_agent.process_query(symbol)
            
    except Exception as e:
        return f"❌ 处理函数调用时出错: {str(e)}"

def openai_integration_example():
    """OpenAI集成示例"""
    try:
        import openai
        
        print("🤖 OpenAI Function Calling集成示例")
        print("=" * 40)
        
        # 获取函数schema
        function_schema = get_openai_function_schema()
        print("✅ 函数schema创建成功")
        print(f"📋 Schema: {json.dumps(function_schema, indent=2, ensure_ascii=False)}")
        
        # 模拟函数调用
        mock_function_call = {
            "arguments": json.dumps({"symbol": "BTC", "query_type": "price"})
        }
        
        result = handle_openai_function_call(mock_function_call)
        print(f"\n🧪 模拟调用结果:\n{result}")
        
        # 如果有OpenAI API密钥，可以进行真实调用
        try:
            # 这里需要设置你的OpenAI API密钥
            # openai.api_key = "your-api-key-here"
            
            messages = [
                {"role": "user", "content": "请告诉我比特币的当前价格"}
            ]
            
            # 注意：这需要有效的OpenAI API密钥
            # response = openai.ChatCompletion.create(
            #     model="gpt-3.5-turbo",
            #     messages=messages,
            #     functions=[function_schema],
            #     function_call="auto"
            # )
            
            print("💡 要进行真实的OpenAI调用，请设置API密钥并取消注释相关代码")
            
        except Exception as e:
            print(f"⚠️  OpenAI调用需要API密钥: {e}")
        
    except ImportError:
        print("❌ OpenAI库未安装，请运行: pip install openai")

if __name__ == "__main__":
    openai_integration_example()