"""
https://leetcode.com/problems/shortest-distance-to-a-character/
"""


class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        N = len(s)
        rslt = [0] * N
        prev = float('-inf')
        for i in range(N):  # Scan from left to right.
            if s[i] == c:
                prev = i
            else:
                rslt[i] = i - prev

        prev = float('inf')
        for i in reversed(range(N)):  # Scan from right to left.
            if s[i] == c:
                prev = i
            else:
                rslt[i] = min(rslt[i], prev - i)

        return rslt


print(Solution().shortestToChar(s="loveleetcode", c="e"))
