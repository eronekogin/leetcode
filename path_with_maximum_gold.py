"""
https://leetcode.com/problems/path-with-maximum-gold/
"""


class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        def dfs(r: int, c: int, currSum: int) -> int:
            if r < 0 or r >= R or c < 0 or c >= C or (r, c) in visited or grid[r][c] == 0:
                return currSum

            visited.add((r, c))
            nextSum = currSum + grid[r][c]
            maxSum = 0

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                maxSum = max(maxSum, dfs(nr, nc, nextSum))

            visited.remove((r, c))
            return maxSum

        R, C = len(grid), len(grid[0])
        visited = set()
        return max(dfs(r, c, 0) for r in range(R) for c in range(C))
