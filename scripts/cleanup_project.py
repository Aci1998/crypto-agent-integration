#!/usr/bin/env python3
"""
项目清理脚本
用于清理临时文件、重组项目结构
"""

import os
import shutil
import glob
from pathlib import Path

def create_directories():
    """创建标准目录结构"""
    directories = [
        'scripts',
        'docs',
        'examples', 
        'integrations',
        'test',
        'temp',
        'logs'
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ 确保目录存在: {directory}/")

def move_test_files():
    """移动测试文件到test目录"""
    test_patterns = [
        '*test*.py',
        '*_test.py',
        'test_*.py'
    ]
    
    moved_files = []
    for pattern in test_patterns:
        for file in glob.glob(pattern):
            if not file.startswith('test/'):
                dest = f"test/{os.path.basename(file)}"
                if os.path.exists(file) and not os.path.exists(dest):
                    shutil.move(file, dest)
                    moved_files.append(f"{file} -> {dest}")
    
    if moved_files:
        print("📁 移动测试文件:")
        for move in moved_files:
            print(f"   {move}")

def move_temp_files():
    """移动临时文件到temp目录"""
    temp_patterns = [
        '*_temp*.py',
        '*_简化版*.yml',
        '*_测试版*.yml',
        '*_极简版*.yml',
        '*_完美版*.yml',
        '*_超简版*.yml',
        '*_友好版*.yml',
        '*_标准版*.yml',
        '*_最终版*.yml',
        'xinghuo_*.py',
        '查询*价格*.yml'
    ]
    
    moved_files = []
    for pattern in temp_patterns:
        for file in glob.glob(pattern):
            if os.path.isfile(file):
                dest = f"temp/{os.path.basename(file)}"
                if not os.path.exists(dest):
                    shutil.move(file, dest)
                    moved_files.append(f"{file} -> {dest}")
    
    if moved_files:
        print("🗂️  移动临时文件:")
        for move in moved_files:
            print(f"   {move}")

def move_documentation():
    """移动文档文件"""
    doc_patterns = [
        '*说明*.md',
        '*指南*.md',
        '*解决方案*.md',
        'BTC*.md',
        '讯飞星火*.md'
    ]
    
    moved_files = []
    for pattern in doc_patterns:
        for file in glob.glob(pattern):
            if os.path.isfile(file) and not file.startswith('docs/'):
                dest = f"docs/{os.path.basename(file)}"
                if not os.path.exists(dest):
                    shutil.move(file, dest)
                    moved_files.append(f"{file} -> {dest}")
    
    if moved_files:
        print("📚 移动文档文件:")
        for move in moved_files:
            print(f"   {move}")

def clean_cache():
    """清理缓存文件"""
    cache_patterns = [
        '__pycache__',
        '*.pyc',
        '*.pyo',
        '.pytest_cache',
        '.coverage'
    ]
    
    cleaned = []
    for pattern in cache_patterns:
        for item in glob.glob(pattern, recursive=True):
            if os.path.isdir(item):
                shutil.rmtree(item)
                cleaned.append(f"目录: {item}")
            elif os.path.isfile(item):
                os.remove(item)
                cleaned.append(f"文件: {item}")
    
    if cleaned:
        print("🧹 清理缓存:")
        for item in cleaned:
            print(f"   {item}")

def create_readme_files():
    """为各个目录创建README文件"""
    readme_contents = {
        'scripts/README.md': """# 脚本目录

这个目录包含项目维护和工具脚本。

## 文件说明

- `cleanup_project.py` - 项目清理脚本
""",
        'temp/README.md': """# 临时文件目录

这个目录包含开发过程中的临时文件和测试文件。

⚠️ 注意：这个目录中的文件不会被Git跟踪。
""",
        'logs/README.md': """# 日志目录

这个目录包含应用程序运行日志。

⚠️ 注意：日志文件不会被Git跟踪。
"""
    }
    
    for file_path, content in readme_contents.items():
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"📝 创建README: {file_path}")

def main():
    """主函数"""
    print("🏗️  开始项目结构整理")
    print("=" * 50)
    
    # 创建目录结构
    create_directories()
    
    # 移动文件
    move_test_files()
    move_temp_files()
    move_documentation()
    
    # 清理缓存
    clean_cache()
    
    # 创建README文件
    create_readme_files()
    
    print("\n" + "=" * 50)
    print("✅ 项目结构整理完成！")
    print("\n📁 当前项目结构:")
    print("├── 📄 核心文件 (crypto_agent.py, price_service.py 等)")
    print("├── 📁 docs/ (文档)")
    print("├── 📁 examples/ (示例)")
    print("├── 📁 integrations/ (集成)")
    print("├── 📁 test/ (测试)")
    print("├── 📁 scripts/ (脚本)")
    print("├── 📁 temp/ (临时文件)")
    print("└── 📁 logs/ (日志)")
    
    print("\n💡 建议:")
    print("1. 检查temp/目录中的文件，确认不需要后可以删除")
    print("2. 运行 'git status' 查看更改")
    print("3. 运行 'git add .' 和 'git commit' 提交更改")

if __name__ == "__main__":
    main()