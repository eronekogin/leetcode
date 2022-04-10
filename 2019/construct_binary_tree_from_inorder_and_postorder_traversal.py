"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""


from typing import List

from test_helper import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # Presumption: Each node of the tree contains a unique value.
        if not inorder:  # Empty tree.
            return None

        root = TreeNode(postorder[-1])
        inIdx, preRoots = -1, [root]
        for currVal in postorder[-2::-1]:
            currRoot, currNode = preRoots[-1], TreeNode(currVal)
            if currRoot.val != inorder[inIdx]:
                # No match to the inorder values, so adding the current node
                # as the right node of the current root.
                currRoot.right = currNode
            else:
                while preRoots and preRoots[-1].val == inorder[inIdx]:
                    # Found match to the inorder values, then keep searching
                    # until arriving at the root that does not match the inorder
                    # values. Then the current node is the left node of
                    # the current root.
                    inIdx -= 1
                    currRoot = preRoots.pop()

                currRoot.left = currNode

            preRoots.append(currNode)

        return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
print(Solution().buildTree(inorder, postorder).print_tree())
