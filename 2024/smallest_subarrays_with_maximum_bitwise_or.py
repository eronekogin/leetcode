"""
https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/description/
"""


class Solution:
    """
    Solution
    """

    def smallest_subarrays(self, nums: list[int]) -> list[int]:
        """
        smallest subarrays
        """
        last_one_bit = [0] * 32
        n = len(nums)
        rslt = [0] * n

        for i in reversed(range(n)):
            for j in range(32):
                if nums[i] & (1 << j):
                    last_one_bit[j] = i

            rslt[i] = max(1, max(last_one_bit) - i + 1)

        return rslt
