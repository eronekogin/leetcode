"""
https://leetcode.com/problems/split-two-strings-to-make-palindrome/
"""


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_palindrome(s: str, start: int, end: int) -> bool:
            while start < end and s[start] == s[end]:
                start += 1
                end -= 1

            return start >= end

        def combine(a: str, b: str) -> bool:
            l, r = 0, len(a) - 1
            while l < r and a[l] == b[r]:
                l += 1
                r -= 1

            return l >= r or is_palindrome(a, l, r) or is_palindrome(b, l, r)

        return combine(a, b) or combine(b, a)


print(Solution().checkPalindromeFormation("pvhmupgqeltozftlmfjjde",
                                          "yjgpzbezspnnpszebzmhvp"))
