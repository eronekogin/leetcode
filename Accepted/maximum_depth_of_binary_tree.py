"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:  # Empty tree.
            return 0

        nodes, depth = [root], 0
        while nodes:
            nextNodes = []
            depth += 1
            for node in nodes:
                if node.left:
                    nextNodes.append(node.left)

                if node.right:
                    nextNodes.append(node.right)

            nodes = nextNodes

        return depth
