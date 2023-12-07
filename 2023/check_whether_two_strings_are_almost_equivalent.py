"""
https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/
"""


from string import ascii_lowercase
from collections import Counter


class Solution:
    """
    Solution
    """

    def check_almost_equivalent(self, word1: str, word2: str) -> bool:
        """
        check_almost_equivalent
        """
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return all(abs(cnt1[c] - cnt2[c]) <= 3 for c in ascii_lowercase)
