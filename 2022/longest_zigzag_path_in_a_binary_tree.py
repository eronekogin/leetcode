"""
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def walk(currNode: TreeNode) -> list[int]:
            """
            Return [left, right, rslt], where:
                left is the max len from the left sub tree.
                right is the max len from the right sub tree.
                rslt is the max len from the whole sub tree.
            """
            if not currNode:
                return [-1, -1, -1]

            left, right = walk(currNode.left), walk(currNode.right)
            return [
                left[1] + 1,
                right[0] + 1,
                max(left[1] + 1, right[0] + 1, left[2], right[2])
            ]

        return walk(root)[-1]
