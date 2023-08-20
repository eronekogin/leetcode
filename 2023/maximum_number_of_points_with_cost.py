"""
https://leetcode.com/problems/maximum-number-of-points-with-cost/
"""


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        """
        Suppose dp[i][j] stands for the maximum points we can get when arrived at position (r, c), then we have:

            for k in [0, j], dp[i + 1][k] = max(dp[i][j] + points[i + 1][k] - (j - k))
                                          = max(dp[i][j] + points[i + 1][k] - j + k)

            for k in [j, C), dp[i + 1][k] = max(dp[i][j] + points[i + 1][k] - (k - j))
                                          = max(dp[i][j] + points[i + 1][k] + j - k)
        """
        C = len(points[0])
        prevDp: list[int] = points[0]
        for r in range(1, len(points)):
            currDp: list[int] = [0] * C
            temp = 0
            for c in range(C):
                temp = max(temp, prevDp[c] + c)
                currDp[c] = temp - c + points[r][c]
            
            temp = -C
            for c in reversed(range(C)):
                temp = max(temp, prevDp[c] - c)
                currDp[c] = max(currDp[c], temp + c + points[r][c])
            
            prevDp = currDp
        
        return max(prevDp)




            
print(Solution().maxPoints([[1,2,3],[1,5,1],[3,1,1]]))