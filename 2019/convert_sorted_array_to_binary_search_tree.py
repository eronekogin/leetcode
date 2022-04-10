"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

from typing import List

from test_helper import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:  # Empty tree.
            return None

        m = (len(nums) - 1) // 2
        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m + 1:])
        return root


nums = [-3, -2, 0, 2, 3]
print(Solution().sortedArrayToBST(nums).print_tree())
