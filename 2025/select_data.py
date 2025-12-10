"""
https://leetcode.com/problems/select-data/description/
"""


import pandas as pd


def select_data(students: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for select_data

    :param students: Description
    :type students: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    return students.loc[students['student_id'] == 101, ['name', 'age']]
