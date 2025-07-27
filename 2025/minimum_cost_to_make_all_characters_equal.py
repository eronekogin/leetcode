"""
https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_cost(self, s: str) -> int:
        """
        minimum cost
        """
        n = len(s)
        return sum(
            min(i, n - i)
            for i in range(1, n)
            if s[i] != s[i - 1]
        )
