"""
https://leetcode.com/problems/letter-tile-possibilities/
"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs() -> int:
            total = 0
            for i in range(N):
                if cnt[i]:
                    total += 1  # Stands for a single char.
                    cnt[i] -= 1  # Remove the current char.
                    total += dfs()
                    cnt[i] += 1  # Add back the current char.

            return total

        N = 26  # 26 english uppercase letters
        cnt = [0] * N
        for c in tiles:
            cnt[ord(c) - ord('A')] += 1

        return dfs()
