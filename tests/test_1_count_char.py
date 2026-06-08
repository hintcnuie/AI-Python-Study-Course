"""第1题测试：字符计数函数。"""

from tests.conftest import _import_module

# 导入以数字开头的模块
exercise1 = _import_module("exercise1", "1_count_specific_char.py")


def test_count_char_present():
    """字符存在时返回正确次数。"""
    assert exercise1.count_char_in_string("China", "c") == 1


def test_count_char_absent():
    """字符不存在时返回0。"""
    assert exercise1.count_char_in_string("hello", "z") == 0


def test_count_case_insensitive():
    """不区分大小写。"""
    assert exercise1.count_char_in_string("CHINA china", "c") == 2


def test_count_with_original_string():
    """使用题目原始字符串，查'c'应出现6次。"""
    s1 = " Welcome to China. China is a great country. Chinese people love to buy china."
    assert exercise1.count_char_in_string(s1, "c") == 6


def test_count_empty_text():
    """空文本返回0。"""
    assert exercise1.count_char_in_string("", "a") == 0


def test_count_multichar_search():
    """搜索子字符串也应正确计数。"""
    assert exercise1.count_char_in_string("hello hello", "ll") == 2
