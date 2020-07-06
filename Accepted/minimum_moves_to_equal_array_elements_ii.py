"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
"""


from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()  # Sort the input list in ascending order.

        # 1. Then the median will be our number in the final list.
        # 2. nums[~i] - nums[i] = (nums[~i] - nums[m]) + (nums[m] - nums[i]),
        #   so the total moves for nums[~i] and nums[i] is nums[~i] - nums[i].
        return sum(nums[~i] - nums[i] for i in range((len(nums) >> 1)))
