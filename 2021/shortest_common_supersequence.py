"""
https://leetcode.com/problems/shortest-common-supersequence/
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def lcs(s1: str, s2: str):
            # Get longest common subsequence between two strings.
            R, C = len(s1), len(s2)
            dp = [['' for _ in range(C + 1)] for _ in range(R + 1)]
            for r in range(R):
                for c in range(C):
                    if s1[r] == s2[c]:
                        dp[r + 1][c + 1] = dp[r][c] + s1[r]
                    else:
                        dp[r + 1][c + 1] = max(
                            dp[r + 1][c], dp[r][c + 1], key=len
                        )

            return dp[-1][-1]

        # Find the lcs between s1 and s2, then append any char that remains
        # to construct the final result
        rslt, r, c = [], 0, 0
        for commonChar in lcs(str1, str2):
            while str1[r] != commonChar:
                rslt += str1[r]
                r += 1

            while str2[c] != commonChar:
                rslt += str2[c]
                c += 1

            rslt += commonChar
            r += 1
            c += 1

        return rslt + str1[r:] + str2[c:]
