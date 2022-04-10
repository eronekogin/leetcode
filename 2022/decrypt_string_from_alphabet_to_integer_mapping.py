"""
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
"""


from string import ascii_lowercase


class Solution:
    def freqAlphabets(self, s: str) -> str:
        rslt = []
        for c in s:
            if c == '#':
                rslt[-2:] = [rslt[-2] + rslt[-1]]
            else:
                rslt.append(c)

        return ''.join(ascii_lowercase[int(w) - 1] for w in rslt)
