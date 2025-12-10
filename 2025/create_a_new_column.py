"""
https://leetcode.com/problems/create-a-new-column/description/
"""


import pandas as pd


def create_bonus_column(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for create_bonus_column

    :param employees: Description
    :type employees: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    employees['bonus'] = employees['salary'] * 2
    return employees
