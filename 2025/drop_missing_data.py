"""
https://leetcode.com/problems/drop-missing-data/description/
"""


import pandas as pd


def drop_missing_data(students: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for drop_missing_data

    :param students: Description
    :type students: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    students.dropna(subset=['name'], inplace=True)
    return students
