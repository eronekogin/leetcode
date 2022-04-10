"""
https://leetcode.com/problems/integer-break/
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        1. For any n >= 4, if we replace it with 2 * (n - 2),
            then 2n - 4 = n + n - 4 >= n. In this case we never need n to be
            one of the factor in the maximized product.
        2. Then we are left with 1, 2, 3 to choose and 1 is a waste of time.
        3. Then 3 * 3 > 2 * 2 * 2, so as a final factor, we should never use 2
            more than twice.
        """
        if n < 4:  # n = 2, rslt = 1 * 1; n = 3, rslt = 1 * 2.
            return n - 1
        elif n % 3 == 0:  # n = 3k, rslt = 3^k
            return 3 ** (n // 3)
        elif n % 3 == 1:  # n = 3k + 1 = 3(k - 1) + 4, rslt = 2*2*3^(k - 1).
            return 2 * 2 * 3 ** ((n - 4) // 3)
        else:  # n = 3k + 2, rslt = 2 * 3 ^ k.
            return 2 * 3 ** (n // 3)
