"""
https://leetcode.com/problems/subsets-ii/
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        rslt, ref = [[]], {}
        # [1, 2] and [2, 1] are taken as the same subset, so have to
        # sort the nums first to prevent duplicate subsets.
        for n in sorted(nums):
            usedList = rslt.copy()
            rslt += [item + [n] for item in rslt if item not in ref.get(n, [])]
            ref[n] = usedList

        return rslt


nums = [2, 2, 1, 2]
print(Solution().subsetsWithDup(nums))
