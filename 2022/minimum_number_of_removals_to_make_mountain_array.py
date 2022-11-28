"""
https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/
"""


from bisect import bisect_left


class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        def lis(nums: list[int]):
            # Get the length of the longest increasing sequence at each index i.
            N = len(nums)
            sequence = [10**10] * N
            lensOfLis = [0] * N
            for i, num in enumerate(nums):
                lensOfLis[i] = bisect_left(sequence, num) + 1
                sequence[lensOfLis[i] - 1] = num

            return lensOfLis

        left, right = lis(nums), lis(nums[::-1])[::-1]
        maxLen = 0
        for i in range(len(nums)):
            if left[i] >= 2 and right[i] >= 2:
                maxLen = max(maxLen, left[i] + right[i] - 1)

        return len(nums) - maxLen
