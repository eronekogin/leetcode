"""
https://leetcode.com/problems/longest-uncommon-subsequence-ii/
"""


from typing import List
from collections import Counter


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def _is_sub_seq(s1: str, s2: str) -> bool:
            # The input string s1's length will be less than b when s1, s2 is
            # passed to this function. Here iter(s2) will generate an iterator
            # of s2, then we check if each char in s1 exists in s2 and follows
            # the same order as in s1.
            it2 = iter(s2)
            return all(c in it2 for c in s1)

        cnt = Counter(strs)
        candidates = sorted(cnt.keys(), key=lambda s: -len(s))
        for i, s1 in enumerate(candidates):
            if cnt[s1] == 1:
                if all(not _is_sub_seq(s1, candidates[j]) for j in range(i)):
                    return len(s1)

        return -1  # No solution found.
