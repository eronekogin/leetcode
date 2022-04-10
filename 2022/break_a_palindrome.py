"""
https://leetcode.com/problems/break-a-palindrome/
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''  # Not possible.

        candidate = None
        for i, c in enumerate(palindrome):
            if c != 'a':
                candidate = palindrome[:i] + 'a' + palindrome[i + 1:]
                break

        # When all the chars are a.
        if not candidate or set(candidate) == {'a'}:
            return palindrome[:-1] + 'b'

        return candidate


print(Solution().breakPalindrome('a'))
