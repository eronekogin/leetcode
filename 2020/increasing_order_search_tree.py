"""
https://leetcode.com/problems/increasing-order-search-tree/
"""


from test_helper import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        currNode, stack = root, []
        newRoot = currRoot = None
        while currNode or stack:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left

            currNode = stack.pop()
            currNode.left = None
            if not newRoot:
                newRoot = currRoot = currNode
            else:
                currRoot.right = currNode
                currRoot = currRoot.right

            currNode = currNode.right

        return newRoot
