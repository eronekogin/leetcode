"""
https://leetcode.com/problems/modify-columns/description/
"""


import pandas as pd


def modify_salary_column(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for modify_salary_column

    :param employees: Description
    :type employees: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    employees['salary'] = employees['salary'] * 2
    return employees
