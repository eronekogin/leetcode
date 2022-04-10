"""
https://leetcode.com/problems/perfect-squares/
"""


class Solution:
    def numSquares(self, n: int) -> int:
        """
        Use dynamic programming:

        dp[0] = 0 
        dp[1] = dp[0]+1 = 1
        dp[2] = dp[1]+1 = 2
        dp[3] = dp[2]+1 = 3
        dp[4] = Min{ dp[4-1*1]+1, dp[4-2*2]+1 } 
            = Min{ dp[3]+1, dp[0]+1 } 
            = 1				
        dp[5] = Min{ dp[5-1*1]+1, dp[5-2*2]+1 } 
            = Min{ dp[4]+1, dp[1]+1 } 
            = 2
                                .
                                .
                                .
        dp[13] = Min{ dp[13-1*1]+1, dp[13-2*2]+1, dp[13-3*3]+1 } 
            = Min{ dp[12]+1, dp[9]+1, dp[4]+1 } 
            = 2
                                .
                                .
                                .
        dp[n] = Min{ dp[n - i*i] + 1 },  n - i*i >=0 && i >= 1
        """
        maxNum = n + 1
        dp = [maxNum] * maxNum
        dp[0] = 0
        for i in range(1, maxNum):
            dp[i] = min(
                [dp[i - j * j] for j in range(1, int(i ** 0.5) + 1)]) + 1

        return dp[-1]

    def numSquares2(self, n: int) -> int:
        """
        Use BFS. The root node is n, find the shortest path to leaf node 0.
        """
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        d, q, nq = 1, {n}, set()
        while q:
            for node in q:
                for square in squares:
                    if node == square:
                        return d
                    elif node < square:
                        break
                    else:
                        nq.add(node - square)

            q, nq, d = nq, set(), d + 1


print(Solution().numSquares2(12))
