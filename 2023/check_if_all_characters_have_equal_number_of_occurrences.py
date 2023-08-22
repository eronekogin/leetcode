"""
https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
"""


from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = Counter(s)
        return len(set(cnt.values())) == 1
