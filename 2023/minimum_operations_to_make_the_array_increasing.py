"""
https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
"""


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ops = 0
        currMax = 0
        for num in nums:
            if num > currMax:
                currMax = num
                continue

            currMax += 1
            ops += currMax - num

        return ops
