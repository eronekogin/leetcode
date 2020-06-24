"""
https://leetcode.com/problems/delete-node-in-a-bst/
"""


from test_helper import TreeNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:  # Root is the target node to be deleted.
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Update the root value with the minimum value on its right
                # sub tree, then delete the old minimum tree node.
                curr = root.right
                while curr.left:
                    curr = curr.left

                root.val = curr.val
                root.right = self.deleteNode(root.right, root.val)

        return root


root = TreeNode(5)
root.create_tree({
    5: (3, 6),
    3: (2, 4),
    6: (None, 7)
})
print(Solution().deleteNode(root, 3).print_tree())
