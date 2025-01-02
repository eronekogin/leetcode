"""
https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/
"""


from test_helper import TreeNode


class Solution:
    """
    Solution
    """

    def minimum_operations(self, root: TreeNode) -> int:
        """
        minimum operations
        """
        def sort_vals(vals: list[int]) -> int:
            if len(vals) < 2:
                return 0

            operations = 0
            memo = {v: i for i, v in enumerate(vals)}
            for i, v in enumerate(sorted(vals)):
                j = memo[v]
                if i == j:
                    continue

                operations += 1
                vals[i], vals[memo[v]] = vals[memo[v]], vals[i]
                memo[vals[i]], memo[v] = memo[v], i

            return operations

        operations = 0
        curr_nodes: list[TreeNode] = [root]
        while curr_nodes:
            vals: list[int] = []
            next_nodes: list[TreeNode] = []
            for node in curr_nodes:
                if node.left:
                    next_nodes.append(node.left)

                if node.right:
                    next_nodes.append(node.right)

                vals.append(node.val)

            operations += sort_vals(vals)
            curr_nodes = next_nodes

        return operations


r = TreeNode(49).create_tree({
    49: (45, 1),
    45: (20, 46),
    1: (15, 39),
    20: (27, None),
    15: (25, None)
})

print(Solution().minimum_operations(r))
