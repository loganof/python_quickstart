"""
asyncio.gather()
收集协程的结果
asyncio.wait()
返回完成的任务与挂起的任务

"""

import asyncio


async def a():
    print("Suspending a")
    await asyncio.sleep(3)
    print('Resuming a')
    return 'A'

async def b():
    print("Suspending b")
    await asyncio.sleep(3)
    print('Resuming b')
    return 'B'

async def main():
    # return_value_a, return_value_b = await asyncio.gather(a(), b())
    # print(return_value_a, return_value_b)
    done, pending = await asyncio.wait([a(), b()])
    print(done, pending)

asyncio.run(main())
