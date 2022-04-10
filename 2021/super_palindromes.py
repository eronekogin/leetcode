"""
https://leetcode.com/problems/super-palindromes/
"""


from typing import Iterator


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        """
        1. The possible maximum range from the input is 10**18, which means the
            square root of the super palindrome numbers falls into 10**9.
        2. Then we could try to construct such square root for which we only
            need the first four digits to determine the whole number with
            format like xx, x0x, x1x, ... , x9x.
        3. Then we walk through those square root numbers and determine if its
            square is a palindrome.
        """
        def generate_palindrome() -> Iterator[int]:
            for i in range(1, 10):
                yield i

            for i in range(1, 10000):
                left = str(i)
                right = left[::-1]
                yield int(''.join([left, right]))
                for j in range(10):
                    yield int(''.join([left, str(j), right]))

        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        cnt, l, r = 0, int(left), int(right)
        for x in generate_palindrome():
            y = x * x
            if l <= y <= r and is_palindrome(str(y)):
                cnt += 1

        return cnt
