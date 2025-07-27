"""
https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def difference_of_distinct_values(self, grid: list[list[int]]) -> list[list[int]]:
        """
        difference of distinct values
        """
        def count(r: int, c: int):
            i, j = r, c
            cnt = Counter()
            while i < m and j < n:
                cnt[grid[i][j]] += 1
                i += 1
                j += 1

            i, j = r, c
            left: set[int] = set()
            while i < m and j < n:
                cnt[grid[i][j]] -= 1
                if cnt[grid[i][j]] == 0:
                    del cnt[grid[i][j]]

                rslt[i][j] = abs(len(cnt) - len(left))
                left.add(grid[i][j])
                i += 1
                j += 1

        m, n = len(grid), len(grid[0])
        rslt = [[0] * n for _ in range(m)]
        for c in range(n):
            count(0, c)

        for r in range(1, m):
            count(r, 0)

        return rslt
