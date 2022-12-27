"""
https://leetcode.com/problems/maximum-erasure-value/
"""


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        memo = set()
        maxScore = currScore = 0
        start = end = 0
        N = len(nums)
        while end < N:
            if nums[end] not in memo:
                memo.add(nums[end])
                currScore += nums[end]
                maxScore = max(maxScore, currScore)
                end += 1
            else:
                memo.remove(nums[start])
                currScore -= nums[start]
                start += 1

        return maxScore


print(Solution().maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))
