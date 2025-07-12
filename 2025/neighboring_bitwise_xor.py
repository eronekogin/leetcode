"""
https://leetcode.com/problems/neighboring-bitwise-xor/description/
"""


class Solution:
    """
    Solution
    """

    def does_valid_array_exist(self, derived: list[int]) -> bool:
        """
        does valid array exists
        """
        return sum(derived) & 1 == 0
