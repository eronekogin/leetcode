"""
https://leetcode.com/problems/create-a-dataframe-from-list/description/
"""


import pandas as pd


def create_data_frame(student_data: list[list[int]]) -> pd.DataFrame:
    """
    Docstring for create_data_frame

    :param student_data: Description
    :type student_data: list[list[int]]
    :return: Description
    :rtype: DataFrame
    """
    column_names = ['student_id', 'age']
    return pd.DataFrame(student_data, columns=column_names)
