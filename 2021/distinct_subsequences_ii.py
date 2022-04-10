"""
https://leetcode.com/problems/distinct-subsequences-ii/
"""


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        """
        Suppose dp[i] stands for the number of subsequences (including the
        empty sequence "") formed from s[0] to s[i], then:
            1. dp[i] = dp[i - 1] * 2, when s[i] does not occur previously. For
                example, s = abc, dp[1] = 4 ('', a, b, ab), then dp[2] = 8
                ('', a, b, ab | c, ac, bc, abc)
            2. dp[i] = dp[i - 1] * 2 - dp[last[s[i]]], when s[i] occur
                before. For example, s = aba, dp[1] = 4 ('', a, b, ab), 
                then dp[2] = 7 ('', a, b, ab | aa, ba, aba) = 
                2 * dp[1] - dp[0], here last['a'] = 0
        """
        dp = [1]
        last = {}
        for i, c in enumerate(s):
            dp.append(dp[-1] << 1)
            if c in last:
                dp[-1] -= dp[last[c]]

            last[c] = i

        # Remove the first empty subsequence from the final result.
        return (dp[-1] - 1) % (10 ** 9 + 7)
