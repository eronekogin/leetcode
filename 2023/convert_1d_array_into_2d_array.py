"""
https://leetcode.com/problems/convert-1d-array-into-2d-array/
"""


class Solution:
    """
    Solution
    """

    def construct_2d_array(self, original: list[int], m: int, n: int) -> list[list[int]]:
        """
        construct_2d_array
        """
        if len(original) != m * n:
            return []

        return [original[i: i + n] for i in range(0, len(original), n)]
