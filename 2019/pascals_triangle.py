"""
https://leetcode.com/problems/pascals-triangle/
"""


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rslt = []
        for row in range(numRows):
            currRow = [1] * (row + 1)
            for col in range(1, row):  # Exclude the first and the last.
                currRow[col] = rslt[-1][col - 1] + rslt[-1][col]

            rslt.append(currRow)

        return rslt


print(Solution().generate(3))
