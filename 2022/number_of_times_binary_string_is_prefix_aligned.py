"""
https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/
"""


class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        """
        If the current step equals the rightmost flipped bit, then it means
        all the previous bits are all flipped, so the current list is
        prefix-aligned.
        """
        rightmostOneBitIndex = 0
        cnt = 0
        for currStep, flippedIndex in enumerate(flips, 1):
            rightmostOneBitIndex = max(rightmostOneBitIndex, flippedIndex)
            cnt += rightmostOneBitIndex == currStep

        return cnt
