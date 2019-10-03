"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        Use level-order traverse.
        """
        if not root:  # Empty tree.
            return 0

        nodes, level = [root], 0
        while nodes:
            level += 1
            nextNodes = []
            for node in nodes:
                if not node.left and not node.right:  # Leaf node found.
                    return level

                if node.left:
                    nextNodes.append(node.left)

                if node.right:
                    nextNodes.append(node.right)

            nodes = nextNodes
