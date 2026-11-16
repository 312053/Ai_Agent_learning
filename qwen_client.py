import os
from dotenv import load_dotenv
from pathlib import Path
import asyncio
from openai import (
    AsyncOpenAI,
    AuthenticationError,
    RateLimitError,
    APITimeoutError,
    APIConnectionError,
)
import time

async def safe_ask(client, model, question):
    try:
        reply = await ask(client, model, question)
        return {
            "question": question, 
            "status": "success", 
            "message": reply
            }
    except AuthenticationError:
        return {
            "question": question, 
            "status": "error", 
            "message": "认证失败，请检查密钥与服务配置"
            }
    except RateLimitError:
        return {
            "question": question, 
            "status": "error", 
            "message": "请求受到限制，请检查限流或额度"
            }
    except APITimeoutError:
        return {
            "question": question, 
            "status": "timeout", 
            "message": "模型请求超时"
            }
    except APIConnectionError:
        return {
            "question": question, 
            "status": "error", 
            "message": "连接失败，请检查网络与接口地址"
            }
    except ValueError as e:
        return {
            "question": question, 
            "status": "error", 
            "message": str(e)
            }


async def ask(client, model, question):
    response = await client.chat.completions.create(
        model=model,
        messages=[
            {"role":"user", "content":question}
        ]
    )
    if not response.choices:
        raise ValueError("服务未返回候选回复")
    reply = response.choices[0].message.content
    if not reply or not reply.strip():
        raise ValueError("服务未返回有效文本")
    return reply

async def main():
    load_dotenv(Path(__file__).resolve().parent / ".env")
    api_key = os.getenv("DASHSCOPE_API_KEY")
    qwen_base_url = os.getenv("QWEN_BASE_URL")
    qwen_model =os.getenv("QWEN_MODEL")

    if not api_key or not api_key.strip():
        raise ValueError("缺少配置: DASHSCOPE_API_KEY")
    if not qwen_base_url or not qwen_base_url.strip():
        raise ValueError("缺少配置: QWEN_BASE_URL")
    if not qwen_model or not qwen_model.strip():
        raise ValueError("缺少配置: QWEN_MODEL")

    questions = [
    "用一句话解释什么是 API。",
    "用一句话解释什么是协程。",
    "用一句话解释 Python asyncio 中的事件循环。",
]

    async with AsyncOpenAI(
        api_key = api_key,
        base_url =qwen_base_url,
        timeout=30.0,
        max_retries=0,
) as client:
        start = time.perf_counter()
        results = await asyncio.gather(
            safe_ask(client, qwen_model, questions[0]),
            safe_ask(client, qwen_model, questions[1]),
            safe_ask(client, qwen_model, questions[2]),
        )
        elapsed = time.perf_counter() - start
        for result in results:
            print(f"问题：{result['question']}")
            print(f"状态：{result['status']}")
            print(f"结果：{result['message']}")
            print()
        print(f"批量问答总耗时：{elapsed:.2f} 秒")


if __name__ == "__main__":
    asyncio.run(main())