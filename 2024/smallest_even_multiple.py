"""
https://leetcode.com/problems/smallest-even-multiple/description/
"""


class Solution:
    """
    Solution
    """

    def smallest_even_multiple(self, n: int) -> int:
        """
        smallest even multiple
        """
        if n & 1:
            return n << 1

        return n
