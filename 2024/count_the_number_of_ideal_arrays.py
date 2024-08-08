"""
https://leetcode.com/problems/count-the-number-of-ideal-arrays/description/
"""


from functools import cache
from math import comb


class Solution:
    """
    Solution
    """

    def ideal_arrays(self, n: int, max_value: int) -> int:
        """
        idea arrays
        """
        @cache
        def dp(curr_end: int, size: int) -> int:
            rslt = comb(n - 1, size - 1)

            next_end = curr_end << 1

            if size == n or next_end > max_value:
                return rslt

            while next_end <= max_value:
                rslt += dp(next_end, size + 1)
                next_end += curr_end

            return rslt

        return sum(
            dp(i, 1)
            for i in range(1, max_value + 1)
        ) % (10 ** 9 + 7)
