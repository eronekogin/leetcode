"""
https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/
"""


class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        R, C = len(grid) - 1, len(grid[0]) - 1
        cells: list[list[int]] = [(0, 0, grid[0][0])]
        visited: set[tuple[int]] = {(0, 0)}
        for r, c, t in cells:
            if r == R and c == C:
                return True

            if t == 1:
                if c - 1 >= 0 and grid[r][c - 1] in [1, 4, 6] and (r, c - 1) not in visited:
                    cells.append((r, c - 1, grid[r][c - 1]))
                    visited.add((r, c - 1))

                if c + 1 <= C and grid[r][c + 1] in [1, 3, 5] and (r, c + 1) not in visited:
                    cells.append((r, c + 1, grid[r][c + 1]))
                    visited.add((r, c + 1))
            elif t == 2:
                if r - 1 >= 0 and grid[r - 1][c] in [2, 3, 4] and (r - 1, c) not in visited:
                    cells.append((r - 1, c, grid[r - 1][c]))
                    visited.add((r - 1, c))

                if r + 1 <= R and grid[r + 1][c] in [2, 5, 6] and (r + 1, c) not in visited:
                    cells.append((r + 1, c, grid[r + 1][c]))
                    visited.add((r + 1, c))
            elif t == 3:
                if c - 1 >= 0 and grid[r][c - 1] in [1, 4, 6] and (r, c - 1) not in visited:
                    cells.append((r, c - 1, grid[r][c - 1]))
                    visited.add((r, c - 1))

                if r + 1 <= R and grid[r + 1][c] in [2, 5, 6] and (r + 1, c) not in visited:
                    cells.append((r + 1, c, grid[r + 1][c]))
                    visited.add((r + 1, c))
            elif t == 4:
                if c + 1 <= C and grid[r][c + 1] in [1, 3, 5] and (r, c + 1) not in visited:
                    cells.append((r, c + 1, grid[r][c + 1]))
                    visited.add((r, c + 1))

                if r + 1 <= R and grid[r + 1][c] in [2, 5, 6] and (r + 1, c) not in visited:
                    cells.append((r + 1, c, grid[r + 1][c]))
                    visited.add((r + 1, c))
            elif t == 5:
                if r - 1 >= 0 and grid[r - 1][c] in [2, 3, 4] and (r - 1, c) not in visited:
                    cells.append((r - 1, c, grid[r - 1][c]))
                    visited.add((r - 1, c))

                if c - 1 >= 0 and grid[r][c - 1] in [1, 4, 6] and (r, c - 1) not in visited:
                    cells.append((r, c - 1, grid[r][c - 1]))
                    visited.add((r, c - 1))
            else:
                if r - 1 >= 0 and grid[r - 1][c] in [2, 3, 4] and (r - 1, c) not in visited:
                    cells.append((r - 1, c, grid[r - 1][c]))
                    visited.add((r - 1, c))

                if c + 1 <= C and grid[r][c + 1] in [1, 3, 5] and (r, c + 1) not in visited:
                    cells.append((r, c + 1, grid[r][c + 1]))
                    visited.add((r, c + 1))

        return False


print(Solution().hasValidPath([[1, 1, 1, 1, 1, 1, 3]]))
