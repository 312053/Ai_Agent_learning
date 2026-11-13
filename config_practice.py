import os
from dotenv import load_dotenv

def main():

    # 任务1：加载 .env
    load_dotenv()

    # 任务2：读取 APP_NAME，设置默认值 ChatBot
    app_name = os.getenv("APP_NAME", "ChatBot")

    # 任务3：读取 DASHSCOPE_API_KEY
    dashscope_api_key = os.getenv("DASHSCOPE_API_KEY")

    # 任务4：读取 MAX_HISTORY，转换成整数
    max_history = int(os.getenv("MAX_HISTORY", "20"))

    # 任务5：检查 API Key 是否存在
    if not dashscope_api_key:
        raise RuntimeError("API_KEY未配置")

    # 任务6：打印配置信息
    print(f"应用名称：{app_name}")
    print(f"API_KEY已配置")
    print(f"最大历史记录条数：{max_history}")


if __name__ == "__main__":
    main()
