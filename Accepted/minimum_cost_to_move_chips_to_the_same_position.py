"""
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
"""


from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """
        All the chips at odd position could be moved to the 1st index with no
        cost and all the chips at even position could be moved to the 0th index
        with no cost.

        Then we simply compare which position holds less chips, which will be
        our final cost to move all the chips to the same position.
        """
        odds = sum(p & 1 for p in position)
        return min(odds, len(position) - odds)
