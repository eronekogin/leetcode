"""
https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/description/
"""


class Solution:
    """
    Solution
    """

    def max_consecutive(self, bottom: int, top: int, special: list[int]) -> int:
        """
        max consecutive
        """
        sorted_floors = sorted([bottom - 1, top + 1] + special)

        return max(
            y - x - 1
            for x, y in zip(sorted_floors, sorted_floors[1:])
        )
