"""
https://leetcode.com/problems/running-sum-of-1d-array/
"""


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefixSums: list[int] = [0]
        for num in nums:
            prefixSums.append(prefixSums[-1] + num)

        return prefixSums[1:]
