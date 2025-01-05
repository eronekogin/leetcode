"""
https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/description/
"""


from bisect import bisect_left

from test_helper import TreeNode


class Solution:
    """
    Solution
    """

    def closest_nodes(self, root: TreeNode, queries: list[int]) -> list[list[int]]:
        """
        closest nodes
        """
        def dfs(node: TreeNode | None):
            if not node:
                return

            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        vals: list[int] = []
        dfs(root)

        rslt: list[list[int]] = []
        for val in queries:
            i = bisect_left(vals, val)

            if i == len(vals):
                rslt.append([vals[-1], -1])
            elif vals[i] == val:
                rslt.append([val, val])
            elif i == 0:
                rslt.append([-1, vals[0]])
            else:
                rslt.append([vals[i - 1], vals[i]])

        return rslt
