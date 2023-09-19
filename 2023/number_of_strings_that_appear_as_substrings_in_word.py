"""
https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
"""


from functools import cache


class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        @cache
        def isExisting(pattern: str):
            return pattern in word
        
        return sum(isExisting(p) for p in patterns)        