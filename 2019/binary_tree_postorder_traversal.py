"""
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""


from test_helper import TreeNode
from typing import List


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # Empty tree.
            return []

        currNode, stack, rslt = root, [], []
        while currNode or stack:
            while currNode:  # Go to the left sub tree first.
                stack.append(currNode)
                currNode = currNode.left

            currNode = stack[-1]
            if not currNode.right:  # Found a leaf node.
                rslt.append(currNode.val)
                stack.pop()
                while stack and stack[-1].right == currNode:
                    # The right sub trees have been processed.
                    rslt.append(stack[-1].val)
                    currNode = stack.pop()

            if stack:
                currNode = stack[-1].right
            else:
                currNode = None

        return rslt


givenDict = {
    1: (None, 2),
    2: (3, None)
}
root = TreeNode(1)
root.create_tree(givenDict)
print(Solution().postorderTraversal(root))
