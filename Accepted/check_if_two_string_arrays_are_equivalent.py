"""
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
"""


from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        iw1 = iw2 = ic1 = ic2 = 0
        N1, N2 = len(word1), len(word2)
        while iw1 < N1 and iw2 < N2 and word1[iw1][ic1] == word2[iw2][ic2]:
            ic1 += 1
            ic2 += 1
            if ic1 == len(word1[iw1]):  # w1 is exhuasted.
                iw1 += 1
                ic1 = 0

            if ic2 == len(word2[iw2]):  # w2 is exhuasted.
                iw2 += 1
                ic2 = 0

        return iw1 == N1 and iw2 == N2
