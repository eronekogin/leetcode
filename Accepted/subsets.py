"""
https://leetcode.com/problems/subsets/
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Presumption: All numbers in nums are unique.
        # So we could use dynamic programming, which
        # dp[n] = dp[n - 1] + [item + [n] for item in dp[n - 1]].
        rslt = [[]]
        for n in nums:
            rslt += [item + [n] for item in rslt]

        return rslt


nums = [1, 4, 6, 8]
print(Solution().subsets(nums))
