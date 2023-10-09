"""
https://leetcode.com/problems/find-all-groups-of-farmland/
"""


class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        def dfs(r: int, c: int) -> tuple[int, int]:
            if r < 0 or r >= R or c < 0 or c >= C or land[r][c] == 0:
                return (0, 0)
            
            land[r][c] = 0  # Mark visited.
            br1, bc1 = dfs(r + 1, c)  # Go down.
            br2, bc2 = dfs(r, c + 1)  # Go right.
            br = max(br1, br2, r)
            bc = max(bc1, bc2, c)
            return (br, bc)

        R, C = len(land), len(land[0])
        rslt: list[list[int]] = []
        for r, row in enumerate(land):
            for c, v in enumerate(row):
                if v == 1:
                    br, bc = dfs(r, c)
                    rslt.append([r, c, br, bc])
        
        return rslt


        

        