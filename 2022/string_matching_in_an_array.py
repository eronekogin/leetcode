"""
https://leetcode.com/problems/string-matching-in-an-array/
"""


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        N = len(words)
        rslt = []
        sortedWords = sorted(words, key=len)
        for i, w in enumerate(sortedWords):
            if any(w in sortedWords[j] for j in range(i + 1, N)):
                rslt.append(w)

        return rslt
