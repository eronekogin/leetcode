"""
https://leetcode.com/problems/number-of-digit-one/
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        See the 2nd solution in
        https://leetcode.com/articles/number-of-digit-one/.
        """
        rslt, i = 0, 1
        while i <= n:
            divider = i * 10
            q, r = divmod(n, divider)
            rslt += q * i + min(max(r - i + 1, 0), i)
            i = divider

        return rslt
