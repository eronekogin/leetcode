"""
https://leetcode.com/problems/binary-tree-paths/
"""


from test_helper import TreeNode
from typing import List


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        rslt = []

        def calc_path(currNode: TreeNode, path: List[str]):
            if not currNode:
                return

            currVal = str(currNode.val)
            if currNode.left:
                calc_path(currNode.left, path + [currVal])

            if currNode.right:
                calc_path(currNode.right, path + [currVal])

            if not currNode.left and not currNode.right:
                rslt.append('->'.join(path + [currVal]))

        calc_path(root, [])
        return rslt


root = TreeNode(1)
givenDict = {
    1: (2, 3),
    2: (None, 5)
}
root.create_tree(givenDict)
print(Solution().binaryTreePaths(root))
