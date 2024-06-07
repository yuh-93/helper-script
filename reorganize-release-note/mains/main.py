input_file_path = "input.md"
output_file_path = "output.md"


def reorganize_release_notes_from_file(input_file_path):
    with open(input_file_path, "r") as file:
        notes = file.read()
        return reorganize_release_notes(notes)


def reorganize_release_notes(notes):
    # ノートを行ごとに分割
    lines = notes.split("\n")

    # 各カテゴリーにアイテムを格納するための辞書
    categorized = {}

    for line in lines:
        # 行が'*'で始まるかチェック
        if line.startswith("* "):
            # カテゴリーと残りの行を抽出
            category, _, rest = line[2:].partition(":")
            # 適切なカテゴリーに行を追加
            categorized.setdefault(category.strip(), []).append(line)

    # 再編成されたノートを構築
    reorganized_notes = "## What's Changed\n"
    for category, items in categorized.items():
        reorganized_notes += f"## {category}\n"
        reorganized_notes += "\n".join(items) + "\n"

    return reorganized_notes


if __name__ == "__main__":
    reorganized_notes = reorganize_release_notes_from_file(input_file_path)

    # リリースノートを表示
    print(reorganized_notes)

    # リリースノートを指定されたファイルに保存
    with open(output_file_path, "w") as output_file:
        output_file.write(reorganized_notes)
