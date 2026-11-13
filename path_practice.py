from pathlib import Path

def main():

    # 任务1：创建 data 文件夹
    folder = Path("data")
    folder.mkdir(exist_ok=True)

    # 任务2：构造 data/history.json 路径
    file_path = folder / "history.json"

    # 任务3：判断 JSON 文件是否存在
    if file_path.exists():
        print(f"文件{file_path.name}存在")
    else:
        print(f"文件{file_path.name}不存在")

    # 任务4：打印文件名称、后缀、绝对路径
    print(f"文件名称：{file_path.name}")
    print(f"文件后缀：{file_path.suffix}")
    print(f"文件绝对路径：{file_path.resolve()}")

    # 任务5：如果文件不存在，写入 []
    if not file_path.exists():
        file_path.write_text("[]", encoding="utf-8")
        print(f"已创建新的聊天文件文件")


if __name__ == "__main__":
    main()
