"""
https://leetcode.com/problems/palindrome-partitioning-ii/
"""


class Solution:
    def minCut(self, s: str) -> int:
        """
        dp[i] stands for the minimum cut needed for s[:i].
        Then dp[i + 1] result in two cases, we just take 
        the odd case as an example:

        .......aba...
        |<-X->| ^
        |<-y----->|

        s[i] = b, s[i - 1] = s[i + 1] = a
        So if the minimum cut for s[i - 1] is X, the mininum cut for s[i + 1]
        Y should be no more than X + 1. 

        So dp[i + 1] = min(dp[i + 1], dp[i - 1] + 1) if s[i - 1] == s[i + 1].

        We also need to check the even case as follows:
        .......aa...
        |<-X->|^
        |<-Y---->|

        In the above case: s[i] = a and s[i - 1] == s[i].
        """
        n = len(s)
        if n < 2:  # Empty string or only 1 char.
            return 0

        # Initialize the dp elements with most cuts.
        dp = list(range(-1, n))
        for m in range(1, n):
            for l, r in [(m, m), (m - 1, m)]:
                while l >= 0 and r < n and s[l] == s[r]:
                    dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                    l -= 1
                    r += 1

        return dp[-1]


s = 'aab'
print(Solution().minCut(s))
