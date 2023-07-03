"""
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
"""


class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        def rotate(mat: list[list[int]]):
            return [list(reversed(k)) for k in zip(*mat)]

        if mat == target:
            return True

        cols1 = rotate(mat)  # 90 degree
        if cols1 == target:
            return True
        
        cols2 = rotate(cols1)  # 180 degree
        if cols2 == target:
            return True
        
        cols3 = rotate(cols2)  # 270 degree
        return cols3 == target
