class ChatBot:

    def __init__(self, name):
        # 1. 保存机器人名称
        self.name = name

        # 2. 创建一个空列表，用于保存聊天记录
        self.chat_history = []


    def chat(self, message):
        # 3. 如果 message 不是字符串，抛出 TypeError
        if not isinstance(message, str):
            raise TypeError("Message must be a string.")

        # 4. 如果 message 是空字符串，抛出 ValueError
        if message.strip() == "":
            raise ValueError("Message cannot be an empty string.")

        # 5. 将用户消息添加到聊天记录
        self.chat_history.append({"role":"user", "content":message})

        # 6. 生成回复，例如：Qwen收到：你好
        response = f"{self.name}收到：{message}"

        # 7. 将机器人回复添加到聊天记录
        self.chat_history.append({"role":"assistant", "content":response})

        # 8. 返回机器人回复
        return response

    def show_history(self):
        for message in self.chat_history:
            role = message["role"]
            content = message["content"]
            print(f"{role}:{content}")
    # 显示全部聊天记录

    def clear_history(self):
        self.chat_history.clear()
    # 清空聊天记录

bot = ChatBot("Qwen")
response = bot.chat("很高兴见到你")
try:
    bot.chat(123)
except TypeError as e:
    print(f"捕获到异常{e}")

try:
    bot.chat("  ")
except ValueError as e:
    print(f"捕获到异常{e}")

print(response)
print(bot.chat_history)
print("查看聊天记录：")
bot.show_history()
print("清空聊天记录：")
bot.clear_history()
print(bot.chat_history)