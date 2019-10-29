"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""


from typing import List
from test_helper import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # Empty tree.
            return []

        currNode, stack, rslt = root, [], []
        while currNode or stack:
            while currNode:  # Go to the left sub tree first.
                stack.append(currNode)
                rslt.append(currNode.val)
                currNode = currNode.left

            currNode = stack.pop()
            currNode = currNode.right  # Then process the right sub tree.

        return rslt
