"""
https://leetcode.com/problems/escape-the-spreading-fire/description/
"""


from collections import deque


class Solution:
    """
    Solution
    """

    def maximum_minutes(self, grid: list[list[int]]) -> int:
        """
        maximum minutes
        """
        def bfs(matrix: list[list[int]], queue: deque[tuple[int, int, int]]):
            while queue:
                r, c, t = queue.popleft()
                matrix[r][c] = t
                nt = t + 1
                for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == 0 and
                        matrix[nr][nc] == -1
                    ):
                        queue.append((nr, nc, nt))

        m, n = len(grid), len(grid[0])

        # Calculate human arrival time regardless of fire.
        human_arrival_time = [[-1] * n for _ in range(m)]
        bfs(human_arrival_time, deque([(0, 0, 0)]))

        # Calculate fire arrival time
        fire_arrival_time = [[-1] * n for _ in range(m)]
        bfs(
            fire_arrival_time,
            deque(
                (r, c, 0)
                for r, row in enumerate(grid)
                for c, v in enumerate(row) if v == 1
            )
        )

        final_human_arrival_time = human_arrival_time[-1][-1]
        final_fire_arrival_time = fire_arrival_time[-1][-1]

        if final_human_arrival_time == -1:  # Cannot reach the safehouse
            return -1

        if final_fire_arrival_time == -1:  # Can always reach the safehouse
            return 10 ** 9

        if final_fire_arrival_time < final_human_arrival_time:  # Fire is first
            return -1

        wait_time = final_fire_arrival_time - final_human_arrival_time
        p1, p2 = human_arrival_time[-1][-2], human_arrival_time[-2][-1]
        f1, f2 = fire_arrival_time[-1][-2], fire_arrival_time[-2][-1]

        if p1 > -1 and p2 > -1 and (f1 - p1 > wait_time or f2 - p2 > wait_time):
            return wait_time

        return wait_time - 1
