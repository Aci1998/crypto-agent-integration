#!/usr/bin/env python3
"""
加密货币Agent集成工具包演示脚本
展示各种集成方式和功能
"""

import time
import json
import asyncio
from typing import Dict, Any

def print_header(title: str):
    """打印标题"""
    print("\n" + "=" * 60)
    print(f"🎯 {title}")
    print("=" * 60)

def print_step(step: str, description: str = ""):
    """打印步骤"""
    print(f"\n📋 {step}")
    if description:
        print(f"   {description}")

def demo_basic_agent():
    """演示基础Agent功能"""
    print_header("基础Agent功能演示")
    
    try:
        from crypto_agent import crypto_agent
        
        print_step("1. 单个货币查询", "查询BTC价格")
        result = crypto_agent.process_query("BTC价格")
        print(f"结果:\n{result}")
        
        print_step("2. 自然语言查询", "使用中文查询")
        result = crypto_agent.process_query("比特币多少钱")
        print(f"结果:\n{result}")
        
        print_step("3. 市场概览", "获取主要币种概览")
        result = crypto_agent.get_market_overview()
        print(f"结果:\n{result}")
        
        print_step("4. 批量查询", "查询多个币种")
        result = crypto_agent.get_multiple_prices(['BTC', 'ETH', 'ADA'])
        print(f"结果:\n{result}")
        
        return True
        
    except Exception as e:
        print(f"❌ 基础Agent演示失败: {e}")
        return False

def demo_integrations():
    """演示集成功能"""
    print_header("集成功能演示")
    
    try:
        from agent_integrations import CryptoAgentPlugin, handle_openai_function_call
        
        print_step("1. 自定义插件", "创建并使用自定义插件")
        plugin = CryptoAgentPlugin()
        
        # 显示插件能力
        capabilities = plugin.get_capabilities()
        print("插件能力:")
        for cap in capabilities:
            print(f"  • {cap['name']}: {cap['description']}")
        
        # 执行插件功能
        result = plugin.execute("query_price", symbol="ETH")
        print(f"插件执行结果:\n{result}")
        
        print_step("2. OpenAI Function Calling", "模拟OpenAI函数调用")
        function_call = {
            "arguments": json.dumps({"symbol": "SOL", "query_type": "price"})
        }
        result = handle_openai_function_call(function_call)
        print(f"函数调用结果:\n{result}")
        
        return True
        
    except Exception as e:
        print(f"❌ 集成功能演示失败: {e}")
        return False

def demo_mcp_server():
    """演示MCP服务器功能"""
    print_header("MCP服务器演示")
    
    try:
        print_step("1. MCP配置生成", "生成Kiro IDE配置")
        
        # 模拟MCP配置
        mcp_config = {
            "mcpServers": {
                "crypto-price-checker": {
                    "command": "python",
                    "args": ["mcp_server.py"],
                    "env": {},
                    "disabled": False,
                    "autoApprove": [
                        "query_crypto_price",
                        "get_market_overview",
                        "batch_query_crypto"
                    ]
                }
            }
        }
        
        print("MCP配置示例:")
        print(json.dumps(mcp_config, indent=2, ensure_ascii=False))
        
        print_step("2. MCP工具列表", "可用的MCP工具")
        tools = [
            {
                "name": "query_crypto_price",
                "description": "查询加密货币价格信息"
            },
            {
                "name": "get_market_overview", 
                "description": "获取主要加密货币市场概览"
            },
            {
                "name": "batch_query_crypto",
                "description": "批量查询多个加密货币价格"
            }
        ]
        
        for tool in tools:
            print(f"  • {tool['name']}: {tool['description']}")
        
        return True
        
    except Exception as e:
        print(f"❌ MCP服务器演示失败: {e}")
        return False

def demo_natural_language():
    """演示自然语言处理"""
    print_header("自然语言处理演示")
    
    try:
        from crypto_agent import crypto_agent
        
        test_queries = [
            "BTC价格",
            "比特币多少钱",
            "查询以太坊",
            "告诉我SOL的价格",
            "ETH/USDT交易对",
            "市场概览",
            "bitcoin price"
        ]
        
        print_step("自然语言查询测试", f"测试 {len(test_queries)} 种查询格式")
        
        for i, query in enumerate(test_queries, 1):
            print(f"\n{i}. 查询: '{query}'")
            result = crypto_agent.process_query(query)
            
            # 简化输出，只显示关键信息
            if "BTC" in result or "ETH" in result or "SOL" in result:
                lines = result.split('\n')
                key_lines = [line for line in lines if any(keyword in line for keyword in ['当前价格', '24小时涨跌', '数据源'])]
                if key_lines:
                    print("   " + " | ".join(key_lines[:3]))
                else:
                    print("   ✅ 查询成功")
            elif result.startswith("❓"):
                print("   ❌ 未识别查询")
            else:
                print("   ✅ 查询成功")
        
        return True
        
    except Exception as e:
        print(f"❌ 自然语言处理演示失败: {e}")
        return False

def demo_performance():
    """演示性能测试"""
    print_header("性能测试演示")
    
    try:
        from crypto_agent import crypto_agent
        
        print_step("1. 响应时间测试", "测试单次查询响应时间")
        
        start_time = time.time()
        result = crypto_agent.process_query("BTC")
        end_time = time.time()
        
        response_time = (end_time - start_time) * 1000  # 转换为毫秒
        print(f"响应时间: {response_time:.2f}ms")
        
        print_step("2. 并发测试", "模拟多个并发查询")
        
        queries = ["BTC", "ETH", "ADA", "SOL", "BNB"]
        start_time = time.time()
        
        results = []
        for query in queries:
            result = crypto_agent.process_query(query)
            results.append(len(result) > 0)
        
        end_time = time.time()
        total_time = (end_time - start_time) * 1000
        
        success_rate = sum(results) / len(results) * 100
        print(f"总耗时: {total_time:.2f}ms")
        print(f"成功率: {success_rate:.1f}%")
        print(f"平均响应时间: {total_time/len(queries):.2f}ms")
        
        return True
        
    except Exception as e:
        print(f"❌ 性能测试演示失败: {e}")
        return False

def demo_error_handling():
    """演示错误处理"""
    print_header("错误处理演示")
    
    try:
        from crypto_agent import crypto_agent
        
        test_cases = [
            ("", "空查询"),
            ("INVALID_COIN", "无效币种"),
            ("OKX", "交易所名称"),
            ("123", "数字输入"),
            ("价格", "仅关键词")
        ]
        
        print_step("错误处理测试", "测试各种异常输入")
        
        for query, description in test_cases:
            print(f"\n测试: {description} ('{query}')")
            result = crypto_agent.process_query(query)
            
            if result.startswith("❓") or "错误" in result or "异常" in result:
                print("   ✅ 错误处理正确")
            else:
                print("   ⚠️  可能的误判")
        
        return True
        
    except Exception as e:
        print(f"❌ 错误处理演示失败: {e}")
        return False

def main():
    """主演示函数"""
    print("🎬 加密货币Agent集成工具包 - 功能演示")
    print("=" * 60)
    print("本演示将展示工具包的各种功能和集成方式")
    
    demos = [
        ("基础Agent功能", demo_basic_agent),
        ("集成功能", demo_integrations),
        ("MCP服务器", demo_mcp_server),
        ("自然语言处理", demo_natural_language),
        ("性能测试", demo_performance),
        ("错误处理", demo_error_handling)
    ]
    
    results = []
    
    for name, demo_func in demos:
        try:
            print(f"\n⏳ 开始演示: {name}")
            success = demo_func()
            results.append((name, success))
            
            if success:
                print(f"✅ {name} 演示完成")
            else:
                print(f"❌ {name} 演示失败")
                
        except KeyboardInterrupt:
            print(f"\n⏹️  演示被用户中断")
            break
        except Exception as e:
            print(f"❌ {name} 演示异常: {e}")
            results.append((name, False))
    
    # 显示总结
    print_header("演示总结")
    
    total = len(results)
    passed = sum(1 for _, success in results if success)
    
    print(f"📊 演示结果: {passed}/{total} 成功")
    
    for name, success in results:
        status = "✅" if success else "❌"
        print(f"  {status} {name}")
    
    if passed == total:
        print("\n🎉 所有演示都成功完成！")
        print("\n🚀 快速开始:")
        print("1. 启动服务: python start.py")
        print("2. 测试功能: python test_suite.py")
        print("3. 查看文档: README.md")
    else:
        print(f"\n⚠️  {total - passed} 个演示失败")
        print("请检查相关配置和依赖")
    
    print("\n📖 更多信息:")
    print("• 集成指南: AGENT_INTEGRATION_GUIDE.md")
    print("• 部署指南: DEPLOYMENT.md")
    print("• API参考: docs/API_REFERENCE.md")

if __name__ == "__main__":
    main()