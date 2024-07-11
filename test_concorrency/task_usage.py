"""
有3种方式, 将协程封装成task.从python3.7之后, 可以统一使用更高阶的asyncio.create_task()
1. task = asyncio.ensure_future(coroutine)
2. task = asyncio.create_task(coroutine)
3. task= loop.create_task(coroutine)
"""


import asyncio


async def task():
    await asyncio.sleep(1)
    print("task complete")
    



async def main():
    task1 = asyncio.ensure_future(task())
    await task1
    
    # recommend
    task2 = asyncio.create_task(task())
    await task2
    
    loop = asyncio.get_event_loop()
    task3 = loop.create_task(task())
    await task3
    
asyncio.run(main())

