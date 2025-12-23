"""
https://leetcode.com/problems/reshape-data-pivot/description/
"""


import pandas as pd


def pivot_table(weather: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for pivot_table

    :param weather: Description
    :type weather: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    ans = weather.pivot(index='month', columns='city', values='temperature')
    return ans
