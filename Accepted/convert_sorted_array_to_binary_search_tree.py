"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

from typing import List

from test_helper import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:  # Empty tree.
            return None

        l, r = 0, len(nums) - 1
        root = TreeNode(None)
        nodes = [(root, l, r)]
        while nodes:
            nextNodes = []
            for node, l, r in nodes:
                m = (l + r) // 2
                node.val = nums[m]
                if l < m:
                    node.left = TreeNode(None)
                    nextNodes.append((node.left, l, m - 1))

                if m < r:
                    node.right = TreeNode(None)
                    nextNodes.append((node.right, m + 1, r))

            nodes = nextNodes

        return root


nums = [-3, -2, 0, 2, 3]
print(Solution().sortedArrayToBST(nums).print_tree())
