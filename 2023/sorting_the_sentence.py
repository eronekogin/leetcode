"""
https://leetcode.com/problems/sorting-the-sentence/
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        N = len(words)
        rslt = [''] * N
        for w in words:
            ow = w[:-1]
            i = int(w[-1]) - 1
            rslt[i] = ow

        return ' '.join(rslt)
