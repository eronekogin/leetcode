"""
https://leetcode.com/problems/univalued-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        if root.left and root.val != root.left.val:
            return False

        if root.right and root.val != root.right.val:
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
