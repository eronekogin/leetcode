"""
https://leetcode.com/problems/goat-latin/
"""


class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels, suffix1, suffix2 = set('AEIOUaeiou'), 'ma', 'a'
        rslt = S.split()
        for i, w in enumerate(rslt):
            suffix = [suffix2] * (i + 1)
            if w[0] in vowels:
                rslt[i] = ''.join([w, suffix1] + suffix)
            else:
                rslt[i] = ''.join([w[1:], w[0], suffix1] + suffix)

        return ' '.join(rslt)
