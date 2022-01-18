"""
https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/
"""


class CustomFunction:
    def f(self, x, y):
        pass


class Solution:
    def findSolution(self, customfunction: CustomFunction, z: int) -> list[list[int]]:
        """
        Rephrase the problem:
            Given a matrix, each row and each column is increasing.
            Find all coordinates (i,j) that A[i][j] == z
        """
        rslt = []
        y = 1000
        for x in range(1, 1001):
            while y > 1 and customfunction.f(x, y) > z:
                y -= 1

            if customfunction.f(x, y) == z:
                rslt.append([x, y])

        return rslt
