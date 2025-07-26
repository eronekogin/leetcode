"""
https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/description/
"""


class Solution:
    """
    Solution
    """

    def difference_of_distinct_values(self, grid: list[list[int]]) -> list[list[int]]:
        """
        difference of distinct values
        """
        def count(r: int, c: int) -> int:
            memo: set[int] = set()
            nr, nc = r - 1, c - 1
            while nr >= 0 and nc >= 0:
                memo.add(grid[nr][nc])
                nr -= 1
                nc -= 1

            l = len(memo)

            memo = set()
            nr, nc = r + 1, c + 1
            while nr < m and nc < n:
                memo.add(grid[nr][nc])
                nr += 1
                nc += 1

            return abs(l - len(memo))

        m, n = len(grid), len(grid[0])
        return [
            [count(r, c) for c in range(n)]
            for r in range(m)
        ]
