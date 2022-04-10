"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""


from typing import List

from test_helper import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:  # Empty tree.
            return []

        nodes, rslt = [root], []
        while nodes:
            nextNodes, values = [], []
            for node in nodes:
                if node.left:
                    nextNodes.append(node.left)

                if node.right:
                    nextNodes.append(node.right)

                values.append(node.val)

            rslt.append(values)
            nodes = nextNodes

        return rslt[::-1]
