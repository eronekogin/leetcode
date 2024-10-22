"""
https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/
"""


from test_helper import TreeNode


class Solution:
    """
    Solution
    """

    def reverse_odd_levels(self, root: TreeNode) -> TreeNode:
        """
        reverse odd levels
        """
        def reverse(nodes: list[TreeNode]):
            l, r = 0, len(nodes) - 1
            while l < r:
                nodes[l].val, nodes[r].val = nodes[r].val, nodes[l].val
                l += 1
                r -= 1

        curr_nodes: list[TreeNode] = [root]
        level = 0
        while curr_nodes:
            next_nodes: list[TreeNode] = []

            if level & 1:
                reverse(curr_nodes)

            for node in curr_nodes:
                if node.left:
                    next_nodes.append(node.left)

                if node.right:
                    next_nodes.append(node.right)

            level += 1
            curr_nodes = next_nodes

        return root
