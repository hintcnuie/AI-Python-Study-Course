"""字符串中间字符提取函数。

给定一个长度超过5的字符串，根据字符串长度的奇偶性，
提取中间几位字符：奇数长度取中间3位，偶数长度取中间2位。
"""


def get_middle_chars(s: str) -> str:
    """提取字符串中间几位字符。

    对于长度大于5的字符串：
    - 奇数长度时，返回中间3个字符
    - 偶数长度时，返回中间2个字符

    Args:
        s: 输入字符串，长度必须大于5

    Returns:
        提取出的中间字符

    Raises:
        TypeError: 输入不是字符串时抛出
        ValueError: 字符串长度不超过5时抛出
    """
    if not isinstance(s, str):
        raise TypeError(f"输入必须是字符串类型，当前类型: {type(s).__name__}")

    length = len(s)
    if length <= 5:
        raise ValueError(f"字符串长度必须大于5，当前长度: {length}")

    mid = length // 2
    if length % 2 == 1:
        # 奇数长度：中间3位
        return s[mid - 1 : mid + 2]
    else:
        # 偶数长度：中间2位
        return s[mid - 1 : mid + 1]


def main() -> None:
    """主函数：测试 get_middle_chars 函数。"""
    test_cases = ["abcdefg", "abcdef", "hello world"]

    for s in test_cases:
        try:
            result = get_middle_chars(s)
            length_type = "奇数" if len(s) % 2 == 1 else "偶数"
            print(f'"{s}"（{length_type}长度）的中间字符: "{result}"')
        except ValueError as e:
            print(f"错误: {e}")


if __name__ == "__main__":
    main()
