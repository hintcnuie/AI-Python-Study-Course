"""第5题测试：银行客户数据操作。"""

import pytest

from tests.conftest import _import_module

exercise5 = _import_module("exercise5", "5_bank_customer_data.py")


class TestLoadBankData:

    def test_file_not_found(self):
        """不存在的文件应抛出 FileNotFoundError。"""
        with pytest.raises(FileNotFoundError):
            exercise5.load_bank_data("nonexistent_file.csv")

    def test_load_success(self, sample_csv_path):
        """正确加载CSV文件。"""
        df = exercise5.load_bank_data(sample_csv_path)
        assert len(df) == 15


class TestGetColumns:

    def test_columns(self, sample_df):
        """应返回所有列名。"""
        cols = exercise5.get_columns(sample_df)
        assert "age" in cols
        assert "job" in cols
        assert "month" in cols


class TestGetDtypes:

    def test_dtypes(self, sample_df):
        """应返回各列的数据类型。"""
        dtypes = exercise5.get_dtypes(sample_df)
        assert "age" in dtypes.index
        assert "job" in dtypes.index


class TestRemoveRows:

    def test_unknown_removed(self, sample_df):
        """删除后不应再包含 job=unknown 的行。"""
        result = exercise5.remove_rows_by_job(sample_df, "unknown")
        assert "unknown" not in result["job"].values

    def test_row_count_decreased(self, sample_df):
        """删除后行数应减少。"""
        original_count = len(sample_df)
        result = exercise5.remove_rows_by_job(sample_df, "unknown")
        assert len(result) < original_count


class TestAddYearColumn:

    def test_year_column_exists(self, sample_df):
        """应新增 year 列。"""
        result = exercise5.add_year_column(sample_df)
        assert "year" in result.columns

    def test_year_value(self, sample_df):
        """year 列的值应为 '2025'。"""
        result = exercise5.add_year_column(sample_df)
        assert (result["year"] == "2025").all()


class TestAddYmColumn:

    def test_ym_column_exists(self, sample_df):
        """应新增 ym 列。"""
        df = exercise5.add_year_column(sample_df)
        result = exercise5.add_ym_column(df)
        assert "ym" in result.columns

    def test_ym_format(self, sample_df):
        """ym 列的格式应为 'year-month'。"""
        df = exercise5.add_year_column(sample_df)
        result = exercise5.add_ym_column(df)
        # 验证第一行的 ym 格式
        expected = df["year"].iloc[0] + "-" + df["month"].iloc[0]
        assert result["ym"].iloc[0] == expected


class TestFilterRetired:

    def test_only_retired(self, sample_df):
        """结果中应只有 job=retired 的行。"""
        result = exercise5.filter_retired_above_age(sample_df)
        assert (result["job"] == "retired").all()

    def test_age_above_60(self, sample_df):
        """结果中所有 age 应大于60。"""
        result = exercise5.filter_retired_above_age(sample_df)
        assert (result["age"] > 60).all()

    def test_returns_dataframe(self, sample_df):
        """返回类型应为 DataFrame。"""
        result = exercise5.filter_retired_above_age(sample_df)
        assert hasattr(result, "columns")
