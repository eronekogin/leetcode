"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

See https://leetcode.wang/leetcode-105-Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal.html#%E8%A7%A3%E6%B3%95%E4%BA%8C-%E8%BF%AD%E4%BB%A3-%E6%A0%88
for a detail example.
"""


from typing import List

from test_helper import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:  # Empty tree.
            return None

        root = TreeNode(preorder[0])  # Take the first preorder value as root.
        preRoots = [root]
        inIdx = 0
        for currVal in preorder[1:]:
            currRoot, currNode = preRoots[-1], TreeNode(currVal)
            if currRoot.val != inorder[inIdx]:
                # No match to the inorder values, so adding the current node
                # as the left node of the current root.
                currRoot.left = currNode
            else:
                while preRoots and preRoots[-1].val == inorder[inIdx]:
                    # Found match to the inorder values, then keep searching
                    # until arriving at the root that does not match the inorder
                    # values. Then the current node is the right node of
                    # the current root.
                    inIdx += 1
                    currRoot = preRoots.pop()

                currRoot.right = currNode

            preRoots.append(currNode)

        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(Solution().buildTree(preorder, inorder).print_tree())
