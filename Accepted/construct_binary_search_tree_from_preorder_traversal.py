"""
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
"""


from typing import List


from test_helper import TreeNode


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def do(start: int, end: int) -> TreeNode:
            if start > end:
                return None

            if start == end:
                return TreeNode(preorder[start])

            rootVal = preorder[start]
            left = start + 1
            while left <= end and preorder[left] < rootVal:
                left += 1

            root = TreeNode(rootVal)
            root.left = do(start + 1, left - 1)
            root.right = do(left, end)
            return root

        return do(0, len(preorder) - 1)
