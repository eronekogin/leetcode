"""
https://leetcode.com/problems/modify-the-matrix/description/
"""


class Solution:
    """
    Solution
    """

    def modified_matrix(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        modified matrix
        """
        memo: dict[int, int] = {}
        m, n = len(matrix), len(matrix[0])
        rslt = [[0] * n for _ in range(m)]

        for r, row in enumerate(matrix):
            for c, v in enumerate(row):
                if v == -1:
                    if c not in memo:
                        memo[c] = max(
                            matrix[i][c]
                            for i in range(m)
                        )

                    rslt[r][c] = memo[c]
                else:
                    rslt[r][c] = v

        return rslt
