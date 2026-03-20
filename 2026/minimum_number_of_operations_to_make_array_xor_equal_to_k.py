"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/
"""


class Solution:
    """
    Solution
    """

    def min_operations(self, nums: list[int], k: int) -> int:
        """
        min operations
        """
        xors = 0
        for x in nums:
            xors ^= x

        diff = 0
        while xors or k:
            diff += (xors & 1) != (k & 1)
            xors >>= 1
            k >>= 1

        return diff
