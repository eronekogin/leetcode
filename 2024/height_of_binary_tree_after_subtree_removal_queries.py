"""
https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/description/
"""


from functools import cache

from test_helper import TreeNode


class Solution:
    """
    Solution
    """

    def tree_queries(self, root: TreeNode, queries: list[int]) -> list[int]:
        """
        tree queries
        """
        @cache
        def get_height(node: TreeNode | None):
            if not node:
                return -1

            return 1 + max(get_height(node.left), get_height(node.right))

        def dfs(node: TreeNode | None, depth: int, max_val: int):
            if not node:
                return

            rslt[node.val] = max_val
            depth += 1

            dfs(node.left, depth, max(max_val, depth + get_height(node.right)))
            dfs(node.right, depth, max(max_val, depth + get_height(node.left)))

        rslt: dict[int, int] = {}
        dfs(root, 0, 0)
        return [rslt[q] for q in queries]
