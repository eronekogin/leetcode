"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


from typing import List

from test_helper import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  # Empty tree.
            return []

        nodes, rslt = [root], []
        while nodes:
            newNodes, values = [], []
            for node in nodes:
                if node.left:
                    newNodes.append(node.left)

                if node.right:
                    newNodes.append(node.right)

                values.append(node.val)

            rslt.append(values)
            nodes = newNodes

        return rslt


givenDict = {
    3: (9, 20),
    20: (15, 7)
}
root = TreeNode(3)
root.create_tree(givenDict)
print(Solution().levelOrder(root))
