"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""


from test_helper import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Use inorder traverse on the input binary tree.
        """
        currNode, stack, cnt = root, [], 0
        while currNode or stack:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left

            currNode = stack.pop()
            cnt += 1
            if cnt == k:
                return currNode.val

            currNode = currNode.right
