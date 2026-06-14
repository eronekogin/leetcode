"""
https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/description/
"""


class Solution:
    """
    Solution
    """

    def min_operations_to_make_median_k(self, nums: list[int], k: int) -> int:
        """
        min operations to make median k
        """
        nums.sort()
        n = len(nums)
        m = n >> 1

        if nums[m] == k:
            return 0

        if nums[m] < k:
            rslt = 0
            i = m
            while i < n and nums[i] <= k:
                rslt += k - nums[i]
                i += 1

            return rslt

        if nums[m] > k:
            rslt = 0
            i = m
            while i >= 0 and nums[i] >= k:
                rslt += nums[i] - k
                i -= 1

            return rslt

        return -1
