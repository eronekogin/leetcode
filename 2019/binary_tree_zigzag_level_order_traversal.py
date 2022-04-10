"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""


from typing import List

from test_helper import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  # Empty tree.
            return []

        nodes, rslt = [root], []
        leftToRight = True  # Initial direction is from left to right.
        while nodes:
            nextNodes, values = [], []
            for node in nodes:
                if node.left:
                    nextNodes.append(node.left)

                if node.right:
                    nextNodes.append(node.right)

                values.append(node.val)

            if not leftToRight:
                values = values[::-1]

            nodes = nextNodes
            rslt.append(values)
            leftToRight = not leftToRight

        return rslt


givenDict = {
    1: (2, 3),
    2: (4, None),
    3: (None, 5)
}
root = TreeNode(1)
root.create_tree(givenDict)
print(Solution().zigzagLevelOrder(root))
