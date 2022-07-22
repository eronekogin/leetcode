"""
https://leetcode.com/problems/path-crossing/
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited: set[tuple[int]] = set()
        x = y = 0
        for c in path:
            visited.add((x, y))
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'W':
                x -= 1
            else:
                x += 1

            if (x, y) in visited:
                return True

        return False
