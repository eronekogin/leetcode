"""
https://leetcode.com/problems/find-the-pivot-integer/description/
"""


class Solution:
    """
    Solution
    """

    def pivot_integer(self, n: int) -> int:
        """
        pivot integer
        """
        total = ((1 + n) * n) >> 1
        t = total ** 0.5
        if int(t) == t:
            return t

        return -1
