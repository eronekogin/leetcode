"""
https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def minimum_deletions(self, word: str, k: int) -> int:
        """
        minimum deletions
        """
        freqs = list(Counter(word).values())
        rslt = len(word) + 1
        for min_freq in freqs:
            deletions = 0
            for f in freqs:
                if min_freq > f:
                    deletions += f
                elif f >= min_freq + k:
                    deletions += f - (min_freq + k)

            rslt = min(rslt, deletions)

        return rslt
