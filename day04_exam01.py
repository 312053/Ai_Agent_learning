import asyncio

async def get_message(name, delay):
    print(f"开始处理：{name}")
    await asyncio.sleep(delay)
    return f"处理完成：{name}"

async def main():
    results = await get_message("文献搜索", 2)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())