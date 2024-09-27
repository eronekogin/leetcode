"""
https://leetcode.com/problems/strictly-palindromic-number/description/
"""


class Solution:
    """
    Solution
    """

    def is_strictly_palindromic(self, n: int) -> bool:
        """
        is strictly palindromic
        """
        def is_palindromic(radix: int):
            curr = n
            digits = []
            while curr:
                curr, r = divmod(curr, radix)
                digits.append(r)

            return digits == digits[::-1]

        return all(is_palindromic(x) for x in range(2, n - 1))
