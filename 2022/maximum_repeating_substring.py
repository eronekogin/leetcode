"""
https://leetcode.com/problems/maximum-repeating-substring/
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0

        maxK = len(sequence) // len(word)
        for k in range(maxK, 0, -1):
            if word * k in sequence:
                return k

        return 0
