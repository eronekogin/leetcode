"""
https://leetcode.com/problems/jump-game/
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Use greedy algorithm to start back jumping from the
        end of nums.
        """
        # The last position of nums is able to jump onto itself.
        goodPos = len(nums) - 1
        for i in range(goodPos, -1, -1):
            if i + nums[i] >= goodPos:
                # We can jump from the current position to
                # the left most good position.
                goodPos = i

        return goodPos == 0  # If the first position is a good one.
