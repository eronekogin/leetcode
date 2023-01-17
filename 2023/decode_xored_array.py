"""
https://leetcode.com/problems/decode-xored-array/
"""


class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        N = len(encoded)
        rslt = [0] * (N + 1)
        rslt[0] = first
        for i in range(N):
            rslt[i + 1] = rslt[i] ^ encoded[i]

        return rslt
