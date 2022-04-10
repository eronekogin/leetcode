"""
https://leetcode.com/problems/ones-and-zeroes/
"""


from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        Suppose dp[i][z][o] holds the maximum number of strings we could form
        by using z zeros and o ones for the first i strings in strs. Then we
        have:

        dp[i][z][o] = max(
            dp[i - 1][z - zeros on strs[i]][o - ones on strs[i]] + 1,
            dp[i - 1][z][o]
        )

        Either take the current string i or skip it, just take the maximum as
        the current result.

        Since the dp[i][*][*] only relies on dp[i - 1][*][*] to get its result,
        we could reduce the 3d matrix to a 2d one instead.
        """
        Z, O = m + 1, n + 1
        dp = [[0] * O for _ in range(Z)]
        for s in strs:
            currZeros = s.count('0')
            currOnes = len(s) - currZeros
            for z in reversed(range(currZeros, Z)):
                for o in reversed(range(currOnes, O)):
                    dp[z][o] = max(
                        dp[z - currZeros][o - currOnes] + 1, dp[z][o])

        return dp[-1][-1]


print(Solution().findMaxForm(["0001", "0101", "1000", "1000"], 9, 3))
