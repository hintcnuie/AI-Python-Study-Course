"""第2题测试：列表索引与切片操作。"""

from tests.conftest import _import_module

exercise2 = _import_module("exercise2", "2_list_operations.py")


# 测试用的列表
LIST1 = [2, 3, 5, 7, 9, [2, 4, 6, 8]]


def test_get_element_5():
    """获取索引2的值应为5。"""
    assert exercise2.get_element_at_index(LIST1, 2) == 5


def test_get_element_first():
    """获取索引0的值应为2。"""
    assert exercise2.get_element_at_index(LIST1, 0) == 2


def test_get_nested_slice():
    """获取嵌套列表切片 [4,6,8]。"""
    assert exercise2.get_nested_slice(LIST1, 5, 1, 4) == [4, 6, 8]


def test_get_nested_slice_single():
    """获取嵌套列表单个元素切片。"""
    assert exercise2.get_nested_slice(LIST1, 5, 0, 1) == [2]


def test_get_nested_slice_all():
    """获取嵌套列表全部元素。"""
    assert exercise2.get_nested_slice(LIST1, 5, 0, 4) == [2, 4, 6, 8]
