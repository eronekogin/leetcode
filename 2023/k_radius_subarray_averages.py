"""
https://leetcode.com/problems/k-radius-subarray-averages/
"""


from itertools import accumulate


class Solution:
    """
    Solution
    """

    def get_averages(self, nums: list[int], k: int) -> list[int]:
        """
        get_averages
        """
        pre_sums = [0] + list(accumulate(nums))
        n = len(nums)
        rslt = [-1] * n
        diameter = (k << 1) + 1
        for i in range(k, n - k):
            rslt[i] = (pre_sums[i + k + 1] - pre_sums[i - k]) // diameter

        return rslt


print(Solution().get_averages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3))
