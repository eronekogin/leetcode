"""
https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/
"""


class Solution:
    """
    Solution
    """

    def min_bit_flips(self, start: int, goal: int) -> int:
        """
        min bit flips
        """
        flips = 0
        while start or goal:
            if start & 1 != goal & 1:
                flips += 1

            start >>= 1
            goal >>= 1

        return flips
