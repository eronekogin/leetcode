"""
https://leetcode.com/problems/minimum-array-length-after-pair-removals/description/
"""


class Solution:
    """
    Solution
    """

    def min_length_after_removals(self, nums: list[int]) -> int:
        """
        min length after removals
        """
        n = len(nums)
        m = n >> 1
        is_odd = n & 1

        deletes = 0
        for i in range(m - 1, -1, -1):
            deletes += (nums[i] < nums[i + m + is_odd]) * 2

        return n - deletes


print(Solution().min_length_after_removals([1, 1, 2, 2, 3, 3]))
