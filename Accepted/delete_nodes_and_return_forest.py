"""
https://leetcode.com/problems/delete-nodes-and-return-forest/
"""


from test_helper import TreeNode


class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        def check(currNode: TreeNode) -> TreeNode or None:
            if currNode:
                currNode.left = check(currNode.left)
                currNode.right = check(currNode.right)
                if currNode.val in deletedNodes:
                    if currNode.left:
                        remainNodes.append(currNode.left)

                    if currNode.right:
                        remainNodes.append(currNode.right)

                    return None

                return currNode

        deletedNodes = set(to_delete)
        remainNodes: list[TreeNode] = []
        if root.val not in deletedNodes:
            remainNodes.append(root)

        check(root)
        return remainNodes
