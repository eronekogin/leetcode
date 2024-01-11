"""
https://leetcode.com/problems/rings-and-rods/
"""


class Solution:
    """
    Solution
    """

    def count_points(self, rings: str) -> int:
        """
        count_points
        """
        memo = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i + 1]
            memo[int(rod)].add(color)

        return sum(len(item) == 3 for item in memo)
