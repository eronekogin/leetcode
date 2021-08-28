"""
https://leetcode.com/problems/binary-prefix-divisible-by-5/
"""


class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        N = len(nums)
        currSum = 0
        rslt = [False] * N
        for i, v in enumerate(nums):
            currSum += v * (1 << (N - 1 - i))
            if currSum % 5 == 0:
                rslt[i] = True

        return rslt
