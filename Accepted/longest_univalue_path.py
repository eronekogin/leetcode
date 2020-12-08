"""
https://leetcode.com/problems/longest-univalue-path/
"""


from test_helper import TreeNode


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        """
        The path is defined as the path from one node to another, without any
        branches in the middle.
        """
        def check(currNode: TreeNode) -> int:
            if not currNode:
                return 0

            leftMax, rightMax = check(currNode.left), check(currNode.right)
            leftSame = rightSame = 0
            if currNode.left and currNode.left.val == currNode.val:
                leftSame = 1 + leftMax

            if currNode.right and currNode.right.val == currNode.val:
                rightSame = 1 + rightMax

            self.rslt = max(self.rslt, leftSame + rightSame)

            return max(leftSame, rightSame)

        self.rslt = 0
        check(root)
        return self.rslt


root = TreeNode(1)
root.right = TreeNode(1)
node = root.right
node.left = TreeNode(1)
node.right = TreeNode(1)
node.left.left = TreeNode(1)
node.left.right = TreeNode(1)
node.right.left = TreeNode(1)
print(Solution().longestUnivaluePath(root))
