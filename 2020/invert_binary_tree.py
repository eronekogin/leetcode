"""
https://leetcode.com/problems/invert-binary-tree/
"""


from test_helper import TreeNode
from collections import deque


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = deque([root])
        while queue:
            currNode = queue.popleft()
            if currNode:
                currNode.left, currNode.right = currNode.right, currNode.left
                queue.extend([currNode.left, currNode.right])

        return root
