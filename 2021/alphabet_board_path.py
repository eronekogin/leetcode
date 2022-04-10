"""
https://leetcode.com/problems/alphabet-board-path/
"""

from string import ascii_lowercase


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        """
        General bfs solution.
        """
        def isValidCell(r: int, c: int) -> bool:
            return (0 <= r < 5 and 0 <= c < 5) or (r == 5 and c == 0)

        def bfs(
            srcRow: int,
            srcCol: int,
            target: str
        ) -> tuple[list[str], int, int]:
            currNodes = [([], srcRow, srcCol)]  # (path, r, c)
            visited = set()
            for path, r, c in currNodes:
                if BOARD[r][c] == target:  # Found.
                    return (path + ['!'], r, c)

                # If not found, search from four directions if not visited yet.
                for direction, nr, nc in [
                    ('U', r - 1, c),
                    ('D', r + 1, c),
                    ('L', r, c - 1),
                    ('R', r, c + 1)
                ]:
                    if isValidCell(nr, nc) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        currNodes.append((path + [direction], nr, nc))

        BOARD = [
            ['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'i', 'j'],
            ['k', 'l', 'm', 'n', 'o'],
            ['p', 'q', 'r', 's', 't'],
            ['u', 'v', 'w', 'x', 'y'],
            ['z']
        ]
        rslt = []
        srcRow = srcCol = 0
        for c in target:
            path, srcRow, srcCol = bfs(srcRow, srcCol, c)
            rslt.extend(path)

        return ''.join(rslt)

    def alphabetBoardPath2(self, target: str) -> str:
        """
        The minimum distance is the sum of offset from one cell to another,
        and since moving right or down could result an emtpy cell, we could
        move left or up first to avoid that.
        """
        BOARD = {c: [i // 5, i % 5] for i, c in enumerate(ascii_lowercase)}
        srcRow, srcCol = 0, 0
        rslt = []
        for c in target:
            dstRow, dstCol = BOARD[c]
            if dstCol < srcCol:
                rslt.append('L' * (srcCol - dstCol))

            if dstRow < srcRow:
                rslt.append('U' * (srcRow - dstRow))

            if dstCol > srcCol:
                rslt.append('R' * (dstCol - srcCol))

            if dstRow > srcRow:
                rslt.append('D' * (dstRow - srcRow))

            rslt.append('!')
            srcRow, srcCol = dstRow, dstCol

        return ''.join(rslt)
