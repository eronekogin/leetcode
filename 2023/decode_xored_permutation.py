"""
https://leetcode.com/problems/decode-xored-permutation/
"""


class Solution:
    def decode(self, encoded: list[int]) -> list[int]:
        N = len(encoded) + 1

        # Get xors from 1 to N first.
        # Then get xors from a2 to an by the following rules:
        # a2 ^ a3 = encoded[1], a4 ^ a5 = encoded[3], ...
        # And N is always odd.
        # Then the first element a1 = 1 ^ 2 ^ ... ^ n ^ a2 ^ a3 ^ ... ^ an
        a1 = 0
        for i in range(1, N + 1):
            a1 ^= i
            if i < N and i & 1:
                a1 ^= encoded[i]

        rslt = [a1]
        for num in encoded:
            rslt.append(rslt[-1] ^ num)

        return rslt


print(Solution().decode([3, 1]))
