"""
https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/description/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def valid_partition(self, nums: list[int]) -> bool:
        """
        valid partition
        """
        @cache
        def dfs(start: int) -> bool:
            if start == n:  # Completed partition
                return True

            if start + 1 < n:
                if nums[start] == nums[start + 1]:
                    rslt = dfs(start + 2)
                    if start + 2 < n and nums[start + 1] == nums[start + 2]:
                        rslt = rslt or dfs(start + 3)

                    return rslt

                if nums[start + 1] - nums[start] == 1:
                    if start + 2 < n and nums[start + 2] - nums[start + 1] == 1:
                        return dfs(start + 3)

                    return False

            return False

        n = len(nums)
        return dfs(0)

    def valid_partition2(self, nums: list[int]) -> bool:
        """
        dp
        """
        dp = [True] + [False] * len(nums)

        for i, x in enumerate(nums):
            if i >= 1 and x == nums[i - 1]:
                dp[i + 1] |= dp[i - 1]

            if i >= 2 and (
                x == nums[i - 1] == nums[i - 2] or
                x == nums[i - 1] + 1 == nums[i - 2] + 2
            ):
                dp[i + 1] |= dp[i - 2]

        return dp[-1]
