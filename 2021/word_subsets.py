"""
https://leetcode.com/problems/word-subsets/
"""


from collections import Counter


class Solution:
    def wordSubsets(self, A: list[str], B: list[str]) -> list[str]:
        maxCnt = Counter()
        for cnt in map(Counter, B):
            maxCnt |= cnt

        return [a for a in A if not maxCnt - Counter(a)]
