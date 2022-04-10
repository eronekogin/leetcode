"""
https://leetcode.com/problems/valid-palindrome-ii/
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # When s[left] is not the same as s[right], if deleting one
                # of them could make the remaining string palindrome, we
                # simply check if the remaining string is palindrome.
                deleteLeft = s[left + 1: right + 1]
                deleteRight = s[left: right]
                return deleteLeft == deleteLeft[::-1] or \
                    deleteRight == deleteRight[::-1]

        return True


print(Solution().validPalindrome('abca'))
