"""
https://leetcode.com/problems/ways-to-make-a-fair-array/description/
"""


class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        candidates = 0
        s1 = [0, 0]
        s2 = [sum(nums[0::2]), sum(nums[1::2])]
        for i, num in enumerate(nums):
            s2[i & 1] -= num  # Remove the current item.
            candidates += s1[0] + s2[1] == s1[1] + s2[0]  # Check if fair.
            s1[i & 1] += num  # Add back the current item to previous sums

        return candidates
