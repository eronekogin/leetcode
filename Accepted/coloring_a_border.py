"""
https://leetcode.com/problems/coloring-a-border/
"""


from typing import Iterator


class Solution:
    def colorBorder(
        self,
        grid: list[list[int]],
        row: int,
        col: int,
        color: int
    ) -> list[list[int]]:
        def neighbors(r: int, c: int) -> Iterator[tuple[int]]:
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                    yield (nr, nc)

        def is_boarder_cell(r: int, c: int) -> bool:
            if (r == 0 or r == R - 1 or c == 0 or c == C - 1):
                return True

            return False

        def get_boarder_cells() -> list[list[int]]:
            currCells = [(row, col)]
            boarderCells = set()
            while currCells:
                nextCells = []
                for r, c in currCells:
                    visited.add((r, c))
                    if is_boarder_cell(r, c):
                        boarderCells.add((r, c))

                    for nr, nc in neighbors(r, c):
                        if grid[nr][nc] == grid[r][c]:
                            nextCells.append((nr, nc))
                        else:
                            boarderCells.add((r, c))
                            visited.add((r, c))

                currCells = nextCells

            return boarderCells

        R, C = len(grid), len(grid[0])
        visited = set()
        for r, c in get_boarder_cells():
            grid[r][c] = color

        return grid


print(Solution().colorBorder([[1, 1], [1, 2]], 0, 0, 3))
