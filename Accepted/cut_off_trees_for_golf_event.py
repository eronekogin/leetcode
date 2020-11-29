"""
https://leetcode.com/problems/cut-off-trees-for-golf-event/
"""


from typing import List


from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def calc_step(sr: int, sc: int) -> int:
            visited = {(sr, sc)}
            queue = deque([(0, sr, sc)])
            while queue:
                d, r, c = queue.popleft()
                if r == tr and c == tc:  # Reach the target cell.
                    return d

                for dr, dc in DIRECTIONS:  # Continue walking.
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited \
                            and forest[nr][nc]:
                        visited.add((nr, nc))
                        queue.append((d + 1, nr, nc))

            return -1  # Not able to reach to the target position.

        sr = sc = 0
        totalSteps = 0
        R, C = len(forest), len(forest[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for _, tr, tc in sorted(
            (h, r, c)
            for r, row in enumerate(forest)
            for c, h in enumerate(row)
            if h > 1
        ):
            currSteps = calc_step(sr, sc)
            if currSteps < 0:  # Cannot reach to one of the trees.
                return -1

            totalSteps += currSteps
            sr, sc = tr, tc

        return totalSteps
