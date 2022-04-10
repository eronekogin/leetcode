"""
https://leetcode.com/problems/smallest-string-starting-from-leaf/
"""


from test_helper import TreeNode
from string import ascii_lowercase


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(currNode: TreeNode, currPath: list[int]) -> None:
            if not currNode:
                return

            if not currNode.left and not currNode.right:  # Found a leaf node.
                self.rslt = min(self.rslt, [currNode.val] + currPath[::-1])
                return

            if currNode.left:
                dfs(currNode.left, currPath + [currNode.val])

            if currNode.right:
                dfs(currNode.right, currPath + [currNode.val])

        self.rslt = [26]
        dfs(root, [])
        return ''.join(ascii_lowercase[i] for i in self.rslt)


root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
print(Solution().smallestFromLeaf(root))
