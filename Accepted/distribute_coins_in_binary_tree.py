"""
https://leetcode.com/problems/distribute-coins-in-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        """
        1. Root asks the left subtree, how much do you need or you've got
            extra? I'll give that/take it away to/from you via our direct edge,
            and pass it to right child, and if something remains, I'll take it.
        2. Same question is asked to the right child.
        3. Answer will be the sum of values(absolute) returned
            after the asked questions from the left(Left) and right(Right).
        4. But what should the root return to its parent? It will return that
            how much does "his tree" need/has extra. That will be the signed
            sum of its Left+Right (question's answer) + same question asked
            to current root node.
        """
        def excess(node: TreeNode) -> int:
            if not node:
                return 0

            leftExcess, rightExcess = excess(node.left), excess(node.right)
            self.moves += abs(leftExcess) + abs(rightExcess)
            return node.val + leftExcess + rightExcess - 1

        self.moves = 0
        excess(root)
        return self.moves
