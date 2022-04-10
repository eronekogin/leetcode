"""
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N = len(s)
        VOWELS = set('aeiouAEIOU')
        return sum(s[i] in VOWELS for i in range(N >> 1)) == \
            sum(s[i] in VOWELS for i in range(N >> 1, N))
