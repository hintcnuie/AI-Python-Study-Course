"""pytest 共享 fixtures。

为所有测试提供共用的测试数据和辅助函数。
"""

import importlib.util
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent


def _import_module(module_name: str, filename: str):
    """通过文件名导入模块（支持以数字开头的文件名）。

    Args:
        module_name: 模块的逻辑名称
        filename: .py 文件的相对路径（相对于项目根目录）
    """
    filepath = PROJECT_ROOT / filename
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture
def sample_csv_path() -> str:
    """返回测试用 CSV 文件的路径。"""
    return str(Path(__file__).parent / "fixtures" / "bank_customers.csv")


@pytest.fixture
def sample_df(sample_csv_path: str) -> pd.DataFrame:
    """返回从测试 CSV 读入的 DataFrame。"""
    return pd.read_csv(sample_csv_path)


@pytest.fixture
def seeded_df() -> pd.DataFrame:
    """返回使用固定种子的练习 DataFrame（对应第4题）。

    A列: [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
    B/C/D列: 由 seed(42) 生成的确定值
    """
    np.random.seed(42)
    data = {
        "A": np.arange(2, 32, 2),
        "B": np.random.randn(15),
        "C": np.random.randint(10, 101, 15),
        "D": np.random.normal(50, 10, 15),
    }
    return pd.DataFrame(data)
