"""
https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/
"""


class Solution:
    """
    Solution
    """

    def sum_indices_with_k_set_bits(self, nums: list[int], k: int) -> int:
        """
        sum indices with k set bits
        """
        return sum(
            x
            for i, x in enumerate(nums)
            if i.bit_count() == k
        )
