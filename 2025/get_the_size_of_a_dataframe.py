"""
https://leetcode.com/problems/get-the-size-of-a-dataframe/description/
"""


import pandas as pd


def get_data_frame_size(players: pd.DataFrame) -> list[int]:
    """
    Docstring for get_data_frame_size

    :param players: Description
    :type players: pd.DataFrame
    :return: Description
    :rtype: list[int]
    """
    return [
        *players.shape
    ]
