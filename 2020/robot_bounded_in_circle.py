"""
https://leetcode.com/problems/robot-bounded-in-circle/
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        After one round of all the instructions:
            1. If the robot goes back to the original point, it will still be
                at the original point after the next round's instructions.
            2. If the robot goes to a new point:
                2.1 If the robot faces to the same direction as the original
                    one, it will go toward the same direction and move further
                    after the next round's instructions.
                2.2 If the robot faces to a different direction, then it means
                    it will eventually go back to the original point.
        """
        x, y, dx, dy = 0, 0, 0, 1
        for c in instructions:
            if c == 'G':
                x += dx
                y += dy
            elif c == 'L':
                dx, dy = -dy, dx
            elif c == 'R':
                dx, dy = dy, -dx

        return (x, y) == (0, 0) or (dx, dy) != (0, 1)


print(Solution().isRobotBounded('GL'))
