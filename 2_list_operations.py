"""列表索引与切片操作练习。

给定嵌套列表 list1 = [2, 3, 5, 7, 9, [2, 4, 6, 8]]，
完成两个操作：获取元素 5，以及获取切片 [4, 6, 8]。
"""


def get_element_at_index(lst: list, index: int):
    """获取列表中指定索引位置的元素。

    Args:
        lst: 列表
        index: 索引位置

    Returns:
        列表中该索引位置的元素
    """
    return lst[index]


def get_nested_slice(lst: list, outer_idx: int, inner_start: int, inner_end: int):
    """获取嵌套列表中子列表的切片。

    Args:
        lst: 外层列表
        outer_idx: 嵌套子列表在外层列表中的索引
        inner_start: 子列表中切片的起始索引
        inner_end: 子列表中切片的结束索引（不包含）

    Returns:
        切取到的子列表片段
    """
    return lst[outer_idx][inner_start:inner_end]


def main() -> None:
    """主函数：演示列表索引与切片操作。"""
    list1 = [2, 3, 5, 7, 9, [2, 4, 6, 8]]

    # 1）获取 5 这个值（索引为2）
    value_5 = get_element_at_index(list1, 2)
    print("获取到的值为：", value_5)

    # 2）获取切片 [4, 6, 8]
    # 嵌套列表在索引5的位置，切片取索引1到3（不含4）
    slice_result = get_nested_slice(list1, 5, 1, 4)
    print("获取到的切片为：", slice_result)


if __name__ == "__main__":
    main()
