"""
https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/description/
"""


class Solution:
    """
    Solution
    """

    def max_palindromes(self, s: str, k: int) -> int:
        """
        max palindromes
        """
        n = len(s)
        start = 0
        cnt = 0
        for center in range((n << 1) - 1):
            l = center >> 1
            r = l + center % 2

            while l >= start and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    cnt += 1
                    start = r + 1
                    break

                l -= 1
                r += 1

        return cnt
