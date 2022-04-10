"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
"""


from test_helper import TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """
        Inorder traverse the BST so that the output numbers are already in
        ascending order.
        """
        currNode, stack, visited = root, [], set()
        while currNode or stack:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left

            currNode = stack.pop()
            if k - currNode.val in visited:
                return True

            visited.add(currNode.val)
            currNode = currNode.right

        return False
