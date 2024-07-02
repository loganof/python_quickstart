import requests

with requests.get("https://www.example.com") as response:
    data = response.text
    
# 请求在这里自动关闭，因为上下文管理器的离开    