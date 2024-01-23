"""
https://leetcode.com/problems/a-number-after-a-double-reversal/description/
"""


class Solution:
    """
    Solution
    """

    def is_same_after_reversals(self, num: int) -> bool:
        """
        is_same_after_reversals
        """
        if num == 0:
            return True

        return num % 10 != 0
