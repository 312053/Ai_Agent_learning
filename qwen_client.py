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

async def ask(api_key, base_url, model):
     async with AsyncOpenAI(
          api_key = api_key,
          base_url = base_url,
          timeout=30.0,
          max_retries=0,
     ) as client:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role":"user", "content":"用一句话解释异步编程。"}
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
            
    try:
        reply = await ask(api_key, qwen_base_url, qwen_model)
        print(reply)
    except AuthenticationError:
         print("认证失败，请检查密钥与服务配置")
    except RateLimitError:
         print("请求受到限制，请检查限流或额度")
    except APITimeoutError:
         print("模型请求超时")
    except APIConnectionError:
         print("连接失败，请检查网络与接口地址")
    except ValueError as e:
         print(f"执行错误：{e}")

if __name__ == "__main__":
    asyncio.run(main())