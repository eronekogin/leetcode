"""
https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/
"""


class Solution:
    """
    Solution
    """

    def area_of_max_diagonal(self, dimensions: list[list[int]]) -> int:
        """
        area of max diagonal
        """
        max_diagonal = 0
        max_area = 0
        for x, y in dimensions:
            curr_diagonal = x * x + y * y
            if curr_diagonal > max_diagonal:
                max_diagonal = curr_diagonal
                max_area = x * y
            elif curr_diagonal == max_diagonal and x * y > max_area:
                max_area = x * y

        return max_area
