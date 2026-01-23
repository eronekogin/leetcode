"""
https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/description/
"""


from functools import cache


class Solution:
    """
    Docstring for Solution
    """

    def min_increment_operations(self, nums: list[int], k: int) -> int:
        """
        dp1 means to increase at index i - 3 and go to the next subarray
        dp2 means to increase at index i - 2 and go to the next subarray
        dp3 means to increase at index i - 1 and go to the next subarray
        """
        dp1 = dp2 = dp3 = 0

        for x in nums:
            dp1, dp2, dp3 = (
                dp2,
                dp3,
                min(dp1, dp2, dp3) + max(k - x, 0)
            )

        return min(dp1, dp2, dp3)

    def min_increment_operations2(self, nums: list[int], k: int) -> int:
        """
        Docstring for min_increment_operations2

        :param self: Description
        :param nums: Description
        :type nums: list[int]
        :param k: Description
        :type k: int
        :return: Description
        :rtype: int
        """
        @cache
        def dfs(start: int) -> int:
            if start + 3 > n:
                return 0

            op1 = max(k - nums[start], 0) + dfs(start + 1)
            op2 = max(k - nums[start + 1], 0) + dfs(start + 2)
            op3 = max(k - nums[start + 2], 0) + dfs(start + 3)

            return min(op1, op2, op3)

        n = len(nums)
        return dfs(0)
