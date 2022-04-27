"""
https://leetcode.com/problems/balance-a-binary-search-tree/
"""


from test_helper import TreeNode


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def get_node_values(root: TreeNode) -> None:
            if not root:
                return

            get_node_values(root.left)
            nodes.append(root)
            get_node_values(root.right)

        def build_balanced_bst(l: int, r: int) -> TreeNode:
            if l > r:
                return None

            m = l + ((r - l) >> 1)
            root = nodes[m]
            root.left = build_balanced_bst(l, m - 1)
            root.right = build_balanced_bst(m + 1, r)
            return root

        nodes: list[TreeNode] = []
        get_node_values(root)
        return build_balanced_bst(0, len(nodes) - 1)
