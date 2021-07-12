"""
https://leetcode.com/problems/flip-equivalent-binary-trees/
"""


from test_helper import TreeNode


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is root2:
            return True

        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))


root1 = TreeNode(1)
root1.create_tree({
    1: (2, 3),
    2: (4, 5),
    5: (7, 8),
    3: (6, None)
})

root2 = TreeNode(1)
root2.create_tree({
    1: (3, 2),
    3: (None, 6),
    2: (4, 5),
    5: (8, 7)
})

print(Solution().flipEquiv(root1, root2))
