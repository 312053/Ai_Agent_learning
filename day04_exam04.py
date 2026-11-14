import asyncio
import time

async def simulate_task(name, delay, should_fail=False):
    print(f"{name}任务开始")
    await asyncio.sleep(delay)
    if should_fail:
        raise ValueError(f"{name}执行失败")
    return f"{name}执行成功"

async def run_task(name, delay, should_fail=False):
    try:
        result = await asyncio.wait_for(simulate_task(name, delay, should_fail=should_fail), timeout=2)
        return result
    except ValueError as e:
        return f"{name}失败：{e}"
    except TimeoutError:
        return f"{name}超时"

async def main():
    start = time.perf_counter()
    results = await asyncio.gather(
        run_task("A", 1, should_fail=False),
        run_task("B", 1, should_fail=True),
        run_task("C", 4, should_fail=False)
    )
    end = time.perf_counter()
    print(results)
    print(f"总耗时: {end - start:.2f} 秒")

if __name__ == "__main__":
    asyncio.run(main())