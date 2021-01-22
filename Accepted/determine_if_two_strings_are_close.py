"""
https://leetcode.com/problems/determine-if-two-strings-are-close/
"""


from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        return sorted(Counter(word1).values()) == sorted(
            Counter(word2).values())
