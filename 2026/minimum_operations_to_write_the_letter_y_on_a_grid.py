"""
https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def minimum_operations_to_write_y(self, grid: list[list[int]]) -> int:
        """
        minimum operations to write y
        """
        n = len(grid)
        n2 = n >> 1

        c1 = Counter()
        for i in range(n2):
            j = n - i - 1
            c1[grid[i][i]] += 1
            c1[grid[j][n2]] += 1
            c1[grid[i][j]] += 1

        c1[grid[n2][n2]] += 1

        c2 = Counter()
        for row in grid:
            c2 += Counter(row)

        c2 -= c1
        return (
            n * n -
            max(
                c1[0] + c2[1],
                c1[0] + c2[2],
                c1[1] + c2[0],
                c1[1] + c2[2],
                c1[2] + c2[1],
                c1[2] + c2[0]
            )
        )


print(Solution().minimum_operations_to_write_y(
    [[0, 1, 0, 1, 0], [2, 1, 0, 1, 2], [2, 2, 2, 0, 1], [2, 2, 2, 2, 2], [2, 1, 2, 2, 2]]))
