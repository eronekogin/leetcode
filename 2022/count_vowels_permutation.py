"""
https://leetcode.com/problems/count-vowels-permutation/
"""


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        This question could be turned to check the width of the tree with
        height n, then we could start counting from the bottom of the string
        all the way to the top, so that we don't need to translate the
        mapping from top to down.
        """
        if not n:
            return 0

        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = e, a + i, a + e + o + u, i + u, a

        return (a + e + i + o + u) % (10 ** 9 + 7)
