"""
https://leetcode.com/problems/reshape-data-melt/description/
"""


import pandas as pd


def melt_table(report: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for melt_table

    :param report: Description
    :type report: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    report = report.melt(
        id_vars=["product"],
        value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
        var_name="quarter",
        value_name="sales",
    )
    return report
