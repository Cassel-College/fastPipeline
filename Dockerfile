# 使用 Python 官方基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 文件到工作目录
COPY requirements.txt .

# 安装 Python 依赖库
RUN pip install --no-cache-dir -r requirements.txt

# 复制当前目录的内容到容器的 /app 目录
COPY . .

# 启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
