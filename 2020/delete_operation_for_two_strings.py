"""
https://leetcode.com/problems/delete-operation-for-two-strings/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        R, C = len(word1) + 1, len(word2) + 1
        deletes = [[None] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if not r or not c:
                    deletes[r][c] = r + c
                elif word1[r - 1] == word2[c - 1]:
                    deletes[r][c] = deletes[r - 1][c - 1]
                else:
                    deletes[r][c] = 1 + min(
                        deletes[r - 1][c], deletes[r][c - 1])

        return deletes[-1][-1]


print(Solution().minDistance('sea', 'eat'))
