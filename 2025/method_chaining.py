"""
https://leetcode.com/problems/method-chaining/description/
"""


import pandas as pd


def find_heavy_animals(animals: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for find_heavy_animals

    :param animals: Description
    :type animals: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]
