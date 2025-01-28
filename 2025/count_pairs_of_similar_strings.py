"""
https://leetcode.com/problems/count-pairs-of-similar-strings/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def similar_pairs(self, words: list[str]) -> int:
        """
        similar pairs
        """
        cnt = 0
        freqs = Counter()
        for w in words:
            m = frozenset(w)
            cnt += freqs[m]
            freqs[m] += 1

        return cnt
