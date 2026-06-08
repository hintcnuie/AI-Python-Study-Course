"""DataFrame 创建与操作练习。

使用 numpy 和 pandas 创建一个包含4列的 DataFrame，
并进行行选择、交叉提取、条件删除等操作。
"""

import numpy as np
import pandas as pd


def create_dataframe(seed: int | None = None) -> pd.DataFrame:
    """生成练习用的 DataFrame。

    创建包含以下列的 DataFrame：
    - A: 从2开始的15个连续偶数
    - B: 符合标准正态分布的15个随机数
    - C: 10-100之间的15个随机整数
    - D: 符合均值50、标准差10的正态分布随机数

    Args:
        seed: 随机种子，用于复现结果。为 None 时不固定种子。

    Returns:
        包含 A、B、C、D 四列的 pandas DataFrame
    """
    if seed is not None:
        np.random.seed(seed)

    data = {
        "A": np.arange(2, 32, 2),
        "B": np.random.randn(15),
        "C": np.random.randint(10, 101, 15),
        "D": np.random.normal(50, 10, 15),
    }
    return pd.DataFrame(data)


def get_row_by_index(df: pd.DataFrame, index: int) -> pd.Series:
    """获取 DataFrame 中指定索引位置的行。

    Args:
        df: 输入的 DataFrame
        index: 行索引（从0开始）

    Returns:
        指定行的 Series
    """
    return df.iloc[index]


def get_cross_section(
    df: pd.DataFrame, row_indices: list, col_names: list
) -> pd.DataFrame:
    """提取指定行索引与列名的交叉部分。

    Args:
        df: 输入的 DataFrame
        row_indices: 行索引列表
        col_names: 列名列表

    Returns:
        交叉部分 DataFrame
    """
    return df.loc[row_indices, col_names]


def delete_rows_by_column_value(
    df: pd.DataFrame, col_name: str, value_to_delete
) -> pd.DataFrame:
    """删除指定列中等于给定值的所有行。

    Args:
        df: 输入的 DataFrame
        col_name: 列名
        value_to_delete: 要删除的值

    Returns:
        删除后的新 DataFrame
    """
    return df[df[col_name] != value_to_delete]


def main() -> None:
    """主函数：演示 DataFrame 的各项操作。"""
    try:
        df = create_dataframe()
    except ImportError as e:
        print(f"导入错误，请确保已安装 numpy 和 pandas: {e}")
        return

    print("原始 DataFrame：")
    print(df)
    print("\n" + "=" * 50 + "\n")

    # 1）获取第4行的数据（索引为3）
    row_4 = get_row_by_index(df, 3)
    print("第4行的数据：")
    print(row_4)
    print("\n" + "=" * 50 + "\n")

    # 2）提取第3行、第5行与列B,D的交叉部分
    cross = get_cross_section(df, [2, 4], ["B", "D"])
    print("第3行、第5行与列B,D的交叉部分：")
    print(cross)
    print("\n" + "=" * 50 + "\n")

    # 3）删除A列值为16的那一行记录
    df_deleted = delete_rows_by_column_value(df, "A", 16)
    print("删除A列值为16的行后：")
    print(df_deleted)


if __name__ == "__main__":
    main()
