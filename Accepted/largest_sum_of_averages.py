"""
https://leetcode.com/problems/largest-sum-of-averages/
"""


class Solution:
    def largestSumOfAverages(self, A: list[int], K: int) -> float:
        """
        1. Suppose dp(i, k) is the best score we could get by dividing A[i:]
            into k groups, then we have:
            dp(i, k + 1) = max(
                avg(A[i:]),
                max(avg(A[i:j]) + dp[j][k] for j in [i + 1, N - 1])
        2. Then we calculate the prefix summary first so that
            avg(A[i:j]) = (sums[j] - sums[i]) / (j - i)
        3. Notice that each dp(i, k + 1) is only related to dp(*, k), so we
            could convert the 2d matrix into 1d list.
        """
        def avg(i: int, j: int) -> float:
            return (sums[j] - sums[i]) / (j - i)

        # Calculate prefix summaries first.
        sums = [0]
        for num in A:
            sums.append(sums[-1] + num)

        # Then calculate each layer of dp.
        N = len(A)

        # Base case, when we don't divide A, then the best score is just the
        # average of each partition.
        dp = [avg(i, N) for i in range(N)]

        for _ in range(2, K + 1):  # Calculate from 2 to K.
            for i in range(N):
                for j in range(i + 1, N):
                    dp[i] = max(dp[i], avg(i, j) + dp[j])

        return dp[0]
