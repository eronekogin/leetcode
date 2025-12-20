"""
https://leetcode.com/problems/change-data-type/description/
"""


import pandas as pd


def change_data_type(students: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for change_data_type

    :param students: Description
    :type students: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    students = students.astype({'grade': int})
    return students
