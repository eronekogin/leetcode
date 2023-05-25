"""
https://leetcode.com/problems/maximum-subarray-min-product/
"""


from itertools import accumulate


class Solution:
    def maxSumMinProduct(self, nums: list[int]) -> int:
        prefix_sums = list(accumulate([0] + nums + [0]))
        left = []
        maxArea = 0
        for i, h in enumerate(nums + [0]):
            start = i
            while left and h <= left[-1][0]:
                prevH, prevStart = left.pop()
                maxArea = max(
                    maxArea, (prefix_sums[i] - prefix_sums[prevStart]) * prevH)
                start = prevStart
            left.append((h, start))
        return maxArea % (10 ** 9 + 7)
