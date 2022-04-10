"""
https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
"""


from test_helper import TreeNode


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root.left and not root.right:  # A leaf node.
            if root.val < limit:
                return None

            return root

        if root.left:  # Calculate new left.
            root.left = self.sufficientSubset(root.left, limit - root.val)

        if root.right:  # Calculate new right.
            root.right = self.sufficientSubset(root.right, limit - root.val)

        if root.left or root.right:  # If having any new left or new right.
            return root

        return None  # If the current node is removed.
