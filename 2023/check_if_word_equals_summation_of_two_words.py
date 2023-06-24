"""
https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
"""


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def calc_value(s: str):
            N = len(s)
            OFFSET = ord('a')
            rslt = 0
            for i, c in enumerate(s):
                rslt += (ord(c) - OFFSET) * 10 ** (N - 1 - i)
            
            return rslt

        return calc_value(firstWord) + calc_value(secondWord) == calc_value(targetWord)

        