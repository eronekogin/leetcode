"""
https://leetcode.com/problems/symmetric-tree/
"""

from test_helper import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:  # Empty tree.
            return True

        nodes = [root.left, root.right]
        while nodes:
            nextNodes = []
            for i in range(0, len(nodes), 2):
                if not nodes[i] and not nodes[i + 1]:
                    continue

                if not nodes[i] or not nodes[i + 1]:
                    return False

                if nodes[i].val != nodes[i + 1].val:
                    return False

                nextNodes.append(nodes[i].left)
                nextNodes.append(nodes[i + 1].right)
                nextNodes.append(nodes[i].right)
                nextNodes.append(nodes[i + 1].left)

            nodes = nextNodes

        return True
