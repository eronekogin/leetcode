"""
https://leetcode.com/problems/count-submatrices-with-all-ones/
"""


class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        R, C = len(mat), len(mat[0])

        # Calculate prefix sum.
        for r in range(1, R):
            for c in range(C):
                if mat[r][c] == 1:
                    mat[r][c] += mat[r - 1][c]

        # Calculate submatrices.
        rslt = 0
        for r in range(R):
            stack: list[int] = []
            cnt = 0
            for c in range(C):
                while stack and mat[r][stack[-1]] > mat[r][c]:
                    start = stack.pop()
                    end = stack[-1] if stack else -1

                    # Remove the exceeded rows from start to end in order
                    # to get candiate submatrices.
                    cnt -= (mat[r][start] - mat[r][c]) * (start - end)

                # Collect matrices.
                cnt += mat[r][c]
                rslt += cnt
                stack.append(c)

        return rslt
