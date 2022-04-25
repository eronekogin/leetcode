"""
https://leetcode.com/problems/lucky-numbers-in-a-matrix/
"""


class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        maxColNums = {max(col) for col in zip(*matrix)}
        minRowNums = {min(row) for row in matrix}
        return list(maxColNums & minRowNums)


print(Solution().luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
