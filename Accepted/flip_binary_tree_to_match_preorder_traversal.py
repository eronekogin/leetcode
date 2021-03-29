"""
https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
"""


from test_helper import TreeNode


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: list[int]) -> list[int]:
        def flip(root: TreeNode) -> None:
            if root:
                if root.val != voyage[self.i]:
                    self.flipped = [-1]
                    return

                self.i += 1
                if self.i < len(voyage) and root.left and \
                        root.left.val != voyage[self.i]:
                    self.flipped.append(root.val)
                    flip(root.right)
                    flip(root.left)
                else:  # No need to flip root.
                    flip(root.left)
                    flip(root.right)

        self.i = 0
        self.flipped = []
        flip(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]

        return self.flipped
