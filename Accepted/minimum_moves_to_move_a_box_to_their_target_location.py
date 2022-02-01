"""
https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/
"""


class Solution:
    def minPushBox(self, grid: list[list[str]]) -> int:
        def is_valid_pos(pos: tuple[int]) -> bool:
            r, c = pos
            return 0 <= r < R and 0 <= c < C and grid[r][c] != '#'

        def can_reach(
            src: tuple[int],
            dst: tuple[int],
            box: tuple[int]
        ) -> bool:
            """
            Check if the person could move from src to dst.
            """
            currCells = [src]
            visited = set()
            for pos in currCells:
                if pos == dst:
                    return True

                r, c = pos
                for newPos in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if (
                        is_valid_pos(newPos) and
                        newPos not in visited and
                        newPos != box
                    ):
                        visited.add(newPos)
                        currCells.append(newPos)

            return False

        R, C = len(grid), len(grid[0])

        # Loop the grid to find the target positions first.
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 'T':
                    target = (r, c)
                elif v == 'B':
                    box = (r, c)
                elif v == 'S':
                    person = (r, c)

        currMoves = [(0, box, person)]
        visited = {box + person}

        for steps, box, person in currMoves:
            if box == target:
                return steps
            br, bc = box

            # Possible positions the box could be after the push.
            newBoxPositions = [
                (br - 1, bc), (br + 1, bc), (br, bc - 1), (br, bc + 1)
            ]

            # Possible positions the person should be before pushing the box.
            newPersonPositions = [
                (br + 1, bc), (br - 1, bc), (br, bc + 1), (br, bc - 1)
            ]

            for newBox, newPerson in zip(newBoxPositions, newPersonPositions):
                if is_valid_pos(newBox) and newBox + box not in visited:
                    if is_valid_pos(newPerson) and can_reach(person, newPerson, box):
                        # After a valid push, the person will be at where
                        # the original box is and the box will be moved to the
                        # newBox.
                        visited.add(newBox + box)
                        currMoves.append((steps + 1, newBox, box))

        return -1
