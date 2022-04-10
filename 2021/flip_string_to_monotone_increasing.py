"""
https://leetcode.com/problems/flip-string-to-monotone-increasing/
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        1. Suppose dp[i] is the minimum flips needed to make the first i chars
            monotone, then we have:
            1.1 if s[i] == '1', the monotone continues, so dp[i] = dp[i - 1]
            1.2 if s[i] == '0':
                1.2.1 Keep s[i], and flip all the previous ones
                    among [0, i - 1].
                1.2.2 Flip s[i].
                1.2.3 So dp[i] = min(previousOnes, dp[i - 1] + 1)
        """
        ones = flips = 0
        for c in s:
            if c == '1':
                ones += 1
            else:
                flips += 1

            flips = min(flips, ones)

        return flips
