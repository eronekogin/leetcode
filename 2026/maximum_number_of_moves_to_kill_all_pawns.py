"""
https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/description/
"""


from collections import deque
from functools import cache
from math import inf


class Solution:
    """
    Solution
    """
    def max_moves(self, kx: int, ky: int, positions: list[list[int]]) -> int:
        """
        max moves
        """
        @cache
        def fn(i: int, mask: int, turn: int):
            if mask == (1 << n) - 1:
                return 0

            rslt = init[turn]

            for k in range(n):
                if not mask & (1 << k):
                    new_mask = mask ^ (1 << k)
                    rslt = ops[turn](
                        rslt,
                        dist[i][k] + fn(k, new_mask, turn ^ 1)
                    )

            return rslt

        n = len(positions)
        init = [0, inf]
        ops = [max, min]
        dist = [[0] * n for _ in range(n + 1)]

        positions.append([kx, ky])
        for i in range(n + 1):
            for j in range(n):
                if i != j:
                    q = deque([positions[i]])
                    seen: set[tuple[int, int]] = set()
                    step = 0

                    while q:
                        for _ in range(len(q)):
                            x, y = q.popleft()
                            if [x, y] == positions[j]:
                                dist[i][j] = step
                                break

                            for xx, yy in [
                                (x - 2, y - 1),
                                (x - 2, y + 1),
                                (x - 1, y - 2),
                                (x - 1, y + 2),
                                (x + 1, y - 2),
                                (x + 1, y + 2),
                                (x + 2, y - 1),
                                (x + 2, y + 1)
                            ]:
                                if (
                                    0 <= xx < 50 and
                                    0 <= yy < 50 and
                                    (xx, yy) not in seen
                                ):
                                    q.append([xx, yy])
                                    seen.add((xx, yy))
                        else:
                            step += 1
                            continue
                        break

        return fn(n, 0, 0)
