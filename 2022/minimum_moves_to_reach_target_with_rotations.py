"""
https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/
"""


class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        """
        Use the position (r, c) of the tail of the snake together with the
        row difference between head and tail dr to mark where the snake
        currently is. Then use BFS to find the answer.
        """
        N = len(grid)
        GOAL = (N - 1, N - 2, 0)
        queue: list[tuple[int]] = [(0, 0, 0, 0)]
        visited = set()
        for r, c, dr, steps in queue:
            if (r, c, dr) == GOAL:
                return steps

            if (r, c, dr) not in visited:
                visited.add((r, c, dr))
                if dr:  # Current is vertical.
                    if c + 1 < N and grid[r][c + 1] + grid[r + 1][c + 1] == 0:
                        queue.extend([
                            (r, c + 1, 1, steps + 1),  # Move right.
                            (r, c, 0, steps + 1)  # Rotate counter-clockwise.
                        ])

                    if r + 2 < N and grid[r + 2][c] == 0:
                        queue.append((r + 1, c, 1, steps + 1))  # Move down.
                else:  # Current is horizontal.
                    if r + 1 < N and grid[r + 1][c] + grid[r + 1][c + 1] == 0:
                        queue.extend([
                            (r + 1, c, 0, steps + 1),  # Move down.
                            (r, c, 1, steps + 1)  # Move clockwise.
                        ])

                    if c + 2 < N and grid[r][c + 2] == 0:
                        queue.append((r, c + 1, 0, steps + 1))  # Move right.

        return -1  # Not able to reach the goal.
