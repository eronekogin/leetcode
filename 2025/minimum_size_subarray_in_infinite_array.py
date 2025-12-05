"""
https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/description/
"""


class Solution:
    """
    Solution
    """

    def min_size_subarray(self, nums: list[int], target: int) -> int:
        """
        min size subarray
        """
        total = sum(nums)
        n = len(nums)
        q, r = divmod(target, total)

        if r == 0:
            return q * n

        starts = {0: -1}
        curr_sum = 0
        rslt = n * 2 + 1
        for end, x in enumerate(nums + nums):
            curr_sum += x
            k = curr_sum - r
            if k in starts:
                rslt = min(rslt, end - starts[k])

            starts[curr_sum] = end

        if rslt == n * 2 + 1:
            return -1

        return q * n + rslt
