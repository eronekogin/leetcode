"""
https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def post_order_traversal(root: TreeNode):
            if not root:
                return [float('inf'), float('-inf'), 0]

            lmin, lmax, lsum = post_order_traversal(root.left)
            rmin, rmax, rsum = post_order_traversal(root.right)

            if lmax < root.val < rmin:  # Current tree is a BST.
                newSum = root.val + lsum + rsum
                newMin = min(lmin, root.val)
                newMax = max(rmax, root.val)
            else:  # Curren tree is not a BST.
                newSum = max(lsum, rsum)
                newMin = float('-inf')
                newMax = float('inf')

            self.maxSum = max(self.maxSum, newSum)
            return [newMin, newMax, newSum]

        self.maxSum = 0
        post_order_traversal(root)
        return self.maxSum
