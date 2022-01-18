"""
https://leetcode.com/problems/circular-permutation-in-binary-representation/
"""


class Solution:
    def circularPermutation(self, n: int, start: int) -> list[int]:
        """
        1. Generate gray code by n ^ (n >> 1).
        2. Then start xor x for x in gray code will generate the target result.
        """
        return [start ^ i ^ (i >> 1) for i in range(1 << n)]
