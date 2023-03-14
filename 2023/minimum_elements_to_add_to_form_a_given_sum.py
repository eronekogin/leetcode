"""
https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/
"""

from math import ceil


class Solution:
    def minElements(self, nums: list[int], limit: int, goal: int) -> int:
        return ceil(abs(sum(nums) - goal) / limit)


print(Solution().minElements([2, 5, 5, -7, 4], 7, 464680098))
