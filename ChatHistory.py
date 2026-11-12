class ChatHistory:

    def __init__(self):
        self.history = []

    def add(self, role, content):
        if role not in ("user", "assistant", "system"):
            raise ValueError("Invalid role")
        if not isinstance(content, str):
            raise TypeError("Content must be a string")
        if not content.strip():
            raise ValueError("Content cannot be empty")
        self.history.append({
            "role": role, 
            "content": content
            })

    def list(self):
        # 返回全部聊天记录
        return self.history.copy()

    def clear(self):
        # 清空聊天记录
        self.history.clear()
history = ChatHistory()

# 测试正常添加
history.add("user", "你好")
history.add("assistant", "你好！")

assert len(history.list()) == 2

# 测试清空
history.clear()

assert history.list() == []

# 测试非法角色
try:
    history.add("admin", "你好")
except ValueError:
    print("非法角色测试通过")

# 测试错误类型
try:
    history.add("user", 123)
except TypeError:
    print("类型错误测试通过")

# 测试空消息
try:
    history.add("user", "   ")
except ValueError:
    print("空消息测试通过")

print("测试结束")