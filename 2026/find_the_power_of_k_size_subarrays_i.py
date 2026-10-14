"""
https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/
"""


class Solution:
    """
    Solution
    """

    def results_array(self, nums: list[int], k: int) -> list[int]:
        """
        results array
        """
        if k == 1:
            return nums

        n = len(nums)
        rslt = [-1] * (n - k + 1)
        seq_len = 1

        for i in range(n - 1):
            if nums[i] + 1 == nums[i + 1]:
                seq_len += 1
            else:
                seq_len = 1

            if seq_len >= k:
                rslt[i - k + 2] = nums[i + 1]

        return rslt
