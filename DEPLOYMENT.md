# 🚀 部署指南

本文档介绍如何部署加密货币Agent集成工具包。

## 📋 部署选项

### 1. 本地开发部署

#### 快速启动
```bash
# 安装依赖
pip install -r requirements.txt

# 启动服务
python start.py
```

#### 手动启动
```bash
# 启动价格服务
python price_service.py &

# 启动MCP服务器
python mcp_server.py &

# 测试功能
python test_suite.py
```

### 2. Docker部署

#### 使用Docker Compose（推荐）
```bash
# 构建并启动服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

#### 使用Docker
```bash
# 构建镜像
docker build -t crypto-agent-integration .

# 运行容器
docker run -d \
  --name crypto-agent \
  -p 5000:5000 \
  -p 8000:8000 \
  crypto-agent-integration
```

### 3. 云平台部署

#### Heroku部署
```bash
# 安装Heroku CLI
# 登录Heroku
heroku login

# 创建应用
heroku create your-crypto-agent-app

# 设置环境变量
heroku config:set FLASK_ENV=production

# 部署
git push heroku main

# 查看日志
heroku logs --tail
```

#### Vercel部署
```bash
# 安装Vercel CLI
npm i -g vercel

# 部署
vercel --prod
```

#### Railway部署
```bash
# 连接GitHub仓库到Railway
# 自动部署
```

## 🔧 环境配置

### 环境变量
```bash
# 生产环境
export FLASK_ENV=production
export PORT=5000
export MCP_PORT=8000

# 开发环境
export FLASK_ENV=development
export DEBUG=true

# API配置
export API_TIMEOUT=30
export CACHE_TTL=300

# Redis配置（可选）
export REDIS_URL=redis://localhost:6379
```

### 配置文件
创建 `config.json`:
```json
{
  "api": {
    "timeout": 30,
    "retries": 3,
    "cache_ttl": 300
  },
  "mcp": {
    "port": 8000,
    "auto_approve": [
      "query_crypto_price",
      "get_market_overview",
      "batch_query_crypto"
    ]
  },
  "logging": {
    "level": "INFO",
    "file": "logs/app.log"
  }
}
```

## 🌐 Nginx反向代理

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /mcp {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

## 📊 监控和日志

### 健康检查端点
- `GET /health` - 服务健康状态
- `GET /metrics` - 服务指标
- `GET /status` - 详细状态信息

### 日志配置
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)
```

### Prometheus监控
```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'crypto-agent'
    static_configs:
      - targets: ['localhost:5000']
    metrics_path: '/metrics'
    scrape_interval: 30s
```

## 🔐 安全配置

### API密钥管理
```bash
# 设置API密钥
export CRYPTO_API_KEY=your-secret-key

# 使用环境变量
import os
api_key = os.environ.get('CRYPTO_API_KEY')
```

### HTTPS配置
```bash
# 使用Let's Encrypt
certbot --nginx -d your-domain.com
```

### 防火墙设置
```bash
# 开放必要端口
ufw allow 80
ufw allow 443
ufw allow 5000
ufw allow 8000
```

## 📈 性能优化

### 缓存配置
```python
# Redis缓存
import redis
cache = redis.Redis(host='localhost', port=6379, db=0)

# 内存缓存
from functools import lru_cache

@lru_cache(maxsize=128)
def get_crypto_price(symbol):
    # 缓存价格数据
    pass
```

### 负载均衡
```yaml
# docker-compose.yml
version: '3.8'
services:
  crypto-agent-1:
    build: .
    ports:
      - "5001:5000"
  
  crypto-agent-2:
    build: .
    ports:
      - "5002:5000"
  
  nginx:
    image: nginx
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
```

## 🚨 故障排除

### 常见问题

1. **端口占用**
```bash
# 查找占用端口的进程
lsof -i :5000
netstat -tulpn | grep :5000

# 杀死进程
kill -9 <PID>
```

2. **依赖问题**
```bash
# 重新安装依赖
pip install --force-reinstall -r requirements.txt

# 清理缓存
pip cache purge
```

3. **权限问题**
```bash
# 设置文件权限
chmod +x start.py
chmod +x mcp_server.py
```

### 调试模式
```bash
# 启用调试模式
export FLASK_ENV=development
export DEBUG=true
python price_service.py
```

### 日志分析
```bash
# 查看实时日志
tail -f logs/app.log

# 搜索错误
grep -i error logs/app.log

# 分析访问模式
awk '{print $1}' logs/access.log | sort | uniq -c | sort -nr
```

## 📋 部署检查清单

- [ ] 环境变量配置完成
- [ ] 依赖安装成功
- [ ] 端口配置正确
- [ ] 防火墙规则设置
- [ ] SSL证书配置（生产环境）
- [ ] 监控和日志配置
- [ ] 备份策略制定
- [ ] 健康检查配置
- [ ] 性能测试完成
- [ ] 安全审计通过

## 🔄 更新和维护

### 滚动更新
```bash
# 拉取最新代码
git pull origin main

# 重启服务
docker-compose restart

# 验证更新
python test_suite.py
```

### 备份策略
```bash
# 备份配置文件
tar -czf backup-$(date +%Y%m%d).tar.gz config/ logs/

# 定期备份脚本
0 2 * * * /path/to/backup.sh
```

---

如有部署问题，请查看项目的Issue页面或联系维护者。