import json

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

    def save(self, filename):
        # TODO：将 self.history 保存到 filename
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=4)

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            messages = json.load(f)
            if not isinstance(messages, list):
                raise ValueError("Invalid data format: expected a list")
            self.history = messages

    def trim(self, max_history):
    # TODO：只保留最近 max_history 条消息
        self.history = self.history[-max_history:]
        return self.history