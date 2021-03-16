"""
https://leetcode.com/problems/binary-tree-pruning/
"""


from test_helper import TreeNode


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if root.val or root.left or root.right:
                # The root node could not be pruned any longer.
                return root


root = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
print(Solution().pruneTree(root).print_tree())
