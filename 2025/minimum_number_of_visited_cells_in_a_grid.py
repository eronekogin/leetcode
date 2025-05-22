"""
https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def minimum_visited_cells(self, grid: list[list[int]]) -> int:
        """
        minimum visited cells
        """
        m, n = len(grid), len(grid[0])
        row_heaps = [[] for _ in range(m)]
        col_heaps = [[] for _ in range(n)]
        max_score = m * n + 1

        heappush(row_heaps[0], (1, 0))

        for r in range(m):
            for c in range(n):
                min_score = max_score

                while row_heaps[r] and row_heaps[r][0][1] < c:
                    heappop(row_heaps[r])

                if row_heaps[r]:
                    min_score = min(min_score, row_heaps[r][0][0])

                while col_heaps[c] and col_heaps[c][0][1] < r:
                    heappop(col_heaps[c])

                if col_heaps[c]:
                    min_score = min(min_score, col_heaps[c][0][0])

                if r + 1 == m and c + 1 == n and min_score != max_score:
                    return min_score

                if min_score != max_score:
                    heappush(row_heaps[r], (min_score + 1, c + grid[r][c]))
                    heappush(col_heaps[c], (min_score + 1, r + grid[r][c]))

        return -1
