"""
https://leetcode.com/problems/image-smoother/
"""


from typing import List


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if not M or not M[0]:
            return M

        R, C = len(M), len(M[0])
        DIRECTIONS = [
            (r, c)
            for r in range(-1, 2)
            for c in range(-1, 2)
            if r or c]
        rslt = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                total = cnt = 0
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        cnt += 1
                        total += M[nr][nc]

                rslt[r][c] = (total + M[r][c]) // (cnt + 1)

        return rslt
