"""
https://leetcode.com/problems/merge-strings-alternately/
"""


from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        rslt = []
        for x, y in zip_longest(word1, word2, fillvalue=''):
            rslt.extend([x, y])

        return ''.join(rslt)
