"""
https://leetcode.com/problems/edit-distance/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Use dynamic programming solution:
        rslt[i][j] stands for the minimum steps taken in order to transfer
        word1[:i] to word2[:j].
        """
        m, n = len(word1) + 1, len(word2) + 1
        rslt = [[0] * m for _ in range(n)]  # Memo is a m * n array.
        for i in range(1, m):
            rslt[0][i] = i  # When word2 is empty.

        for i in range(1, n):
            rslt[i][0] = i  # When word1 is empty.

        for i2 in range(1, n):
            for i1 in range(1, m):
                if word1[i1 - 1] == word2[i2 - 1]:
                    rslt[i2][i1] = rslt[i2 - 1][i1 - 1]
                else:
                    rslt[i2][i1] = 1 + min(
                        rslt[i2][i1 - 1],  # Insert.
                        rslt[i2 - 1][i1],  # Delete.
                        rslt[i2 - 1][i1 - 1]  # Replace.
                    )

        return rslt[-1][-1]


word1, word2 = 'horse', 'ros'
print(Solution().minDistance(word1, word2))
