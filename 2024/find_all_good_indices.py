"""
https://leetcode.com/problems/find-all-good-indices/description/
"""


class Solution:
    """
    Solution
    """

    def good_indices(self, nums: list[int], k: int) -> list[int]:
        """
        good indices
        """
        n = len(nums)

        lefts, rights = [1] * (n + 1), [1] * (n + 1)

        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                lefts[i] = lefts[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                rights[i] = rights[i + 1] + 1

        return [
            i
            for i in range(k, n - k)
            if lefts[i - 1] >= k and rights[i + 1] >= k
        ]
