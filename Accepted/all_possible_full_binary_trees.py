"""
https://leetcode.com/problems/all-possible-full-binary-trees/
"""


from test_helper import TreeNode


class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        def check(n: int) -> list[TreeNode]:
            if n not in memo:
                rslt = []
                for i in range(n):
                    j = n - 1 - i
                    for left in check(i):
                        for right in check(j):
                            root = TreeNode(0)
                            root.left = left
                            root.right = right
                            rslt.append(root)

                memo[n] = rslt

            return memo[n]

        if not n & 1:  # Must have odd nodes to form full binary tree.
            return []

        memo = {
            0: [],
            1: [TreeNode(0)]
        }

        return check(n)
