"""
https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/
"""


class Solution:
    def reconstructMatrix(
        self,
        upper: int,
        lower: int,
        colsum: list[int]
    ) -> list[list[int]]:
        N = len(colsum)
        upperList, lowerList = [0] * N, [0] * N
        remainUpper, remainLower = upper, lower
        for i, c in enumerate(colsum):
            if c == 2:
                upperList[i] = 1
                lowerList[i] = 1
                remainUpper -= 1
                remainLower -= 1
            elif c == 1:
                if remainUpper >= remainLower:
                    upperList[i] = 1
                    remainUpper -= 1
                else:
                    lowerList[i] = 1
                    remainLower -= 1

        if remainUpper == 0 and remainLower == 0:
            return [upperList, lowerList]

        return []
