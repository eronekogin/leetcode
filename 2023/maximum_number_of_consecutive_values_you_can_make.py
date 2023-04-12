"""
https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/
"""


class Solution:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        """
        Sort the coins in ascending order, and suppose currMax is the current
        max number we can make from the coins, which means we can make numbers
        from 0 to currMax - 1, then we have:
            1. If currNum > currMax, we cannot make the currMax
                with any of the remaining numbers as they will be greater
                than the current number.
            2. If currNum <= currMax, we can make numbers from
                currNum to currNum + currMax - 1, so our next goal will just
                be currNum + currMax. 
        """
        currMax = 1
        for num in sorted(coins):
            if num > currMax:
                break

            currMax += num

        return currMax
