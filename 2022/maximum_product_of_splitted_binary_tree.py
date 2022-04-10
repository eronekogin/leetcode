"""
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def get_total_sum(root: TreeNode) -> int:
            if not root:
                return 0

            if root not in memo:
                memo[root] = (
                    root.val +
                    get_total_sum(root.left) +
                    get_total_sum(root.right)
                )

            return memo[root]

        memo = {}
        sumOfAllNodes = get_total_sum(root)
        maxProduct = float('-inf')
        for root in memo:
            sumOfSubNodes = memo[root]
            maxProduct = max(
                maxProduct,
                sumOfSubNodes * (sumOfAllNodes - sumOfSubNodes)
            )

        return maxProduct % (10 ** 9 + 7)
