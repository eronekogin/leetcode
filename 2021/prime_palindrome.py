"""
https://leetcode.com/problems/prime-palindrome/
"""


class Solution:
    def primePalindrome(self, N: int) -> int:
        """
        1. All palindrome numbers having even digits could be divided by 11.
            So only 11 is a prime, the remaining ones could be skipped.
        """
        def is_prime(x: int) -> bool:
            return x > 1 and all(x % d for d in range(2, int(x ** 0.5) + 1))

        def is_palindrome(x: int) -> bool:
            rslt = 0
            y = x
            while y:
                y, r = divmod(y, 10)
                rslt = 10 * rslt + r

            return rslt == x

        def get_digits(x: int) -> int:
            rslt = 0
            while x:
                x = x // 10
                rslt += 1

            return rslt

        rslt = N
        while True:
            if 8 <= rslt <= 11:
                return 11

            if is_palindrome(rslt) and is_prime(rslt):
                return rslt

            digits = get_digits(rslt)
            if digits & 1 == 0:  # The number has even digits.
                rslt = 10 ** digits + 1  # Skip to the next level.
            else:
                rslt += 1  # Continue to the next number.


print(Solution().primePalindrome(6))
