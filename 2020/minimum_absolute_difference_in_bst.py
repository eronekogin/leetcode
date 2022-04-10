"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""


from test_helper import TreeNode


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        """
        In-order traverse the BST so that each value collected are already
        in ascending order. Then simply collect the minimum difference between
        each adjacent node.
        """
        currNode, stack, minDiff, pre = root, [], float('inf'), None
        while currNode or stack:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left

            currNode = stack.pop()
            if pre is not None:
                minDiff = min(minDiff, currNode.val - pre)

            pre = currNode.val
            currNode = currNode.right

        return minDiff
