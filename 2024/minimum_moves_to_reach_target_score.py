"""
https://leetcode.com/problems/minimum-moves-to-reach-target-score/description/
"""


class Solution:
    """
    Solution
    """

    def min_moves(self, target: int, max_doubles: int) -> int:
        """
        min_moves
        """
        remain_doubles = max_doubles
        curr = target
        moves = 0
        while remain_doubles > 0 and curr > 1:
            curr, r = divmod(curr, 2)
            remain_doubles -= 1
            moves += 1 + r

        return moves + curr - 1
