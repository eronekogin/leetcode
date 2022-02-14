"""
https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
"""


class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        R, C = len(mat), len(mat[0])
        prefixSums = [[0] * (C + 1) for _ in range(R + 1)]
        maxSideLen = 0
        for r in range(R):
            for c in range(C):
                prefixSums[r + 1][c + 1] = (
                    prefixSums[r][c + 1] +
                    prefixSums[r + 1][c] -
                    prefixSums[r][c] +
                    mat[r][c]
                )
                if min(r, c) >= maxSideLen:
                    sideLen = (
                        prefixSums[r + 1][c + 1] -
                        prefixSums[r - maxSideLen][c + 1] -
                        prefixSums[r + 1][c - maxSideLen] +
                        prefixSums[r - maxSideLen][c - maxSideLen]
                    )
                    if sideLen <= threshold:
                        maxSideLen += 1

        return maxSideLen


print(Solution().maxSideLength([[1, 1, 3, 2, 4, 3, 2], [
      1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4))
