"""
https://leetcode.com/problems/row-with-maximum-ones/description/
"""


class Solution:
    """
    Solution
    """

    def row_and_maximum_ones(self, mat: list[list[int]]) -> list[int]:
        """
        row and maximum ones
        """
        max_index, max_count = 0, 0
        for i, row in enumerate(mat):
            curr_count = row.count(1)
            if curr_count > max_count:
                max_index, max_count = i, curr_count

        return [max_index, max_count]
