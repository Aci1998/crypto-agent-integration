FROM python:3.9-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 5000 8000

# 创建启动脚本
RUN echo '#!/bin/bash\n\
echo "🚀 启动加密货币Agent集成服务..."\n\
echo "价格服务端口: 5000"\n\
echo "MCP服务器端口: 8000"\n\
echo ""\n\
# 启动价格服务\n\
python price_service.py &\n\
PRICE_PID=$!\n\
\n\
# 等待价格服务启动\n\
sleep 3\n\
\n\
# 启动MCP服务器\n\
python mcp_server.py &\n\
MCP_PID=$!\n\
\n\
echo "✅ 服务启动完成"\n\
echo "价格服务PID: $PRICE_PID"\n\
echo "MCP服务器PID: $MCP_PID"\n\
echo ""\n\
echo "🧪 运行测试:"\n\
python test_suite.py\n\
\n\
# 保持容器运行\n\
wait\n\
' > /app/start.sh && chmod +x /app/start.sh

CMD ["/app/start.sh"]