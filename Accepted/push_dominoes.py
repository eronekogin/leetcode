"""
https://leetcode.com/problems/push-dominoes/
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        boarders = [(v, i) for i, v in enumerate(dominoes) if v != '.']
        boarders = [('L', -1)] + boarders + [('R', len(dominoes))]
        rslt = list(dominoes)
        for (vl, il), (vr, ir) in zip(boarders, boarders[1:]):
            if vl == vr:  # Case L..L or R..R.
                rslt[il + 1: ir] = [vl] * (ir - il - 1)
            elif vl > vr:  # Case R...L
                totalLen = ir - il - 1
                m = totalLen >> 1
                rslt[il + 1: il + 1 + m] = [vl] * m
                rslt[il + m + 1 + (totalLen & 1): ir] = [vr] * m

        return ''.join(rslt)


print(Solution().pushDominoes2(".L.R...LR..L.."))
