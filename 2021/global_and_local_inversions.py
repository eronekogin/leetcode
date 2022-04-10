"""
https://leetcode.com/problems/global-and-local-inversions/
"""


class Solution:
    def isIdealPermutation(self, A: list[int]) -> bool:
        """
        1. For an idea permutation, its total global inversions equal to its
            total local inversion.
        2. In other words, each global inversion happens right at each local
            inversion.
        3. So in an idea permutation, each number v could only be placed at
            either index v - 1, v, or v + 1.
        """
        return all(abs(v - i) <= 1 for i, v in enumerate(A))


print(Solution().isIdealPermutation([3, 2, 0, 1]))
