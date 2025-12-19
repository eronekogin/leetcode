"""
https://leetcode.com/problems/rename-columns/description/
"""


import pandas as pd


def rename_columns(students: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for rename_columns

    :param students: Description
    :type students: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    students = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
    return students
