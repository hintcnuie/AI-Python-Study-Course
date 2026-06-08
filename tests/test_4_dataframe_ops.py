"""第4题测试：DataFrame 创建与操作。"""

import numpy as np
import pandas as pd

from tests.conftest import _import_module

exercise4 = _import_module("exercise4", "4_dataframe_operations.py")


class TestCreateDataframe:

    def test_shape(self):
        """DataFrame 应为 15行 × 4列。"""
        df = exercise4.create_dataframe()
        assert df.shape == (15, 4)

    def test_columns(self):
        """列名应为 A, B, C, D。"""
        df = exercise4.create_dataframe()
        assert list(df.columns) == ["A", "B", "C", "D"]

    def test_column_a_values(self):
        """A列应为2到30的连续偶数。"""
        df = exercise4.create_dataframe()
        expected = np.arange(2, 32, 2)
        assert (df["A"].values == expected).all()

    def test_seeded_deterministic(self):
        """相同seed应生成完全相同的DataFrame。"""
        df1 = exercise4.create_dataframe(seed=42)
        df2 = exercise4.create_dataframe(seed=42)
        pd.testing.assert_frame_equal(df1, df2)


class TestGetRow:

    def test_row_4_value(self, seeded_df):
        """第4行（索引3）的A列值应为8。"""
        row = exercise4.get_row_by_index(seeded_df, 3)
        assert row["A"] == 8


class TestGetCrossSection:

    def test_shape(self, seeded_df):
        """交叉提取应返回 2行 × 2列。"""
        result = exercise4.get_cross_section(seeded_df, [2, 4], ["B", "D"])
        assert result.shape == (2, 2)

    def test_columns(self, seeded_df):
        """交叉提取的列应为 B 和 D。"""
        result = exercise4.get_cross_section(seeded_df, [2, 4], ["B", "D"])
        assert list(result.columns) == ["B", "D"]


class TestDeleteRows:

    def test_a16_removed(self, seeded_df):
        """删除后 A 列不应再包含 16。"""
        df_deleted = exercise4.delete_rows_by_column_value(seeded_df, "A", 16)
        assert 16 not in df_deleted["A"].values

    def test_shape_after_delete(self, seeded_df):
        """删除后应为 14行。"""
        df_deleted = exercise4.delete_rows_by_column_value(seeded_df, "A", 16)
        assert df_deleted.shape == (14, 4)
