"""
https://leetcode.com/problems/diameter-of-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def __init__(self):
        self.currMax = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(currNode: TreeNode) -> int:
            """
            Calculate the height of each input node.
            """
            if not currNode:
                return 0

            left, right = height(currNode.left), height(currNode.right)
            self.currMax = max(self.currMax, left + right)
            return 1 + max(left, right)

        height(root)
        return self.currMax
