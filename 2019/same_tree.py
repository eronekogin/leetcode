"""
https://leetcode.com/problems/same-tree/
"""

from test_helper import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:  # p, q are both emtpy.
            return True

        if not p or not q:  # One of p, q is empty.
            return False

        if p.val != q.val:  # Both p, q are not empty.
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(
            p.right, q.right)
