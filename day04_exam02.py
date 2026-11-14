import asyncio
import time

async def job(name, delay):
    print(f"{name}任务开始")
    await asyncio.sleep(delay)
    print(f"{name}任务完成")
    return f"{name}的结果"
async def main():
    start1 = time.perf_counter()
    a = await job("A", 2)
    b = await job("B", 3)
    c = await job("C", 1)
    end1 = time.perf_counter()
    print([a, b, c])
    print(f"总耗时: {end1 - start1:.2f} 秒")


    start2 = time.perf_counter()
    result = await asyncio.gather(
        job("A", 2),
        job("B", 3),
        job("C", 1)
    )
    end2 = time.perf_counter()
    print(result)
    print(f"总耗时: {end2 - start2:.2f} 秒")

if __name__ == "__main__":
    asyncio.run(main())