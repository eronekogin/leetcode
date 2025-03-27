"""
https://leetcode.com/problems/house-robber-iv/description/
"""


class Solution:
    """
    Solution
    """

    def min_capability(self, nums: list[int], k: int) -> int:
        """
        min capability
        """
        def can_rob(m: int):
            robbed = 0
            i = 0

            while i < n and robbed < k:
                if nums[i] <= m:
                    robbed += 1
                    i += 2
                else:
                    i += 1

            return robbed >= k

        l, r = 1, max(nums)
        n = len(nums)

        while l < r:
            m = l + ((r - l) >> 1)
            if can_rob(m):
                r = m
            else:
                l = m + 1

        return l


print(Solution().min_capability([2, 3, 5, 9], 2))
