"""
https://leetcode.com/problems/fill-missing-data/description/
"""


import pandas as pd


def fill_missing_values(products: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for fill_missing_values

    :param products: Description
    :type products: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    products['quantity'].fillna(0, inplace=True)
    return products
