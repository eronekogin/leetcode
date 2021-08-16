"""
https://leetcode.com/problems/grid-illumination/
"""


from collections import Counter


class Solution:
    def gridIllumination(
        self,
        n: int,
        lamps: list[list[int]],
        queries: list[list[int]]
    ) -> list[int]:
        rows = Counter()
        cols = Counter()
        leftDiagonals = Counter()  # x + y = x0 + y0
        rightDiagonals = Counter()  # x + y = y0 - x0
        lights = {(r, c) for r, c in lamps}  # Remove dup lamps

        # Count lighted cells.
        for r, c in lights:
            rows[r] += 1
            cols[c] += 1
            leftDiagonals[r + c] += 1
            rightDiagonals[c - r] += 1

        # Calculate answer.
        rslt = []
        for r, c in queries:
            if rows[r] > 0 or cols[c] > 0 or leftDiagonals[r + c] > 0 or rightDiagonals[c - r] > 0:
                rslt.append(1)
            else:
                rslt.append(0)

            # Turn off lamp if any.
            for nr, nc in [
                (nr, nc)
                for nr in range(r - 1, r + 2)
                for nc in range(c - 1, c + 2)
                if (nr, nc) in lights
            ]:
                lights.remove((nr, nc))
                rows[nr] -= 1
                cols[nc] -= 1
                leftDiagonals[nr + nc] -= 1
                rightDiagonals[nc - nr] -= 1

        return rslt


print(Solution().gridIllumination(
    5,
    [[0, 0], [0, 4]],
    [[0, 4], [0, 1], [1, 4]]
))
