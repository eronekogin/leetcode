"""
https://leetcode.com/problems/count-sub-islands/
"""


class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        def dfs(r: int, c: int):
            if r < 0 or r >= R or c < 0 or c >= C or not grid2[r][c]:
                return
            
            grid2[r][c] = 0
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        R, C = len(grid1), len(grid1[0])

        # Remove all non-common grid in grid2.
        for r in range(R):
            for c in range(C):
                if grid2[r][c] and not grid1[r][c]:
                    dfs(r, c)
        
        # Count islands.
        islands = 0
        for r in range(R):
            for c in range(C):
                if grid2[r][c]:
                    dfs(r, c)
                    islands += 1
        
        return islands


print(Solution().countSubIslands(
    [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
    [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
))