"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""


from test_helper import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        currNode, preRights = root, []
        while currNode or preRights:
            while currNode and currNode.left:
                if currNode.right:
                    preRights.append(currNode.right)

                currNode.right = currNode.left
                currNode.left = None
                currNode = currNode.right

            if not currNode.right and preRights:
                currNode.right = preRights.pop()

            currNode = currNode.right


givenDict = {
    1: (2, 5),
    2: (3, 4),
    5: (None, 6)
}

root = TreeNode(1)
root.create_tree(givenDict)
Solution().flatten(root)
print(root.print_tree())
