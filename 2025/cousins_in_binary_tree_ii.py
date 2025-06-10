"""
https://leetcode.com/problems/cousins-in-binary-tree-ii/description/
"""


from test_helper import TreeNode


class Solution:
    """
    Solution
    """

    def replace_value_in_tree(self, root: TreeNode) -> TreeNode:
        """
        replace value in tree
        """
        parent_nodes: list[TreeNode] = [root]
        parent_sum = root.val

        while parent_nodes:
            children_nodes: list[TreeNode] = []
            child_sum = 0

            for parent in parent_nodes:
                parent.val = parent_sum - parent.val
                curr_child_sum = (
                    (parent.left.val if parent.left else 0) +
                    (parent.right.val if parent.right else 0)
                )

                if parent.left:
                    child_sum += parent.left.val
                    parent.left.val = curr_child_sum
                    children_nodes.append(parent.left)

                if parent.right:
                    child_sum += parent.right.val
                    parent.right.val = curr_child_sum
                    children_nodes.append(parent.right)

            parent_sum = child_sum
            parent_nodes = children_nodes

        return root


x = TreeNode(5).create_tree({
    5: (4, 9),
    4: (1, 10),
    9: (None, 7)
})

print(Solution().replace_value_in_tree(x))
