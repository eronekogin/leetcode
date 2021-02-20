"""
https://leetcode.com/problems/number-of-matching-subsequences/
"""


from collections import defaultdict
from bisect import bisect_left


class Solution:
    def numMatchingSubseq(self, S: str, words: list[str]) -> int:
        def is_sub_seq(w: str) -> bool:
            searchStartIdx = 0
            for c in w:
                if c not in memo:
                    return False

                candidates = memo[c]
                firstMatch = bisect_left(candidates, searchStartIdx)
                if firstMatch == len(candidates):  # Not found.
                    return False

                searchStartIdx = candidates[firstMatch] + 1

            return True

        memo = defaultdict(list)
        for i, c in enumerate(S):
            memo[c].append(i)

        return sum(is_sub_seq(w) for w in words)


print(Solution().numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))
