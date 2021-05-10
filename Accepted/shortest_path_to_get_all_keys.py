"""
https://leetcode.com/problems/shortest-path-to-get-all-keys/
"""


from typing import Iterator


class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        """
        Simple BFS. The critical point is to store the visited state with
        keys state.
        """
        def neighbors(r: int, c: int) -> Iterator[tuple[int]]:
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
                    yield (nr, nc)

        R, C = len(grid), len(grid[0])
        OFFSET = ord('a')
        allKeys, currItems, visited = [0] * 6, [], set()
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == '@':
                    currItems.append((r, c, tuple([0] * 6)))
                    visited.add((r, c, tuple([0] * 6)))
                elif v.islower():
                    allKeys[ord(v) - OFFSET] = 1

        allKeys = tuple(allKeys)
        moves = 0
        while currItems:
            nextItems = []
            for r, c, currKeys in currItems:
                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] in '.@' or (grid[nr][nc].isupper() and currKeys[ord(grid[nr][nc].lower()) - OFFSET]):
                        # Either emtpy or start point or a door which could
                        # be locked with the previous collected keys.
                        if (nr, nc, currKeys) not in visited:
                            visited.add((nr, nc, currKeys))
                            nextItems.append((nr, nc, currKeys))
                    elif grid[nr][nc].islower():
                        nextKeys = list(currKeys)
                        nextKeys[ord(grid[nr][nc]) - OFFSET] = 1
                        nextKeys = tuple(nextKeys)
                        if nextKeys == allKeys:
                            return moves + 1  # Found all keys now.

                        if (nr, nc, nextKeys) not in visited:
                            visited.add((nr, nc, nextKeys))
                            nextItems.append((nr, nc, nextKeys))

            currItems = nextItems
            moves += 1

        return -1  # Not reachable.
