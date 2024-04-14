"""
https://leetcode.com/problems/count-collisions-on-a-road/description/
"""


class Solution:
    """
    Solution
    """

    def count_collisions(self, directions: str) -> int:
        """
        count collisions
        """
        n = len(directions)
        l, r = 0, n - 1
        while l < n and directions[l] == 'L':
            l += 1

        while r >= 0 and directions[r] == 'R':
            r -= 1

        return sum(
            directions[i] != 'S'
            for i in range(l, r + 1)
        )
