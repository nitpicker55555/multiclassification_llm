import asyncio
import random


async def async_func(efe):
    try:
        # 这只是一个示例，您可以替换为您的真实异步操作3
        timess=random.randint(0,8)
        print(timess)
        await asyncio.sleep(timess)
        return "Hello from async function!%s"%str(timess)
    except asyncio.CancelledError:
        print("Async function was cancelled!")
        return None

async def execute_with_timeout():
    while True:
        task = asyncio.create_task(async_func(efe=1))  # 创建一个Task对象
        try:
            result = await asyncio.wait_for(task, timeout=5)
            return result
        except asyncio.TimeoutError:
            print("Function took too long, cancelling and restarting...")
            task.cancel()
            await task  # 确保任何清理操作都已完成

# result = asyncio.run(execute_with_timeout())
# print(result)
