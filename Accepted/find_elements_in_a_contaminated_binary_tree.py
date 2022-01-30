"""
https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
"""


from test_helper import TreeNode


class FindElements:

    def __init__(self, root: TreeNode):
        def recover(currNode: TreeNode, currVal: int) -> TreeNode:
            currNode.val = currVal
            if currNode.left:
                recover(currNode.left, (currVal << 1) + 1)

            if currNode.right:
                recover(currNode.right, (currVal + 1) << 1)

            return currNode

        self.root = recover(root, 0)

    def find(self, target: int) -> bool:
        targetPath = bin(target + 1)[3:]  # Remove the root 1.
        i = 0
        currNode = self.root
        while currNode and i <= len(targetPath):
            if currNode.val == target:
                return True

            if targetPath[i] == '0':
                currNode = currNode.left
            else:
                currNode = currNode.right

            i += 1

        return False
