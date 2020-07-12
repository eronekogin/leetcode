"""
https://leetcode.com/problems/matchsticks-to-square/
"""


from typing import List


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        """
        Simple back tracking.
        """
        if not nums or len(nums) < 4:  # Does not have enough matchsticks.
            return False

        maxSideLen, remain = divmod(sum(nums), 4)
        if remain or any(stickLen > maxSideLen for stickLen in nums):
            # Sum of matchsticks could not be divided into 4 equal parts or
            # any matchstick's length could not fit into one side.
            return False

        memo = {}  # used matchstcik mask: can form a square or not flag.

        def form_a_new_side(usedMask: int, currSum: int) -> bool:
            if usedMask in memo:
                return memo[usedMask]

            completedSide, remain = divmod(currSum, maxSideLen)

            # Already completed 3 sides, then the left sticks must be able
            # to form the last side.
            if completedSide == 3 and not remain:
                memo[usedMask] = True
                return True

            # When coming here, check the remaining available space for the
            # unused matchsticks to complete a new side.
            availableLen = maxSideLen - remain
            for i, stickLen in enumerate(nums):
                chkMask = 1 << i
                if not usedMask & chkMask and stickLen <= availableLen and\
                        form_a_new_side(usedMask | chkMask, currSum + stickLen):
                    memo[usedMask] = True
                    return True

            memo[usedMask] = False
            return False  # Cannot form any new side.

        return form_a_new_side(0, 0)
