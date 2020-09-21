"""
https://leetcode.com/problems/subtree-of-another-tree/
"""


from test_helper import TreeNode


class Solution:
    def _is_same_tree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True

        if not t1 or not t2:
            return False

        return t1.val == t2.val and \
            self._is_same_tree(t1.left, t2.left) and \
            self._is_same_tree(t1.right, t2.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return s is not None and (
            self._is_same_tree(s, t) or
            self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
