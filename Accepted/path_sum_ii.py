"""
https://leetcode.com/problems/path-sum-ii/
"""


from typing import List

from test_helper import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        """
        Use level-order traverse.
        """
        if not root:  # Empty tree.
            return []

        nodes, rslt = [(root, target, [])], []
        while nodes:
            nextNodes = []
            for node, value, preRoots in nodes:
                currRoots = preRoots + [node.val]
                if not node.left and not node.right and node.val == value:
                    rslt.append(currRoots)  # Found a target path.
                    continue

                if node.left:
                    nextNodes.append((node.left, value - node.val, currRoots))

                if node.right:
                    nextNodes.append((node.right, value - node.val, currRoots))

            nodes = nextNodes

        return rslt


givenDict = {
    1: (2, 6),
    2: (3, 4)
}

root = TreeNode(1)
root.create_tree(givenDict)
print(Solution().pathSum(root, 7))
