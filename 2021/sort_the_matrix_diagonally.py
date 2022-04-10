"""
https://leetcode.com/problems/sort-the-matrix-diagonally/
"""


from typing import List, Iterable


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def diagonal_items(r: int, c: int) -> Iterable[int]:
            while r < R and c < C:
                yield mat[r][c]
                r += 1
                c += 1

        def do(r: int, c: int) -> None:
            for v in sorted(diagonal_items(r, c)):
                mat[r][c] = v
                r += 1
                c += 1

        R, C = len(mat), len(mat[0])

        # First going down.
        for r in range(R):
            do(r, 0)

        # Then going right.
        for c in range(1, C):
            do(0, c)

        return mat
