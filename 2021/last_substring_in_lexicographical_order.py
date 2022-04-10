"""
https://leetcode.com/problems/last-substring-in-lexicographical-order/
"""


class Solution:
    def lastSubstring(self, s: str) -> str:
        """
        1. Use two points to stands for two positions to compare on which 
            substring starting at those positions is the largest substring.
        2. When two starting position contain the same char, check the next
            char right following it by taking advantage of an offset to
            indicate what is the next char to compare.
        """
        first, second, offset = 0, 1, 0
        N = len(s)
        while first + offset < N and second + offset < N:
            if s[first + offset] == s[second + offset]:
                offset += 1
            else:
                if s[first + offset] < s[second + offset]:
                    first += offset + 1
                else:
                    second += offset + 1

                if first == second:
                    second += 1

                offset = 0

        return s[first:]
