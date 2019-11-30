"""
https://leetcode.com/problems/binary-search-tree-iterator/
"""


from test_helper import TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        """
        Use inorder traversal.
        """
        self.stack = []
        self.currNode = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        currNode = self.currNode
        while currNode:
            self.stack.append(currNode)
            currNode = currNode.left

        currNode = self.stack.pop()
        self.currNode = currNode.right
        return currNode.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.currNode is not None or len(self.stack) > 0
