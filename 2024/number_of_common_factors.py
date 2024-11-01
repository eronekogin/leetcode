"""
https://leetcode.com/problems/number-of-common-factors/description/
"""


class Solution:
    """
    Solution
    """

    def common_factors(self, a: int, b: int) -> int:
        """
        common factors
        """
        return sum(
            a % x == 0 and b % x == 0
            for x in range(1, min(a, b) + 1)
        )
