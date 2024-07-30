1. 添加fastapi_usage到python查找路径
   1. 新建.env文件
      1. PYTHONPATH=./tools/fastapi_usage
   2. ctrl + shift + p: 首选项(打开工作区设置)
      1. {"python.envFile": "${workspaceFolder}/.env"}
2. 执行
   1. python tools/fastapi_usage/main.py
3. Pydantic是一个python数据校验库。整个FastAPI建立在Pydantic的基础之上。