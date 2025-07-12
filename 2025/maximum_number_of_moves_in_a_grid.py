"""
https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/
"""


class Solution:
    """
    Solution
    """

    def max_moves(self, grid: list[list[int]]) -> int:
        """
        max moves
        """
        m, n = len(grid), len(grid[0])
        curr_nodes = [(r, 0) for r in range(m)]
        moves = 0
        visited: set[tuple[int, int]] = set()
        while curr_nodes:
            next_nodes: list[tuple[int, int]] = []
            for r, c in curr_nodes:
                for nr, nc in [(r - 1, c + 1), (r, c + 1), (r + 1, c + 1)]:
                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] > grid[r][c] and
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        next_nodes.append((nr, nc))

            curr_nodes = next_nodes
            moves += (len(curr_nodes) > 0)

        return moves


print(Solution().max_moves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]))
