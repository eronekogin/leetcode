"""
https://leetcode.com/problems/shortest-completing-word/
"""


from typing import List

from collections import Counter


class Solution:
    def shortestCompletingWord(
            self, licensePlate: str, words: List[str]) -> str:
        # Count letters in the licensePlate first.
        requiredLetters = Counter(
            c.lower() for c in licensePlate if c.isalpha())

        # Check words.
        return min(
            [w for w in words if not (requiredLetters - Counter(w))],
            key=len)
