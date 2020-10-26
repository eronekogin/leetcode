"""
https://leetcode.com/problems/k-inverse-pairs-array/
"""


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """
        Suppose dp[n][k] stands for the number of different list that has n
        numbers with k inverse pairs. Then if we add a new number n + 1 to
        the above lists, we have:
            1. Put n + 1 at the index n, we got 0 new pair.
            2. Put n + 1 at the index n - 1, we got 1 new pair.
            3. Put n + 1 at the index n - 2, we got 2 new pairs.
            ...
            i. Put n + 1 at the index 0, we got n new pairs.

        So we have:
            1. If k >= n:
                dp[n+1][k] = dp[n][k] + dp[n][k-1] + ... + dp[n][k+1-n]
                    + dp[n][k-n]
                dp[n+1][k+1] = dp[n][k+1] + dp[n][k] + ... + dp[n][k+2-n]
                    + dp[n][k+1-n]
                dp[n+1][k+1] = dp[n][k+1] + dp[n+1][k] - dp[n][k-n]
            2. Else:
                dp[n+1][k] = dp[n][k] + ... + dp[n][0]
                dp[n+1][k+1] = dp[n][k+1] + dp[n][k] + ... + dp[n][0]
                dp[n+1][k+1] = dp[n][k+1] + dp[n+1][k]

        Notice that we only use the data from the previous row, we could
        reduce the 2d dp to 1d instead. So we have:
            1. If k >= n:
                next[k + 1] = curr[k + 1] + next[k] - old[k - n]
            2. Else:
                next[k + 1] = curr[k + 1] + next[k]
        """
        if not k:
            return 1

        currList = [0] * (k + 1)
        for i in range(1, n + 1):
            nextList = [1] + [0] * k
            for j in range(1, k + 1):
                if j >= i:
                    nextList[j] = (
                        currList[j] + nextList[j - 1] - currList[j - i])
                else:
                    nextList[j] = currList[j] + nextList[j - 1]

            currList = nextList

        return (currList[-1] - currList[-2]) % (10 ** 9 + 7)


print(Solution().kInversePairs(4, 5))
