"""
https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def minimum_operations(self, grid: list[list[int]]) -> int:
        """
        dp[i] stands for the operations needed to change the
        current column's digits to i, and since we only care
        about the previous column of the current column, we
        can take the previously calculated dp to calculate the
        current dp for the current column as long as its
        changed digit is not equal to the previous one.
        """
        dp = [0] * 10
        for c in map(Counter, zip(*grid)):
            dp = [
                min(
                    dp[a] + len(grid) - c[b]
                    for a in range(10)
                    if a != b
                )
                for b in range(10)
            ]
        return min(dp)


print(Solution().minimum_operations([[2, 6, 6, 9, 8, 4, 2, 6, 2, 3]]))
