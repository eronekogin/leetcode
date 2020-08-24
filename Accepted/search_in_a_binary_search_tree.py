"""
https://leetcode.com/problems/search-in-a-binary-search-tree/
"""


from test_helper import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        if val == root.val:
            return root

        return self.searchBST(root.left, val) or self.searchBST(
            root.right, val)
