"""
https://leetcode.com/problems/reshape-data-concatenate/description/
"""


import pandas as pd


def concatenate_tables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for concatenate_tables

    :param df1: Description
    :type df1: pd.DataFrame
    :param df2: Description
    :type df2: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    return pd.concat([df1, df2], axis=0)
