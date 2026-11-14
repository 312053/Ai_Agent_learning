import asyncio
import time

async def run_task(name, delay, should_fail=False):
    print(f"{name}开始执行")
    await asyncio.sleep(delay)
    if should_fail:
        raise ValueError(f"{name}执行失败")
    return f"{name}执行成功"

async def packtask(name, delay, should_fail=False):
    try:
        result = await asyncio.wait_for(run_task(name, delay, should_fail=should_fail), timeout=2)
        return {"name":name, "status":"success", "message":result}
    except TimeoutError:
        return {"name":name, "status":"timeout", "message":name+"超时"}
    except ValueError as e:
        return {"name":name, "status":"error", "message":str(e)}
    

async def main():
    start = time.perf_counter()
    
    task1 = asyncio.create_task(packtask("文献搜索", 1, should_fail=False))
    task2 = asyncio.create_task(packtask("数据查询", 1, should_fail=True))
    task3 = asyncio.create_task(packtask("模型请求", 4, should_fail=False))

    results = await asyncio.gather(
        task1,
        task2,
        task3
    )

    end = time.perf_counter()
    for result in results:
        print(result)
    print(f"总耗时：{end - start:.2f}秒")


if __name__ == "__main__":
    asyncio.run(main())