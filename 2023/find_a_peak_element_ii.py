"""
https://leetcode.com/problems/find-a-peak-element-ii/
"""


class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        R, C = len(mat), len(mat[0])
        startCol, endCol = 0, C - 1

        while startCol <= endCol:
            maxRow = 0
            midCol = startCol + ((endCol - startCol) >> 1)

            # Find the current maximum value in the mid column.
            for r in range(R):
                if mat[r][midCol] >= mat[maxRow][midCol]:
                    maxRow = r
            
            isLeftBig = midCol - 1 >= startCol and mat[maxRow][midCol - 1] > mat[maxRow][midCol]
            isRightBig = midCol + 1 <= endCol and mat[maxRow][midCol + 1] > mat[maxRow][midCol]

            if (not isLeftBig) and (not isRightBig):
                return [maxRow, midCol]
            
            if isRightBig:
                # On the right side there is a number that is greater than all the values in the midCol.
                # So we have to move midCol to the righter side.
                startCol = midCol + 1
            else:
                endCol = midCol - 1
        
        return []  # No peak found.
            

