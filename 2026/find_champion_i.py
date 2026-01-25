"""
https://leetcode.com/problems/find-champion-i/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def find_champion(self, grid: list[list[int]]) -> int:
        """
        Docstring for find_champion

        :param self: Description
        :param grid: Description
        :type grid: list[list[int]]
        :return: Description
        :rtype: int
        """
        n = len(grid)
        for i, row in enumerate(grid):
            if sum(row) + 1 == n:
                return i

        return -1


print(Solution().find_champion([[0, 1], [0, 0]]))
