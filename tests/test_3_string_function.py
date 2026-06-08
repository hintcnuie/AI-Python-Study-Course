"""第3题测试：字符串中间字符提取函数。"""

import pytest

from tests.conftest import _import_module

exercise3 = _import_module("exercise3", "3_string_function.py")


def test_odd_length_7():
    """奇数长度7应返回中间3位。"""
    assert exercise3.get_middle_chars("abcdefg") == "cde"


def test_even_length_6():
    """偶数长度6应返回中间2位。"""
    assert exercise3.get_middle_chars("abcdef") == "cd"


def test_odd_length_9():
    """奇数长度9应返回中间3位。"""
    assert exercise3.get_middle_chars("123456789") == "456"


def test_even_length_8():
    """偶数长度8应返回中间2位。"""
    assert exercise3.get_middle_chars("12345678") == "45"


def test_min_length_6():
    """长度恰好6（边界值）。"""
    assert exercise3.get_middle_chars("123456") == "34"


def test_length_exactly_5_raises():
    """长度恰好5应抛出 ValueError。"""
    with pytest.raises(ValueError):
        exercise3.get_middle_chars("12345")


def test_length_3_raises():
    """长度小于5应抛出 ValueError。"""
    with pytest.raises(ValueError):
        exercise3.get_middle_chars("abc")


def test_empty_string_raises():
    """空字符串应抛出 ValueError。"""
    with pytest.raises(ValueError):
        exercise3.get_middle_chars("")


def test_non_string_int_raises():
    """传入整数应抛出 TypeError。"""
    with pytest.raises(TypeError):
        exercise3.get_middle_chars(123)


def test_non_string_none_raises():
    """传入 None 应抛出 TypeError。"""
    with pytest.raises(TypeError):
        exercise3.get_middle_chars(None)
