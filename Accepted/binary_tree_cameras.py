"""
https://leetcode.com/problems/binary-tree-cameras/
"""


from test_helper import TreeNode


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(currNode: TreeNode, parent: TreeNode = None) -> None:
            if currNode:
                dfs(currNode.left, currNode)
                dfs(currNode.right, currNode)

                if not parent and currNode not in covered or currNode.left not in covered or currNode.right not in covered:
                    self.rslt += 1  # Insert a camera here.
                    covered.update(
                        {currNode, parent, currNode.left, currNode.right})

        self.rslt = 0
        covered = {None}
        dfs(root)
        return self.rslt
