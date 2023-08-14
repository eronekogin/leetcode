"""
https://leetcode.com/problems/painting-a-grid-with-three-different-colors/
"""


from functools import cache


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        def get_color(mask: int, position: int):
            """
            Get the color of the mask at position. Using 2 bits as a color.
            """
            return (mask >> (position << 1)) & 3
        
        def set_color(mask: int, position: int, color: int):
            """
            Set the color of the mask at position. Using 2 bits as a color.
            """
            return mask | (color << (position << 1))

        def dfs(currRow: int, currColMask: int, prevColMask: int, out: list[int]):
            if currRow == m:
                out.append(currColMask)
                return
            
            for color in [1, 2, 3]:
                if (
                    get_color(prevColMask, currRow) != color and
                    (currRow == 0 or get_color(currColMask, currRow - 1) != color)
                ):
                    dfs(currRow + 1, set_color(currColMask, currRow, color), prevColMask, out)
        
        @cache
        def neighbors(prevColMask: int):
            out: list[int] = []
            dfs(0, 0, prevColMask, out)
            return out
        
        @cache
        def dp(currCol: int, prevColMask: int):
            if currCol == n:  # Found a valid way.
                return 1

            rslt = 0
            for neighbor in neighbors(prevColMask):
                rslt = (rslt + dp(currCol + 1, neighbor)) % (10 ** 9 + 7)
            
            return rslt

        return dp(0, 0)
