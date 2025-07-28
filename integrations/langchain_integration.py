"""
LangChain集成示例
"""

from typing import Optional
import sys
import os
from langchain.tools import Tool

# 添加父目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crypto_agent import CryptoAgent

def create_langchain_tool():
    """创建LangChain工具"""
    try: 
        
        crypto_agent = CryptoAgent()
        
        def crypto_price_tool(query: str) -> str:
            """LangChain工具函数"""
            return crypto_agent.process_query(query)
        
        crypto_tool = Tool(
            name="CryptoPriceChecker",
            description="查询加密货币价格信息。输入货币代码或自然语言查询，如'BTC价格'、'比特币多少钱'等",
            func=crypto_price_tool
        )
        
        return crypto_tool
        
    except ImportError:
        print("❌ LangChain未安装，请运行: pip install langchain")
        return None

def create_langchain_agent():
    """创建完整的LangChain Agent"""
    try:
        from langchain.agents import initialize_agent, AgentType
        from langchain.llms import OpenAI
        
        # 创建工具
        crypto_tool = create_langchain_tool()
        if not crypto_tool:
            return None
        
        # 创建LLM（需要OpenAI API密钥）
        llm = OpenAI(temperature=0)
        
        # 创建Agent
        agent = initialize_agent(
            tools=[crypto_tool],
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )
        
        return agent
        
    except ImportError as e:
        print(f"❌ 依赖未安装: {e}")
        return None
    except Exception as e:
        print(f"❌ 创建Agent失败: {e}")
        return None

def langchain_example():
    """LangChain使用示例"""
    print("🔗 LangChain集成示例")
    print("=" * 40)
    
    # 创建工具
    tool = create_langchain_tool()
    if tool:
        print("✅ LangChain工具创建成功")
        
        # 测试工具
        result = tool.run("BTC价格")
        print(f"🧪 测试结果:\n{result}")
        
        # 尝试创建完整Agent
        agent = create_langchain_agent()
        if agent:
            print("✅ LangChain Agent创建成功")
            
            # 测试Agent
            try:
                response = agent.run("告诉我比特币的当前价格")
                print(f"🤖 Agent响应:\n{response}")
            except Exception as e:
                print(f"❌ Agent执行失败: {e}")
        else:
            print("❌ LangChain Agent创建失败（可能缺少OpenAI API密钥）")
    else:
        print("❌ LangChain工具创建失败")

if __name__ == "__main__":
    langchain_example()