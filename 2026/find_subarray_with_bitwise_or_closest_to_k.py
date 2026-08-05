"""
https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/description/
"""


from math import inf


class Solution:
    """
    Solution
    """

    def minimum_difference(self, nums: list[int], k: int) -> int:
        """
        nums[j] stores the or sum from subarray [j, i]
        """
        rslt = inf
        for i, x in enumerate(nums):
            rslt = min(rslt, abs(x - k))
            j = i - 1
            while j >= 0 and nums[j] | x != nums[j]:
                nums[j] |= x
                rslt = min(rslt, abs(nums[j] - k))
                j -= 1

        return int(rslt)
