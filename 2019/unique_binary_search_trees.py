"""
https://leetcode.com/problems/unique-binary-search-trees/
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        Let G(n) be the total unique BST constructed from sequence [1, n] and
        F(i, n) be the total unique BST constrctured from sequence [1, n] when
        i is the root node while i in [1, n]. Then we could have:

            F(i, n) = G(i - 1) * G(n - i)
            G(n) = F(1, n) + ... + F(n, n)

        For example, if the current sequence is [1, 7] and the root node is 3.
        Then for the left sub sequence [1, 2] the unique BST it forms is G(2),
        and for the right sub sequence [4, 7] the unique BST it forms is G(4).
        So the total combination F(3, 7) = G(2) * G(4).
        """
        totalBST = [1] * (n + 1)
        for i in range(2, n + 1):
            totalBST[i] = 0
            for j in range(1, i + 1):
                totalBST[i] += totalBST[j - 1] * totalBST[i - j]

        return totalBST[n]
