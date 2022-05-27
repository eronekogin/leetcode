"""
https://leetcode.com/problems/restore-the-array/
"""


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        """
        dp[i] stands for the number of possible arrays that ends at
        position i.
        """
        MOD = 10 ** 9 + 7
        N = len(s)
        MAXLEN = len(str(k))
        dp = [1] * (N + 1)

        for end in range(N):
            rslt, currStr = 0, ''
            for start in range(end, max(-1, end - MAXLEN), -1):
                currStr = s[start] + currStr
                if currStr[0] != '0' and int(currStr) <= k:
                    rslt += dp[start]

            if rslt == 0:  # No possible array.
                return 0

            dp[end + 1] = rslt % MOD

        return dp[-1]
