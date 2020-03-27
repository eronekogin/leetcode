"""
https://leetcode.com/problems/house-robber-iii/
"""


from test_helper import TreeNode
from typing import List


class Solution:
    def rob(self, root: TreeNode) -> int:

        def rob_each(currNode: TreeNode) -> List[int]:
            """
            The returned result contains:
            1. The maximum money when the current node is not robbed.
            2. The maximum money when the current node is robbed.
            """
            if not currNode:  # Cannot rob anything.
                return [0] * 2

            left = rob_each(currNode.left)
            right = rob_each(currNode.right)

            # Calculate the max money when the current node is not robbed.
            # We could either rob its left or right node or not rob them.
            # Just get the maximum money from both cases.
            m1 = max(left) + max(right)

            # Calculate the max money when the current node is robbed.
            # In this case we should not rob either its left or right node.
            m2 = currNode.val + left[0] + right[0]

            return [m1, m2]

        return max(rob_each(root))


root = TreeNode(1)
root.create_tree(givenDict={
    1: (2, 3),
    2: (4, 5),
    3: (6, 7)
})
print(Solution().rob(root))
