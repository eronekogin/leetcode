"""
https://leetcode.com/problems/valid-perfect-square/
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        Use binary search.
        """
        l, r = 0, num
        while l <= r:
            m = l + ((r - l) >> 1)
            if m * m > num:
                r = m - 1
            elif m * m < num:
                l = m + 1
            else:
                return True

        return False

    def isPerfectSquare2(self, num: int) -> bool:
        """
        Use Newton's method:
        x2 = x1 - f(x1) / f'(x1), while f'(x) is the deravative of f(x).

        For our case:
        x2 = x1 - (x1^2 - num) / 2 * x1 = (x1 + num / x1) / 2.
        """
        x = num
        while x * x > num:
            x = (x + num // x) >> 1

        return x * x == num


print(Solution().isPerfectSquare(16))
