"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        stepCnt = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1

            stepCnt += 1

        return stepCnt
