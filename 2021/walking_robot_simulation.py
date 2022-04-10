"""
https://leetcode.com/problems/walking-robot-simulation/
"""


class Solution:
    def robotSim(
            self, commands: list[int], obstacles: list[list[int]]) -> int:
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        memo = {(x, y) for x, y in obstacles}
        x, y, d = 0, 0, 0
        maxDistance = 0
        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            elif cmd == -2:
                d = (d - 1) % 4
            else:
                dx, dy = DIRECTIONS[d]
                for _ in range(cmd):
                    if (x + dx, y + dy) in memo:
                        break

                    x += dx
                    y += dy

                maxDistance = max(maxDistance, (x ** 2 + y ** 2))

        return maxDistance
