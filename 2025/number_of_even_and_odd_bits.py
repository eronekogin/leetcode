"""
https://leetcode.com/problems/number-of-even-and-odd-bits/description/
"""


class Solution:
    """
    Solution
    """

    def even_odd_bit(self, n: int) -> list[int]:
        """
        even odd bit
        """
        digits: list[int] = []
        while n:
            n, r = divmod(n, 2)
            digits.append(r)

        rslt = [0, 0]
        for i, d in enumerate(digits):
            if d == 0:
                continue

            rslt[i & 1] += 1

        return rslt
