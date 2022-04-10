"""
https://leetcode.com/problems/bulls-and-cows/
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        ms, mg = {}, {}
        for i, s in enumerate(secret):
            g = guess[i]
            if s == g:
                bulls += 1
            else:
                ms[s] = ms.get(s, 0) + 1
                mg[g] = mg.get(g, 0) + 1

        for k in ms:
            if k in mg:
                cows += min(ms[k], mg[k])

        return '{0}A{1}B'.format(bulls, cows)
