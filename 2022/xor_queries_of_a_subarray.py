"""
https://leetcode.com/problems/xor-queries-of-a-subarray/
"""


class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        """
        x ^ y ^ x = y, so we could use prefix xors to determine the total
        xor for a given range.
        """
        prefixXORs: list[int] = [0]
        for num in arr:
            prefixXORs.append(prefixXORs[-1] ^ num)

        return [prefixXORs[l] ^ prefixXORs[r + 1] for l, r in queries]


print(Solution().xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]))
