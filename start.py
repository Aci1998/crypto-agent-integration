#!/usr/bin/env python3
"""
加密货币Agent集成工具启动脚本
"""

import sys
import subprocess
import time
import threading
import signal
import os

def start_price_service():
    """启动价格服务"""
    print("🚀 启动价格服务...")
    try:
        process = subprocess.Popen([sys.executable, "price_service.py"])
        return process
    except Exception as e:
        print(f"❌ 启动价格服务失败: {e}")
        return None

def start_mcp_server():
    """启动MCP服务器"""
    print("📡 启动MCP服务器...")
    try:
        process = subprocess.Popen([sys.executable, "mcp_server.py"])
        return process
    except Exception as e:
        print(f"❌ 启动MCP服务器失败: {e}")
        return None

def test_agent():
    """测试Agent功能"""
    print("🧪 运行测试...")
    try:
        result = subprocess.run([sys.executable, "test_suite.py"], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("✅ 测试通过")
        else:
            print("❌ 测试失败")
            print(result.stdout)
    except Exception as e:
        print(f"❌ 测试执行失败: {e}")

def interactive_demo():
    """交互式演示"""
    print("🤖 启动交互式演示...")
    try:
        subprocess.run([sys.executable, "crypto_agent.py"])
    except KeyboardInterrupt:
        print("\n👋 演示结束")
    except Exception as e:
        print(f"❌ 演示失败: {e}")

def show_menu():
    """显示菜单"""
    print("\n" + "=" * 50)
    print("🪙 加密货币Agent集成工具")
    print("=" * 50)
    print("1. 启动价格服务")
    print("2. 启动MCP服务器")
    print("3. 运行测试套件")
    print("4. 交互式演示")
    print("5. 生成MCP配置")
    print("6. 查看集成示例")
    print("0. 退出")
    print("=" * 50)

def generate_mcp_config():
    """生成MCP配置"""
    try:
        subprocess.run([sys.executable, "mcp_server.py", "config"])
    except Exception as e:
        print(f"❌ 生成配置失败: {e}")

def show_integration_examples():
    """显示集成示例"""
    print("\n📚 集成示例:")
    print("=" * 30)
    
    examples = [
        ("Kiro IDE集成", "examples/kiro_integration.py"),
        ("LangChain集成", "integrations/langchain_integration.py"),
        ("OpenAI集成", "integrations/openai_integration.py"),
    ]
    
    for name, path in examples:
        if os.path.exists(path):
            print(f"✅ {name}: {path}")
        else:
            print(f"❌ {name}: {path} (文件不存在)")
    
    print("\n运行示例:")
    print("python examples/kiro_integration.py")
    print("python integrations/langchain_integration.py")

def main():
    """主函数"""
    processes = []
    
    def signal_handler(sig, frame):
        print("\n🛑 正在关闭服务...")
        for process in processes:
            if process and process.poll() is None:
                process.terminate()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    while True:
        show_menu()
        
        try:
            choice = input("\n请选择操作 (0-6): ").strip()
            
            if choice == "0":
                print("👋 再见！")
                break
            
            elif choice == "1":
                process = start_price_service()
                if process:
                    processes.append(process)
                    print("✅ 价格服务已启动")
                    print("🌐 API地址: http://localhost:5000")
                    print("💊 健康检查: http://localhost:5000/health")
            
            elif choice == "2":
                process = start_mcp_server()
                if process:
                    processes.append(process)
                    print("✅ MCP服务器已启动")
            
            elif choice == "3":
                test_agent()
            
            elif choice == "4":
                interactive_demo()
            
            elif choice == "5":
                generate_mcp_config()
            
            elif choice == "6":
                show_integration_examples()
            
            else:
                print("❌ 无效选择，请重试")
            
            if choice in ["1", "2"]:
                input("\n按Enter继续...")
        
        except KeyboardInterrupt:
            print("\n👋 再见！")
            break
        except Exception as e:
            print(f"❌ 操作失败: {e}")
    
    # 清理进程
    for process in processes:
        if process and process.poll() is None:
            process.terminate()

if __name__ == "__main__":
    main()