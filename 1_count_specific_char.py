"""统计字符串中指定字符的出现次数（忽略大小写）。

运行时会提示用户输入要查找的字符。
如果用户未输入（直接按回车），则默认查找字符 'c'。
"""


def count_char_in_string(text: str, char: str) -> int:
    """统计字符串中指定字符的出现次数，不区分大小写。

    Args:
        text: 待搜索的字符串
        char: 要查找的字符（也可以是子字符串）

    Returns:
        字符在字符串中出现的次数（不区分大小写）
    """
    return text.lower().count(char.lower())


def main() -> None:
    """主函数：获取用户输入并输出统计结果。"""
    s1 = " Welcome to China. China is a great country. Chinese people love to buy china."

    search_char_input = input("请输入需要查找的字符：")

    if not search_char_input.strip():
        search_char = "c"
        print(f"用户没有有效输入，查找的字符为默认的 '{search_char}'")
    else:
        search_char = search_char_input
        print(f"查找字符为 '{search_char}'")

    count_c = count_char_in_string(s1, search_char)
    print(f"字符'{search_char}'出现了 {count_c} 次")


if __name__ == "__main__":
    main()
