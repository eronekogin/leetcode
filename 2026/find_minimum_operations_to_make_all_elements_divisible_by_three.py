"""
https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_operations(self, nums: list[int]) -> int:
        """
        minimum operations
        """
        return sum(
            x % 3 != 0
            for x in nums
        )
