"""
https://leetcode.com/problems/spiral-matrix-iii/
"""


class Solution:
    def spiralMatrixIII(
            self,
            rows: int,
            cols: int,
            rStart: int,
            cStart: int) -> list[list[int]]:
        """
        1. The walk steps follows 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, ..., so
            in order to generate such sequence, we use a counter to stand for
            the index of this sequence and we could find that when index is
            odd, we increase the curret walk steps by 1.
        2. The spiral walks towards four directions from east, south, west,
            north. When any time we step onto a valid cell on the grid, we
            add it to the final results.
        """
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rslt = [(rStart, cStart)]
        cnt, walkSteps, toward = 0, 1, 0
        r, c = rStart, cStart
        while len(rslt) < rows * cols:
            dr, dc = DIRECTIONS[toward]
            for _ in range(1, walkSteps + 1):
                r += dr
                c += dc
                if 0 <= r < rows and 0 <= c < cols:
                    rslt.append((r, c))

            if cnt & 1:
                walkSteps += 1

            cnt += 1
            toward = (toward + 1) % 4

        return rslt
