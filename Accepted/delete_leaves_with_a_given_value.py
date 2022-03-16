"""
https://leetcode.com/problems/delete-leaves-with-a-given-value/
"""


from test_helper import TreeNode


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(currNode: TreeNode) -> TreeNode:
            if not currNode:
                return None

            currNode.left = dfs(currNode.left)
            currNode.right = dfs(currNode.right)
            if (
                not currNode.left and
                not currNode.right and
                currNode.val == target
            ):
                return None

            return currNode

        return dfs(root)
