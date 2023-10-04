"""
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
"""


class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        sortedNums = sorted(nums)
        return min(
            [
                sortedNums[i + k - 1] - sortedNums[i]
                for i in range(len(sortedNums) - k + 1)
            ] or [0]
        )