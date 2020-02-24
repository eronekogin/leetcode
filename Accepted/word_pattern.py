"""
https://leetcode.com/problems/word-pattern/
"""


class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        p, w = pattern, string.split()
        return len(set(zip(p, w))) == len(set(p)) == len(set(w)) and\
            len(p) == len(w)
