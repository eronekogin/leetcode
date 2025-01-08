"""
https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_cuts(self, n: int) -> int:
        """
        number of cuts
        """
        if n == 1:
            return 0

        if n & 1:
            return n

        return n >> 1
