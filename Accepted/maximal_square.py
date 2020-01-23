"""
https://leetcode.com/problems/maximal-square/
"""


from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Use dynamic programming:

        Take dp[r][c] as the right bottom of the maximum square. Then we have:

            dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1

        Since we only used the values in the previous element and the nearest
        above row, we could just use a one-dimentional list as follows:

            dp[c] = min(dp[c - 1], dp[c], old value of dp[c - 1]) + 1

        while dp first hold the value of the nearest above row, then use it
        to calculate the dp for the current row and still stores the result
        to the dp.
        """
        if not matrix or not matrix[0]:  # Input matrix is empty.
            return 0

        R, C = len(matrix) + 1, len(matrix[0]) + 1
        dp = [0] * C  # Initialize the list to all zeros.
        maxLen = pre = 0
        for r in range(1, R):
            for c in range(1, C):
                temp = dp[c]
                if matrix[r - 1][c - 1] == '1':
                    dp[c] = min(dp[c - 1], dp[c], pre) + 1
                    maxLen = max(maxLen, dp[c])
                else:
                    # Cannot form any square at the current position.
                    dp[c] = 0

                pre = temp

        return maxLen * maxLen
