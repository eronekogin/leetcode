"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""


from typing import List


from test_helper import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        currNodes = [root]
        rslt = []
        while currNodes:
            nextNodes, total = [], 0
            for node in currNodes:
                total += node.val
                if node.left:
                    nextNodes.append(node.left)

                if node.right:
                    nextNodes.append(node.right)

            rslt.append(total / len(currNodes))
            currNodes = nextNodes

        return rslt
