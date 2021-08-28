"""
https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
"""


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        """
        Brutal force: since the binary format of i must occur in the binary
        format of (i << 1), so we don't need to check any number less than
        (n << 1) - 1.
        """
        return all(bin(i)[2:] in s for i in range(n, max((n >> 1) - 1, 1), -1))
