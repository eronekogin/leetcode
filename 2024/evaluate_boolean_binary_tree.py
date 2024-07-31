"""
https://leetcode.com/problems/evaluate-boolean-binary-tree/description/
"""


from test_helper import TreeNode


class Solution:
    """
    Solution
    """

    def evaluate_tree(self, root: TreeNode) -> bool:
        """
        evaluate tree
        """
        def dfs(root: TreeNode):
            if not root.left:  # leaf node.
                return root.val

            left, right = dfs(root.left), dfs(root.right)

            if root.val == 2:
                return left or right

            if root.val == 3:
                return left and right

        return bool(dfs(root))
