"""
https://leetcode.com/problems/grid-game/
"""


class Solution:
    """
    Solution
    """

    def grid_game(self, grid: list[list[int]]) -> int:
        """
        grid_game
        """
        top_sum = sum(grid[0])
        min_sum = top_sum + sum(grid[1])
        bottom_sum = 0

        for i in range(len(grid[0])):
            top_sum -= grid[0][i]
            min_sum = min(min_sum, max(top_sum, bottom_sum))
            bottom_sum += grid[1][i]

        return min_sum


print(Solution().grid_game([[2, 5, 4], [1, 5, 1]]))
