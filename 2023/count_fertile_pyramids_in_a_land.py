"""
https://leetcode.com/problems/count-fertile-pyramids-in-a-land/
"""


class Solution:
    """
    Solution
    """

    def count_pyramids(self, grid: list[list[int]]) -> int:
        """
        count_pyramids
        """
        def count(grid: list[list[int]]):
            """
            count number of pyramid in the target grid from top to down
            """
            pyramids = 0
            for r in range(1, len(grid)):
                for c in range(1, len(grid[0]) - 1):
                    if grid[r][c] and grid[r - 1][c]:
                        new_pyramids = min(
                            grid[r - 1][c - 1],
                            grid[r - 1][c + 1]
                        )
                        pyramids += new_pyramids
                        grid[r][c] = new_pyramids + 1

            return pyramids

        reverse_grid: list[list[int]] = []
        for r in range(len(grid) - 1, -1, -1):
            reverse_grid.append(grid[r][:])

        return count(grid) + count(reverse_grid)
