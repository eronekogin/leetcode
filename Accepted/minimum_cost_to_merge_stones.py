"""
https://leetcode.com/problems/minimum-cost-to-merge-stones/
"""


class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        """
        1. We could only merge k consecutive piles into one pile. So suppose
            we take out 1 pile, the remaining piles should be able to be
            merged into k - 1 piles, so that the whole stones could merge
            into 1 pile. In other words, if (N - 1) % (k - 1) is greater than
            zero, we cannot merge all piles of stone into 1 pile.
        2. Suppose dp[i][j] is the minimum cost to merge stones[i:j+1] into
            a few piles. Then
            dp[i][j] = min(dp[i][m] + dp[m + 1][j] for m in range(i, j))
            2.1 We could only merge k piles into 1 pile means:
                2.1.1 We cannot merge k + 1 piles into 1 pile.
                2.1.2 We can merge k + (k - 1) piles into 1 pile as k + (k - 1)
                    -> 1 + (k - 1) -> k -> 1 pile.
                2.1.3 Then we can merge k + (k - 1) * steps piles into 1 pile.
            2.2 Then the m could actually be in range(i, j, k - 1).
            2.3 In the end, if ((j - i + 1) - 1) % (k - 1) == 0, it means 
                the whole consecutive piles from i to j could merge into 1
                pile, and the cost will be prefix[j + 1] - prefix[i]. 
        """
        def dp(start: int, end: int) -> int:
            if (start, end) not in memo:
                if end - start + 1 < k:
                    rslt = 0
                else:
                    rslt = min(
                        dp(start, mid) + dp(mid + 1, end)
                        for mid in range(start, end, k - 1))

                    if (end - start) % (k - 1) == 0:
                        rslt += prefix[end + 1] - prefix[start]

                memo[(start, end)] = rslt

            return memo[(start, end)]

        memo = {}
        N = len(stones)
        if (N - 1) % (k - 1):  # Not able to merge all piles into one.
            return -1

        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + stones[i]

        return dp(0, N - 1)


print(Solution().mergeStones([3, 2, 4, 1], 2))
