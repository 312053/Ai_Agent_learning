import json
from Chat_History import ChatHistory
from pathlib import Path
from config import APP_NAME, HISTORY_FILE, MAX_HISTORY

def main():

    history = ChatHistory()
    file_path = Path(HISTORY_FILE)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    max_history = MAX_HISTORY
    if max_history <= 0:
        raise ValueError("max_history must be a positive integer")
    print(f"欢迎使用{APP_NAME}")

    try:
        history.load(file_path)
    # TODO 1：捕获 FileNotFoundError
    except FileNotFoundError:
        print("历史记录文件不存在")
    # TODO 2：捕获 json.JSONDecodeError
    except json.JSONDecodeError:
        print("历史记录文件格式错误")
        return
    print(f"加载的旧聊天记录为：{len(history.list())}条")

    try:
        message1 = input("请输入消息：")
        history.add("user", message1)
    except ValueError as e:
        print(f"输入错误：{e}")
        return

    if len(history.list()) > max_history:
        history.trim(max_history)
        print(f"已裁剪聊天记录，只保留最近{max_history}条消息"  )

    history.save(file_path)
    print(f"当前聊天记录数量为{len(history.list())}条")

if __name__ == "__main__":
    main()