"""
https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/description/
"""


from functools import cache
from collections import defaultdict


class Solution:
    """
    Solution
    """

    def has_valid_path(self, grid: list[list[str]]) -> bool:
        """
        has valid path
        """
        @cache
        def dfs(balance: int, r: int, c: int) -> bool:
            if r + 1 == m and c + 1 == n and balance == 0:
                return True

            rslt = False
            for nr, nc in [(r + 1, c), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and balance >= 0:
                    if grid[nr][nc] == '(':
                        rslt = rslt or dfs(balance + 1, nr, nc)
                    else:
                        rslt = rslt or dfs(balance - 1, nr, nc)

            return rslt

        m, n = len(grid), len(grid[0])
        return dfs((1 if grid[0][0] == '(' else -1), 0, 0)

    def has_valid_path2(self, grid: list[list[str]]) -> bool:
        """
        has valid path
        """
        dp: defaultdict[tuple[int, int], set[int]] = defaultdict(set)
        dp[0, -1] = dp[-1, 0] = {0}

        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                d = 1 if v == '(' else -1
                dp[r, c] |= {
                    a + d
                    for a in dp[r - 1, c] | dp[r, c - 1]
                    if a + d >= 0
                }

        return 0 in dp[len(grid) - 1, len(grid[0]) - 1]


print(Solution().has_valid_path([["(", ")"], ["(", ")"]]))
