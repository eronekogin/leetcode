"""
https://leetcode.com/problems/drop-duplicate-rows/description/
"""


import pandas as pd


def drop_duplicate_emails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Docstring for drop_duplicate_emails

    :param customers: Description
    :type customers: pd.DataFrame
    :return: Description
    :rtype: DataFrame
    """
    return customers.drop_duplicates('email')
