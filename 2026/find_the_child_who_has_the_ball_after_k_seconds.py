"""
https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_child(self, n: int, k: int) -> int:
        """
        number of child
        """
        q, r = divmod(k, n - 1)
        if q & 1:
            return n - 1 - r

        return r
