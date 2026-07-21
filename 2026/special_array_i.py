"""
https://leetcode.com/problems/special-array-i/description/
"""


class Solution:
    """
    Solution
    """

    def is_array_special(self, nums: list[int]) -> bool:
        """
        is array special
        """
        prev = nums[0] & 1
        for i in range(1, len(nums)):
            curr = nums[i] & 1
            if prev == curr:
                return False

            prev = curr

        return True
