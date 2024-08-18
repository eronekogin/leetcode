"""
https://leetcode.com/problems/equal-row-and-column-pairs/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def equal_pairs(self, grid: list[list[int]]) -> int:
        """
        equal pairs
        """
        rows = Counter(tuple(x) for x in grid)
        cols = Counter(zip(*grid))
        return sum(rows[k] * cols[k] for k in cols)


Solution().equal_pairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]])
