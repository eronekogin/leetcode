"""
https://leetcode.com/problems/deepest-leaves-sum/
"""


from test_helper import TreeNode


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        currNodes = [root]
        while currNodes:
            currSum = sum(node.val for node in currNodes)
            nextNodes = []
            for node in currNodes:
                if node.left:
                    nextNodes.append(node.left)

                if node.right:
                    nextNodes.append(node.right)

            currNodes = nextNodes

        return currSum
