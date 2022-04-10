"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""


from typing import List

from test_helper import TreeNode


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def inorder_traverse(currNode: TreeNode, x: int, y: int) -> None:
            if not currNode:
                return

            inorder_traverse(currNode.left, x - 1, y - 1)

            # -y is to make sure when sorting on the keys of nodes, the nodes
            # with smaller y axis will be output later.
            nodes[(x, -y)] = nodes.get((x, -y), []) + [currNode.val]

            inorder_traverse(currNode.right, x + 1, y - 1)

        nodes = {}  # (x, y): nodes with the same position.
        inorder_traverse(root, 0, 0)
        positions = sorted(nodes.keys())
        rslt = []
        i, n = 0, len(positions)
        while i < n:
            currNodes = sorted(nodes[positions[i]])
            while i + 1 < n and positions[i + 1][0] == positions[i][0]:
                i += 1
                currNodes += sorted(nodes[positions[i]])

            rslt.append(currNodes)
            i += 1

        return rslt


root = TreeNode(1)
root.create_tree({
    1: (2, 3),
    2: (4, 5),
    3: (6, 7)
})
print(Solution().verticalTraversal(root))
