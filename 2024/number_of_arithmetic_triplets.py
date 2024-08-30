"""
https://leetcode.com/problems/number-of-arithmetic-triplets/description/
"""


class Solution:
    """
    Solution
    """

    def arithmetic_triplets(self, nums: list[int], diff: int) -> int:
        """
        arithmetic triplets
        """
        memo = set(nums)
        return sum(
            x + diff in memo and x + diff + diff in memo
            for x in nums[:-2]
        )
