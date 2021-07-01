"""
https://leetcode.com/problems/shortest-bridge/
"""


from collections import deque
from typing import Iterator


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        def neighbors(r: int, c: int) -> Iterator[tuple[int]]:
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield (nr, nc)

        def find_first_non_zero() -> tuple[int]:
            for r, row in enumerate(grid):
                for c, v in enumerate(row):
                    if v:
                        return (r, c)

        R, C = len(grid), len(grid[0])

        # Collect boundaries for the first island.
        r, c = find_first_non_zero()
        queue = deque([(r, c)])
        queue2 = deque([(0, r, c)])
        island1 = {(r, c)}
        while queue:
            r, c = queue.popleft()
            for nr, nc in neighbors(r, c):
                if (nr, nc) not in island1 and grid[nr][nc]:
                    island1.add((nr, nc))
                    queue2.append((0, nr, nc))
                    queue.append((nr, nc))

        while queue2:
            currFlipped, r, c = queue2.popleft()
            for nr, nc in neighbors(r, c):
                if (nr, nc) not in island1:
                    if not grid[nr][nc]:  # Try to flip the current cell.
                        island1.add((nr, nc))
                        queue2.append((currFlipped + 1, nr, nc))
                    elif (nr, nc) not in island1:  # Found a new island.
                        return currFlipped

        return -1  # Not found.


print(Solution().shortestBridge([[0, 1], [1, 0]]))
