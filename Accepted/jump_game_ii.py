"""
https://leetcode.com/problems/jump-game-ii/
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Use Breadth First Search (=BFS) with greedy algorithm:
        for [2, 3, 1, 1, 4]:
            jump#0: 0, 0
            jump#1: 0, 2
            jump#2: 2, 4

        For each jump, counts the maximum position the current node between the
        range could reach (i + nums[i]). Then if a jump contains a position
        >= the end position of nums, it means it will take current jump
        times to get to the end of the nums list.
        """
        endPos = len(nums) - 1
        if endPos <= 0:  # Less than 2 elements, no need to jump.
            return 0

        currMaxPos, step, currPos = 0, 0, 0
        while currMaxPos < endPos:
            step += 1  # Need a new jump.
            nextMaxPos = 0
            for i in range(currPos, currMaxPos + 1):
                nextMaxPos = max(nextMaxPos, i + nums[i])
                if nextMaxPos >= endPos:
                    # No need to calculate the remaining
                    # when the first one is found.
                    return step

            currPos = currMaxPos
            currMaxPos = nextMaxPos

        return 0  # Should not come here.


nums = [2, 3, 1, 1, 4]
print(Solution().jump(nums))
