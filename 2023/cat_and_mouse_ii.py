"""
https://leetcode.com/problems/cat-and-mouse-ii/
"""


from functools import cache


class Solution:
    def canMouseWin(
        self,
        grid: list[str],
        catJump: int,
        mouseJump: int
    ) -> bool:
        @cache
        def dp(
            currTurn: int,
            mousePos: tuple[int],
            catPos: tuple[int]
        ):
            if currTurn == availableSteps * 2:
                # Cat and mouse have both searched the whole grid at this turn.
                return False

            if currTurn & 1 == 0:  # Mouse move.
                r, c = mousePos
                for dr, dc in directions:
                    for jump in range(mouseJump + 1):
                        nr, nc = r + dr * jump, c + dc * jump
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
                            if (
                                dp(currTurn + 1, (nr, nc), catPos) or
                                grid[nr][nc] == 'F'
                            ):
                                return True
                        else:
                            break

                return False
            else:  # Cat move.
                r, c = catPos
                for dr, dc in directions:
                    for jump in range(catJump + 1):
                        nr, nc = r + dr * jump, c + dc * jump
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
                            if (
                                not dp(currTurn + 1, mousePos, (nr, nc)) or
                                (nr, nc) == mousePos or
                                grid[nr][nc] == 'F'
                            ):
                                return False
                        else:
                            break

                return True

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        R, C = len(grid), len(grid[0])
        mousePos = catPos = None
        availableSteps = 0

        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v != '#':
                    availableSteps += 1

                if v == 'M':
                    mousePos = (r, c)
                elif v == 'C':
                    catPos = (r, c)

        return dp(0, mousePos, catPos)
