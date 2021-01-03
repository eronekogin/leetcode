"""
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
"""


from test_helper import TreeNode


class Solution:
    def getTargetCopy(
            self,
            original: TreeNode,
            cloned: TreeNode,
            target: TreeNode) -> TreeNode:
        def walk(n1: TreeNode, n2: TreeNode) -> TreeNode:
            if not n1:
                return

            if n1 == target:
                return n2

            return walk(n1.left, n2.left) or walk(n1.right, n2.right)

        return walk(original, cloned)
