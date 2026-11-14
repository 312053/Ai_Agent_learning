import asyncio
import time

async def job(name, delay):
    print(f"{name}任务开始")
    await asyncio.sleep(delay)
    print(f"{name}任务完成")
    return f"{name}的结果"
async def main():
    start = time.perf_counter()
    task_a = asyncio.create_task(job("A", 2))
    task_b = asyncio.create_task(job("B", 3))
    task_c = asyncio.create_task(job("C", 1))
    print(f"三个任务已创建")
    result_a = await task_a
    result_b = await task_b
    result_c = await task_c
    end = time.perf_counter()
    print([result_a, result_b, result_c])
    print(f"总耗时: {end - start:.2f} 秒")

if __name__ == "__main__":
    asyncio.run(main())