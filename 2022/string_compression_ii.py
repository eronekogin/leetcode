"""
https://leetcode.com/problems/string-compression-ii/
"""


from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i: int, prevChar: str, prevCnt: int, remainCharsToDelete: int):
            if remainCharsToDelete < 0:  # Exceed limit.
                return float('inf')

            if i == len(s):  # Reach the end of the string.
                return 0

            # Count the total length after deleting the current char.
            deleteLen = dp(i + 1, prevChar, prevCnt, remainCharsToDelete - 1)

            # Count the total length after keeping the current char.
            if s[i] == prevChar:
                keepLen = (
                    dp(i + 1, prevChar, prevCnt + 1, remainCharsToDelete) +
                    (prevCnt in [1, 9, 99])
                )
            else:
                keepLen = dp(i + 1, s[i], 1, remainCharsToDelete) + 1

            return min(deleteLen, keepLen)

        return dp(0, '', 0, k)
