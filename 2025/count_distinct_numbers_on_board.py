"""
https://leetcode.com/problems/count-distinct-numbers-on-board/description/
"""


class Solution:
    """
    Solution
    """

    def distinct_integers(self, n: int) -> int:
        """
        distinct integers
        """
        if n > 1:
            return n - 1

        return 1
