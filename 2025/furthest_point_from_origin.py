"""
https://leetcode.com/problems/furthest-point-from-origin/description/
"""


class Solution:
    """
    Solution
    """

    def furthest_distance_from_origin(self, moves: str) -> int:
        """
        furthest distance from origin
        """
        extra = 0
        d = 0
        for c in moves:
            if c == 'L':
                d -= 1
            elif c == 'R':
                d += 1
            else:
                extra += 1

        if d >= 0:
            return d + extra

        return extra - d
