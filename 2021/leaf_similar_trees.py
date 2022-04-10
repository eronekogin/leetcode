"""
https://leetcode.com/problems/leaf-similar-trees/
"""


from test_helper import TreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leaves(root: TreeNode) -> list[int]:
            if not root:
                return []

            if not root.left and not root.right:
                return [root.val]

            return get_leaves(root.left) + get_leaves(root.right)

        return get_leaves(root1) == get_leaves(root2)
