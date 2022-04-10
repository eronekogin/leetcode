"""
https://leetcode.com/problems/champagne-tower/
"""


class Solution:
    def champagneTower(
            self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Calculate the total champagne flow through each glass. For example,
        if poured 10 cups, the only glass on the first row has 9 cups flowed
        through; then the two glasses on the second row has 3.5 cups flowed
        through each. 
        """
        dp = [[0.0] * (r + 1) for r in range(query_row + 1)]
        dp[0][0] = poured
        for r in range(query_row):
            for c in range(r + 1):
                exceeds = (dp[r][c] - 1.0) / 2.0
                if exceeds > 0:
                    dp[r + 1][c] += exceeds
                    dp[r + 1][c + 1] += exceeds

        return min(1.0, dp[query_row][query_glass])

    def champagneTower2(
            self, poured: int, query_row: int, query_glass: int) -> float:
        """
        The above could be reduced to a 1d dp instead since we only use the
        information from the previous row.
        """
        currRow = [poured]
        for r in range(1, query_row + 1):
            nextRow = [0.0] * (r + 1)
            for c in range(r):
                exceeds = (currRow[c] - 1.0) / 2.0
                if exceeds > 0:
                    nextRow[c] += exceeds
                    nextRow[c + 1] += exceeds

            currRow = nextRow

        return min(1.0, currRow[query_glass])


print(Solution().champagneTower2(25, 6, 1))
