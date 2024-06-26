"""
https://leetcode.com/problems/maximum-total-importance-of-roads/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_importance(self, n: int, roads: list[list[int]]) -> int:
        """
        maximum_importance
        """
        in_degress = [0] * n
        for u, v in roads:
            in_degress[v] += 1
            in_degress[u] += 1

        in_degress.sort()

        return sum((i + 1) * v for i, v in enumerate(in_degress))
