"""
https://leetcode.com/problems/check-if-the-number-is-fascinating/description/
"""


class Solution:
    """
    Solution
    """

    def is_fascinating(self, n: int) -> bool:
        """
        is fancinating
        """
        def get_digits(x: int) -> list[int]:
            digits: list[int] = []
            while x:
                x, r = divmod(x, 10)
                digits.append(r)

            return digits

        if n % 10 == 0:
            return False

        rslt = get_digits(n) + get_digits(2 * n) + get_digits(3 * n)
        if len(rslt) > 9 or 0 in rslt:
            return False

        return len(set(rslt)) == 9
