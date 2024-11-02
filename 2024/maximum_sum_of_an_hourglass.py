"""
https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/
"""


class Solution:
    """
    Solution
    """

    def max_sum(self, grid: list[list[int]]) -> int:
        """
        max sum
        """
        def get_sum(r: int) -> int:
            curr_sum = curr_max = (
                grid[r][0] + grid[r][1] + grid[r][2] +
                grid[r + 1][1] +
                grid[r + 2][0] + grid[r + 2][1] + grid[r + 2][2]
            )

            for c in range(3, n):
                curr_sum += (
                    grid[r][c] - grid[r][c - 3] +
                    grid[r + 1][c - 1] - grid[r + 1][c - 2] +
                    grid[r + 2][c] - grid[r + 2][c - 3]
                )
                curr_max = max(curr_max, curr_sum)

            return curr_max

        m, n = len(grid), len(grid[0])
        rslt = get_sum(0)
        for r in range(1, m - 2):
            rslt = max(rslt, get_sum(r))

        return rslt
