"""
https://leetcode.com/problems/create-binary-tree-from-descriptions/description/
"""


from test_helper import TreeNode


class Solution:
    """
    Solution
    """

    def create_binary_tree(self, descriptions: list[list[int]]) -> TreeNode:
        """
        create binary tree
        """
        children = set()
        nodes = {}
        for p, c, l in descriptions:
            parent = nodes.setdefault(p, TreeNode(p))
            child = nodes.setdefault(c, TreeNode(c))
            if l:
                parent.left = child
            else:
                parent.right = child

            children.add(c)

        root = (set(nodes) - set(children)).pop()

        return nodes[root]
