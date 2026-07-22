"""
https://leetcode.com/problems/special-array-ii/description/
"""


class Solution:
    """
    Solution
    """

    def is_array_special(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        """
        is array special
        """
        prev = nums[0] & 1
        parities = [prev]
        for i in range(1, len(nums)):
            curr = nums[i] & 1
            parities.append(parities[-1] + (curr == prev))
            prev = curr

        return [
            parities[end] == parities[start]
            for start, end in queries
        ]
