import os
from dotenv import load_dotenv

#加载 .env.
load_dotenv()

#读取应用名称，默认值为 ChatBot.
APP_NAME = os.getenv("APP_NAME", "ChatBot")


#读取聊天记录保存路径，默认值为 data/history.json.
HISTORY_FILE = os.getenv("HISTORY_FILE", "data/history.json")


#读取最大聊天记录数量，并转换为整数，默认值为 20.
MAX_HISTORY = int(os.getenv("MAX_HISTORY", "20"))