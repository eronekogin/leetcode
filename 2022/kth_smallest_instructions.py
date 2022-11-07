"""
https://leetcode.com/problems/kth-smallest-instructions/
"""


from math import comb


class Solution:
    def kthSmallestPath(self, destination: list[int], k: int) -> str:
        R, C = destination
        remainV = R
        totalSteps = R + C
        rslt: list[str] = []
        for i in range(totalSteps):
            remainSteps = totalSteps - (i + 1)
            numberOfWays = comb(remainSteps, remainV)
            if numberOfWays >= k:
                rslt.append('H')
            else:
                remainV -= 1
                k -= numberOfWays
                rslt.append('V')

        return ''.join(rslt)
