"""
https://leetcode.com/problems/pacific-atlantic-water-flow/
"""


from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return None

        R, C = len(matrix), len(matrix[0])
        visited = [[0] * C for _ in range(R)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rslt = []

        def fill(r: int, c: int, src: int):
            if visited[r][c] + src == 0:
                # The current cell was filled by another source before and now
                # it was filled by the new source, which means both oceans
                # could reach to this cell.
                rslt.append((r, c))

            visited[r][c] = src  # Fill the current cell with water.
            for dr, dc in directions:  # Try to fill its neighbors.
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] >=\
                        matrix[r][c] and visited[nr][nc] != src:
                    # The water could only fill when the neighbor's height
                    # >= the current cell, so that the water could flow from
                    # the neigbor to the current cell.
                    fill(nr, nc, src)

        # Try to fill water from Pacific ocean first.
        for r in range(R):  # Start at the leftmost cell for each row.
            fill(r, 0, 1)

        for c in range(C):  # Start at the topmost cell for each column.
            fill(0, c, 1)

        # Then fill water from the Atlantic ocean.
        for r in range(R):  # Start at the rightmost cell for each row.
            fill(r, C - 1, -1)

        for c in range(C):  # Start at the bottommost cell for each column.
            fill(R - 1, c, -1)

        return rslt


print(Solution().pacificAtlantic(
    [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
))
