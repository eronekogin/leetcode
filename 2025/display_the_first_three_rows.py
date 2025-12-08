"""
https://leetcode.com/problems/display-the-first-three-rows/description/
"""


import pandas as pd


def select_first_rows(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for select_first_rows

    :param employees: Description
    :type employees: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    return employees.head(3)
