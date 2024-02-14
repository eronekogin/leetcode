"""
https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/description/
"""


from collections import deque


class Solution:
    """
    Solution
    """

    def highest_ranked_k_items(
        self,
        grid: list[list[int]],
        pricing: list[int],
        start: list[int],
        k: int
    ) -> list[list[int]]:
        """
        highest_ranked_k_items
        """
        lp, rp = pricing
        r0, c0 = start
        m, n = len(grid), len(grid[0])
        visited = {(r0, c0)}
        queue: deque[tuple[int, int, int, int]] = deque(
            [(0, grid[r0][c0], r0, c0)]
        )
        rslt: list[list[int]] = []

        while queue:
            d, p, r, c = queue.popleft()
            if lp <= p <= rp:
                rslt.append([d, p, r, c])

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] > 0:
                    queue.append((d + 1, grid[nr][nc], nr, nc))
                    visited.add((nr, nc))

        rslt.sort()
        return [[r, c] for _, _, r, c in rslt[:k]]
