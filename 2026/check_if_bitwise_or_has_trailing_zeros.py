"""
https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/description/
"""


class Solution:
    """
    Solution
    """

    def has_trailing_zeros(self, nums: list[int]) -> bool:
        """
        has trailing zeros
        """
        has_zeros = False
        for x in nums:
            if x & 1 == 0:
                if has_zeros:
                    return True

                has_zeros = True

        return False
