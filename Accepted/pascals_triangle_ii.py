"""
https://leetcode.com/problems/pascals-triangle-ii/
"""


from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        k = rowIndex + 1
        currRow = [0] * k
        currRow[0] = 1
        for row in range(1, k):
            # Adding the numbers from the right to the left for each
            # round of the loop.
            for col in range(row, 0, -1):
                currRow[col] += currRow[col - 1]

        return currRow


print(Solution().getRow(4))
