"""银行客户数据操作练习。

读取银行客户 CSV 文件，完成以下操作：
查看列名、查看数据类型、删除指定行、新增列、字符串拼接、条件筛选。
"""

import logging
import sys

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def load_bank_data(filepath: str) -> pd.DataFrame:
    """读取银行客户 CSV 文件。

    Args:
        filepath: CSV 文件的路径

    Returns:
        包含银行客户数据的 DataFrame

    Raises:
        FileNotFoundError: 指定路径的 CSV 文件不存在时抛出
    """
    try:
        df = pd.read_csv(filepath)
        logging.info(f"成功读取文件: {filepath}，共 {len(df)} 行")
        return df
    except FileNotFoundError:
        logging.error(f"文件未找到: {filepath}")
        raise


def get_columns(df: pd.DataFrame) -> list:
    """获取 DataFrame 的所有列名。

    Args:
        df: 输入的 DataFrame

    Returns:
        列名列表
    """
    return df.columns.tolist()


def get_dtypes(df: pd.DataFrame) -> pd.Series:
    """获取 DataFrame 所有列的数据类型。

    Args:
        df: 输入的 DataFrame

    Returns:
        各列数据类型的 Series
    """
    return df.dtypes


def remove_rows_by_job(df: pd.DataFrame, job_value: str) -> pd.DataFrame:
    """删除 job 列为指定值的所有行。

    Args:
        df: 输入的 DataFrame
        job_value: 要删除的 job 值

    Returns:
        删除后的新 DataFrame
    """
    rows_before = len(df)
    result = df[df["job"] != job_value]
    rows_removed = rows_before - len(result)
    logging.info(f"删除了 job='{job_value}' 的行，共 {rows_removed} 行")
    return result


def add_year_column(df: pd.DataFrame, year: str = "2025") -> pd.DataFrame:
    """新增 year 列，赋值为字符串格式的年份。

    Args:
        df: 输入的 DataFrame
        year: 年份字符串，默认为 "2025"

    Returns:
        包含新列 year 的 DataFrame
    """
    df = df.copy()
    df["year"] = year
    return df


def add_ym_column(df: pd.DataFrame) -> pd.DataFrame:
    """连接 year 和 month 列生成 ym 列（格式: '2025-aug'）。

    Args:
        df: 输入的 DataFrame（需要包含 year 和 month 列）

    Returns:
        包含新列 ym 的 DataFrame
    """
    df = df.copy()
    df["ym"] = df["year"] + "-" + df["month"]
    return df


def filter_retired_above_age(df: pd.DataFrame, age_threshold: int = 60) -> pd.DataFrame:
    """筛选 age 大于阈值且 job 为 'retired' 的记录。

    Args:
        df: 输入的 DataFrame
        age_threshold: 年龄阈值，默认为 60

    Returns:
        满足条件的记录组成的 DataFrame
    """
    return df.loc[(df["age"] > age_threshold) & (df["job"] == "retired")]


def main() -> None:
    """主函数：执行银行客户数据的各项操作。"""
    filepath = "BankCustomer Data.csv"

    try:
        df = load_bank_data(filepath)
    except FileNotFoundError:
        print(f"请将 'BankCustomer Data.csv' 放在当前目录下，然后重新运行。")
        sys.exit(1)

    # 1）查看有哪些变量
    print("1）变量（列名）：")
    print(get_columns(df))

    # 2）查看所有变量的数据类型
    print("\n2）数据类型：")
    print(get_dtypes(df))

    # 3）删除 job 为 unknown 的行
    print("\n3）删除 job 为 unknown 的行...")
    df = remove_rows_by_job(df, "unknown")

    # 4）新生成一列 year
    print("\n4）新增 year 列...")
    df = add_year_column(df)

    # 5）连接 year、month 生成 ym
    print("\n5）生成 ym 列...")
    df = add_ym_column(df)
    print("ym 列前5行：")
    print(df["ym"].head())

    # 6）提取 age 大于60且 job 为 retired 的记录
    print("\n6）age大于60且job为retired的记录：")
    group1 = filter_retired_above_age(df)
    print(f"共找到 {len(group1)} 条记录")
    print(group1)


if __name__ == "__main__":
    main()
