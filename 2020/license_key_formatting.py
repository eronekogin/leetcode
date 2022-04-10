"""
https://leetcode.com/problems/license-key-formatting/
"""


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = S.replace('-', '').upper()
        first = len(s) % K
        rslt = [s[:first]] if first else []
        for i in range(first, len(s), K):
            rslt.append(s[i: i + K])

        return '-'.join(rslt)


print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))
