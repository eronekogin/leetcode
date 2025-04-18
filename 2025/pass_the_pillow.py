"""
https://leetcode.com/problems/pass-the-pillow/description/
"""


class Solution:
    """
    Solution
    """

    def pass_the_pillow(self, n: int, time: int) -> int:
        """
        pass the pillow
        """
        curr_round, r = divmod(time, n - 1)

        if curr_round & 1:
            return n - r

        return r + 1
