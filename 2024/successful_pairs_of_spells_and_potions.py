"""
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
"""

from bisect import bisect_right


class Solution:
    """
    Solution
    """

    def successful_pairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        successful pairs
        """
        sorted_potions = sorted(success / x for x in potions)
        return [
            bisect_right(sorted_potions, x)
            for x in spells
        ]
