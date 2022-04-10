"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""


from test_helper import TreeNode


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        currNode, stack = root, []
        prev, minDiff = None, float('inf')
        while currNode or stack:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left

            currNode = stack.pop()
            if prev is None:
                prev = currNode.val
            else:
                minDiff = min(minDiff, currNode.val - prev)
                prev = currNode.val

            currNode = currNode.right

        return minDiff
