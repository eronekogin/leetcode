"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""


from test_helper import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Define a helper to calculate the maximum sum for the current node.
        def curr_max(node: TreeNode) -> int:
            if not node:
                return 0

            leftSum, rightSum = curr_max(node.left), curr_max(node.right)
            self.maxSum = max(self.maxSum, leftSum + node.val + rightSum)

            # If the sum of the current node < 0, skip it from the path as
            # we always want to search for the maximum sum.
            return max(node.val + max(leftSum, rightSum), 0)

        self.maxSum = float('-inf')
        curr_max(root)
        return self.maxSum
