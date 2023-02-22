"""
https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/
"""


class Solution:
    def canChoose(self, groups: list[list[int]], nums: list[int]) -> bool:
        i = 0
        for group in groups:
            for ii in range(i, len(nums)):
                if nums[ii: ii + len(group)] == group:
                    i = ii + len(group)
                    break
            else:  # No matching subarray is found for the current group.
                return False

        return True
