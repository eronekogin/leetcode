"""
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
"""


class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        N = len(nums)
        positives = [0] * N
        negatives = [0] * N

        if nums[0] > 0:
            positives[0] = 1
        elif nums[0] < 0:
            negatives[0] = 1

        for i in range(1, N):
            if nums[i] > 0:
                positives[i] = 1 + positives[i - 1] if positives[i - 1] else 1
                negatives[i] = 1 + negatives[i - 1] if negatives[i - 1] else 0
            elif nums[i] < 0:
                positives[i] = 1 + negatives[i - 1] if negatives[i - 1] else 0
                negatives[i] = 1 + positives[i - 1] if positives[i - 1] else 1

        return max(positives)
