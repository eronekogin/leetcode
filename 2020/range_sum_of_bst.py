"""
https://leetcode.com/problems/range-sum-of-bst/
"""


from test_helper import TreeNode


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def calc(currNode: TreeNode) -> int:
            if not currNode:
                return 0

            if currNode.val > high:
                return calc(currNode.left)
            elif currNode.val < low:
                return calc(currNode.right)
            else:
                return calc(currNode.left) + currNode.val + \
                    calc(currNode.right)

        return calc(root)
