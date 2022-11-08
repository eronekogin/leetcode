"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
"""


from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = Counter(s).values()
        if len(set(freqs)) == len(freqs):
            return 0

        deletes = 0
        used: set[int] = set()
        for f in freqs:
            while f > 0 and f in used:
                f -= 1
                deletes += 1

            used.add(f)

        return deletes
