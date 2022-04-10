"""
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        minLevel, maxSum = 0, float('-inf')
        currLevel, currNodes, currSum = 1, [root], root.val
        while currNodes:
            if currSum > maxSum:
                minLevel, maxSum = currLevel, currSum

            nextNodes = []
            nextSum = 0
            for node in currNodes:
                if node.left:
                    nextSum += node.left.val
                    nextNodes.append(node.left)

                if node.right:
                    nextSum += node.right.val
                    nextNodes.append(node.right)

            currLevel += 1
            currSum = nextSum
            currNodes = nextNodes

        return minLevel
