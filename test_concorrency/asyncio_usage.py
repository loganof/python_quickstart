"""
1. asyncio 是_Python_ 3.4版本_引入_的标准库，直接内置了对异步IO的支持。对比多线程、多进程，Asyncio是一种单线程的并发模型。
2. loop.run_until_complete()方法是 asyncio 中早期的 API。
3. asyncio.run()是python3.7中引入的，是运行asyncio程序的推荐方法。
"""

import asyncio

async def task():
    await asyncio.sleep(1)
    print("task complete")
    
    
if __name__ == "__main__":
    # method1
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task())
    # method2
    # asyncio.run(task())
    
    