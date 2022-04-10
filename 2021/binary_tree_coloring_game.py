"""
https://leetcode.com/problems/binary-tree-coloring-game/
"""


from test_helper import TreeNode


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        """
        1. For any x, the best y is to choose one of the three neighbors of 
            node x, which are left, right and parent of node x. It could block
            out the remaining path of x and also means the total nodes in the
            chosed subtree will be what the second player could get.
        2. Then we could check the total nodes of left, right or parent
            sub trees. Notice the parent sub tree = n - left - right - 1.
        3. We should also compare the maximum value we could get from step 2
            with n >> 1, since if it is less than half of all the nodes, it
            must mean that x could get more than half of all the nodes, where
            the first player will win.
        """
        def count(root: TreeNode) -> int:
            if not root:
                return 0

            left, right = count(root.left), count(root.right)
            if root.val == x:
                cnt[0], cnt[1] = left, right

            return 1 + left + right

        cnt = [0, 0]  # [leftCnt, rightCnt]
        return count(root) >> 1 < max(max(cnt), n - sum(cnt) - 1)
