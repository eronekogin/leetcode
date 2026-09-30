"""
https://leetcode.com/problems/find-if-digit-game-can-be-won/description/
"""


class Solution:
    """
    Solution
    """

    def can_alice_win(self, nums: list[int]) -> bool:
        """
        can alice win
        """
        l = r = 0
        for x in nums:
            if x < 10:
                l += x
            else:
                r += x

        return l != r
