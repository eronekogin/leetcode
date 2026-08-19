"""
https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
"""


class Solution:
    """
    Solution
    """

    def min_operations(self, nums: list[int]) -> int:
        """
        min operations
        """
        n = len(nums)
        cnt = 0

        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                cnt += 1

        if nums[-2] == 0 or nums[-1] == 0:
            return -1

        return cnt
